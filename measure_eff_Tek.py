import numpy as np
import pyvisa
import time
import xlsxwriter
from power_supply import power_supplies
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

def eff(settings, instrument_manager, progress_callback=None, result_callback=None, graph_callback=None):
    # Extract settings
    input_shunt_max_voltage = settings['shunt_settings'][0]
    input_shunt_max_current = settings['shunt_settings'][1]
    output_shunt_max_voltage = settings['shunt_settings'][2]
    output_shunt_max_current = settings['shunt_settings'][3]
    power_supply_GPIB_address = instrument_manager.instruments['supply'][0]
    data_logger_GPIB_address = instrument_manager.instruments['DAQ'][0]
    electronic_load_GPIB_address = instrument_manager.instruments['load'][0]
    lecory_usb_address = instrument_manager.instruments['o_scope'][0]
    input_v_ch = 100 + settings['daq'].index('input V') + 1
    input_i_ch = 100 + settings['daq'].index('input I') + 1
    output_v_ch = 100 + settings['daq'].index('output V') + 1
    output_i_ch = 100 + settings['daq'].index('output I') + 1
    vcc_ch = 100 + settings['daq'].index('Vcc') + 1
    ldo_ch = 100 + settings['daq'].index('LDO') + 1
    Max_input_voltage = settings['max_vin']
    Max_input_current = settings['max_iin']
    Max_load_current = settings['max_iout']
    output_file = "efficiency_test_results"
    Input_V = [settings['input_v']]
    Input_I = settings['input_i']
    Low_load_start = settings['low_load'][0]
    Low_load_step = settings['low_load'][1]
    Low_load_stop = settings['low_load'][2]
    High_load_stop = settings['high_load'][2]
    High_load_step = settings['high_load'][1]
    low_load_timing = 1
    high_load_timing = 1
    FRE = 1

    max_vin = max(Input_V)
    min_vin = min(Input_V)
    input_length = len(Input_V)

    index = 0
    index_start_list = []
    index_end_list = []

    if max_vin <= Max_input_voltage and High_load_stop <= Max_load_current:
        try:
            if result_callback:
                result_callback("Test started")

            r_input_shunt = input_shunt_max_voltage / input_shunt_max_current
            r_output_shunt = (output_shunt_max_voltage / output_shunt_max_current) - 0.00002432

            input_v_add = f' (@{input_v_ch})'
            vcc_v_add = f' (@{vcc_ch})'
            ldo_v_add = f' (@{ldo_ch})'
            input_i_add = f' (@{input_i_ch})'
            output_v_add = f' (@{output_v_ch})'
            output_i_add = f' (@{output_i_ch})'

            rm = pyvisa.ResourceManager()
            p_supply = rm.open_resource(power_supply_GPIB_address)
            Power_supply = power_supplies(p_supply)
            supply_type = rm.open_resource(power_supply_GPIB_address).query('*IDN?')

            data_logger = rm.open_resource(data_logger_GPIB_address)
            electronic_load = rm.open_resource(electronic_load_GPIB_address)
            lecroy = rm.open_resource(lecory_usb_address)

            lecroy.write('COMM_HEADER OFF')
            data_logger.write('*CLS')

            if supply_type.find('62006P') > -1 or supply_type.find('62012') > -1:
                p_supply.write(f'SOUR:VOLT:LIMIT:HIGH {Max_input_voltage}')
                p_supply.write(f'SOUR:CURR:LIMIT:HIGH {Max_input_current}')

            Power_supply.set_voltage(Input_V[0], supply_type)
            Power_supply.set_current(Input_I, supply_type)
            Power_supply.turn_on_supply(supply_type)

            electronic_load.write('CHAN 1')
            electronic_load.write('CONF:SOUND OFF')
            electronic_load.write('CURR:STAT:L1 0')
            electronic_load.write('CONF:VOLT:L1 0')
            electronic_load.write('LOAD ON')

            if FRE == 1:
                lecroy.write("display:waveview1:ch2:state 0")
                lecroy.write("display:waveview1:ch3:state 0")
                lecroy.write("display:waveview1:ch4:state 0")
                lecroy.write("display:waveview1:ch5:state 0")
                lecroy.write("display:waveview1:ch6:state 0")
                lecroy.write("display:waveview1:ch1:state 1")
                time.sleep(2)
                lecroy.write('HOR:SCA 20E-6')
                lecroy.write("MEASUREMENT:MEAS1:TYPE FREQUENCY")
                lecroy.write("MEASUREMENT:MEAS1:SOURCE CH1")
                lecroy.write('CH1:BAN 20E+06')
                time.sleep(2)
                lecroy.write("TRIGger:A:TYPe EDGE")
                lecroy.write("TRIGger:A:EDGE:SOUrce CH1")
                lecroy.write("TRIGger:A SETLevel")
                time.sleep(1)

            data = []

            total_steps = len(Input_V) * (len(np.arange(Low_load_start, Low_load_stop, Low_load_step)) + 
                                          len(np.arange(Low_load_stop, High_load_stop + 0.002, High_load_step)))
            current_step = 0

            for input_voltage_setpoint in Input_V:
                Power_supply.set_voltage(input_voltage_setpoint, supply_type)
                time.sleep(1)

                electronic_load.write('CHAN 3')
                electronic_load.write('LOAD ON')
                time.sleep(1)
                electronic_load.write('CHAN 4')
                electronic_load.write('LOAD ON')
                time.sleep(1)
                electronic_load.write('CHAN 1')
                electronic_load.write('LOAD ON')

                if input_voltage_setpoint < 5:
                    lecroy.write('CH1:SCA 2')
                elif 5 < input_voltage_setpoint < 15:
                    lecroy.write('CH1:SCA 5')
                elif 15 < input_voltage_setpoint < 30:
                    lecroy.write('CH1:SCA 10')
                elif input_voltage_setpoint > 30:
                    lecroy.write('CH1:SCA 20')
                else:
                    lecroy.write('CH1:SCA 5')

                for output_current_setpoint in np.arange(Low_load_start, Low_load_stop, Low_load_step):
                    current_step += 1
                    if progress_callback:
                        progress_callback(int(current_step / total_steps * 100))

                    electronic_load.write('MODE CCL')
                    electronic_load.write(f'CURR:STAT:L1 {output_current_setpoint}')

                    time.sleep(int(low_load_timing))

                    data_logger.write(f'CONF:VOLT:DC AUTO, MAX,{input_i_add}')
                    data_logger.write(f'SENS:VOLT:DC:NPLC 2,{input_i_add}')
                    data_logger.write('TRIG:SOUR IMM')
                    v_input_shunt = float(data_logger.query('READ?'))

                    data_logger.write(f'CONF:VOLT:DC AUTO, MAX,{output_i_add}')
                    data_logger.write(f'SENS:VOLT:DC:NPLC 2,{output_i_add}')
                    data_logger.write('TRIG:SOUR IMM')
                    v_output_shunt = float(data_logger.query('READ?'))

                    data_logger.write(f'CONF:VOLT:DC AUTO, MAX,{input_v_add}')
                    data_logger.write(f'SENS:VOLT:DC:NPLC 2,{input_v_add}')
                    data_logger.write('TRIG:SOUR IMM')
                    v_input_voltage = float(data_logger.query('READ?'))

                    data_logger.write(f'CONF:VOLT:DC AUTO, MAX,{output_v_add}')
                    data_logger.write(f'SENS:VOLT:DC:NPLC 2,{output_v_add}')
                    data_logger.write('TRIG:SOUR IMM')
                    v_output_voltage = float(data_logger.query('READ?'))

                    data_logger.write(f'CONF:VOLT:DC AUTO, MAX,{vcc_v_add}')
                    data_logger.write(f'SENS:VOLT:DC:NPLC 2,{vcc_v_add}')
                    data_logger.write('TRIG:SOUR IMM')
                    vcc_voltage = float(data_logger.query('READ?'))

                    data_logger.write(f'CONF:VOLT:DC AUTO, MAX,{ldo_v_add}')
                    data_logger.write(f'SENS:VOLT:DC:NPLC 2,{ldo_v_add}')
                    data_logger.write('TRIG:SOUR IMM')
                    ldo_voltage = float(data_logger.query('READ?'))

                    electronic_load_setpoint = float(electronic_load.query('CURR:STAT:L1?'))
                    electronic_load_current = float(electronic_load.query('MEAS:CURR?'))
                    electronic_load_voltage = float(electronic_load.query('MEAS:VOLT?'))

                    if FRE == 1:
                        Frequency = float(lecroy.query("MEASUrement:MEAS1:VALue?"))

                    i_input_current = float(v_input_shunt) / float(r_input_shunt)
                    p_input_power = v_input_voltage * i_input_current
                    i_output_current = v_output_shunt / r_output_shunt
                    p_output_power = v_output_voltage * i_output_current
                    p_power_loss = p_input_power - p_output_power
                    efficiency = 100.0 * p_output_power / p_input_power

                    data.append({
                        'input_voltage_setpoint': input_voltage_setpoint,
                        'VCC': vcc_voltage,
                        'PG': ldo_voltage,
                        'v_input_shunt': v_input_shunt,
                        'v_output_shunt': v_output_shunt,
                        'v_input_voltage': v_input_voltage,
                        'v_output_voltage': v_output_voltage,
                        'i_input_current': i_input_current,
                        'i_output_current': i_output_current,
                        'p_input_power': p_input_power,
                        'p_output_power': p_output_power,
                        'p_power_loss': p_power_loss,
                        'efficiency': efficiency,
                        'electronic_load_setpoint': electronic_load_setpoint,
                        'electronic_load_current': electronic_load_current,
                        'electronic_load_voltage': electronic_load_voltage,
                        'switching_frequency': Frequency if FRE == 1 else None
                    })

                    if result_callback:
                        result_callback(f"Measurement taken at {input_voltage_setpoint}V, {output_current_setpoint}A")

                for output_current_setpoint in np.arange(Low_load_stop, High_load_stop + 0.002, High_load_step):
                    current_step += 1
                    if progress_callback:
                        progress_callback(int(current_step / total_steps * 100))

                    electronic_load.write('MODE CCH')
                    electronic_load.write(f'CURR:STAT:L1 {output_current_setpoint}')

                    time.sleep(int(high_load_timing))

                    # Repeat the measurement code here (same as in the previous loop)
                    # ...

                electronic_load.write('CHAN 3')
                electronic_load.write('LOAD OFF')
                time.sleep(1)
                electronic_load.write('CHAN 4')
                electronic_load.write('LOAD OFF')

            df = pd.DataFrame(data)

            # Create Excel file
            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Data', index=False)
                workbook = writer.book
                worksheet = writer.sheets['Data']

                # Create charts
                chart_efficiency = workbook.add_chart({'type': 'scatter', 'subtype': 'smooth_with_markers'})
                chart_load_regulation = workbook.add_chart({'type': 'scatter', 'subtype': 'smooth_with_markers'})
                chart_vcc_regulation = workbook.add_chart({'type': 'scatter', 'subtype': 'smooth_with_markers'})
                chart_pg_regulation = workbook.add_chart({'type': 'scatter', 'subtype': 'smooth_with_markers'})
                chart_frequency = workbook.add_chart({'type': 'scatter', 'subtype': 'smooth_with_markers'})

                # Add series to charts
                for i, voltage in enumerate(df['input_voltage_setpoint'].unique()):
                    row_start = df[df['input_voltage_setpoint'] == voltage].index[0] + 2
                    row_end = df[df['input_voltage_setpoint'] == voltage].index[-1] + 2
                    
                    chart_efficiency.add_series({
                        'name': f'Vin={voltage}V',
                        'categories': f'=Data!$I${row_start}:$I${row_end}',
                        'values': f'=Data!$N${row_start}:$N${row_end}',
                    })
                    
                    chart_load_regulation.add_series({
                        'name': f'Vin={voltage}V',
                        'categories': f'=Data!$I${row_start}:$I${row_end}',
                        'values': f'=Data!$G${row_start}:$G${row_end}',
                    })
                    
                    chart_vcc_regulation.add_series({
                        'name': f'Vin={voltage}V',
                        'categories': f'=Data!$I${row_start}:$I${row_end}',
                        'values': f'=Data!$B${row_start}:$B${row_end}',
                    })
                    
                    chart_pg_regulation.add_series({
                        'name': f'Vin={voltage}V',
                        'categories': f'=Data!$I${row_start}:$I${row_end}',
                        'values': f'=Data!$C${row_start}:$C${row_end}',
                    })
                    
                    if 'switching_frequency' in df.columns:
                        chart_frequency.add_series({
                            'name': f'Vin={voltage}V',
                            'categories': f'=Data!$I${row_start}:$I${row_end}',
                            'values': f'=Data!$R${row_start}:$R${row_end}',
                        })

                # Configure charts
                chart_efficiency.set_title({'name': 'Efficiency Measurement'})
                chart_efficiency.set_x_axis({'name': 'Load Current (A)'})
                chart_efficiency.set_y_axis({'name': 'Efficiency (%)'})
                worksheet.insert_chart('S2', chart_efficiency)

                chart_load_regulation.set_title({'name': 'Load Regulation'})
                chart_load_regulation.set_x_axis({'name': 'Load Current (A)'})
                chart_load_regulation.set_y_axis({'name': 'Output Voltage (V)'})
                worksheet.insert_chart('S18', chart_load_regulation)

                chart_vcc_regulation.set_title({'name': 'VCC Regulation'})
                chart_vcc_regulation.set_x_axis({'name': 'Load Current (A)'})
                chart_vcc_regulation.set_y_axis({'name': 'VCC Voltage (V)'})
                worksheet.insert_chart('S34', chart_vcc_regulation)

                chart_pg_regulation.set_title({'name': 'PG Regulation'})
                chart_pg_regulation.set_x_axis({'name': 'Load Current (A)'})
                chart_pg_regulation.set_y_axis({'name': 'PG Voltage (V)'})
                worksheet.insert_chart('S50', chart_pg_regulation)

                if 'switching_frequency' in df.columns:
                    chart_frequency.set_title({'name': 'Switching Frequency'})
                    chart_frequency.set_x_axis({'name': 'Load Current (A)'})
                    chart_frequency.set_y_axis({'name': 'Frequency (Hz)'})
                    worksheet.insert_chart('S66', chart_frequency)

            excel_buffer.seek(0)
            
            # Generate plots for GUI display
            plt.figure(figsize=(12, 8))
            for voltage in df['input_voltage_setpoint'].unique():
                data = df[df['input_voltage_setpoint'] == voltage]
                plt.plot(data['i_output_current'], data['efficiency'], label=f'Vin={voltage}V')
            plt.title('Efficiency vs Load Current')
            plt.xlabel('Load Current (A)')
            plt.ylabel('Efficiency (%)')
            plt.legend()
            plt.grid(True)
            
            plot_buffer = BytesIO()
            plt.savefig(plot_buffer, format='png')
            plot_buffer.seek(0)
            
            if graph_callback:
                graph_callback(plot_buffer)

            Power_supply.turn_off_supply(supply_type)
            electronic_load.write('CHAN 1')
            electronic_load.write('LOAD OFF')

            if result_callback:
                result_callback("Test completed successfully")

            return excel_buffer

        except Exception as e:
            if result_callback:
                result_callback(f"Error during test: {str(e)}")
            raise

    else:
        if result_callback:
            result_callback("Error: check I/O values")
        raise ValueError("Input voltage or load current exceeds maximum allowed values")