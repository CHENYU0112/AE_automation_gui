import numpy as np
import pyvisa
import time
import xlsxwriter
from config import *
from power_supply import *
from pverifyDrivers import _scope
from pverifyDrivers import powsup
from pverifyDrivers import daq
from pverifyDrivers import load


def efficiency(input_shunt_max_voltage, input_shunt_max_current, output_shunt_max_voltage, output_shunt_max_current,
        power_supply_GPIB_address, data_logger_GPIB_address, electronic_load_GPIB_address, lecory_usb_address,
        input_v_ch, input_i_ch, output_v_ch, output_i_ch, vcc_ch, ldo_ch, Max_input_voltage, Max_input_current,
        Max_load_current, Input_V, Input_I, Low_load_start, Low_load_step, Low_load_stop, High_load_start, High_load_stop,
        High_load_step, low_load_timing, high_load_timing, FRE,power_supply_channel):

    print("Debug: efficiency function started")
    results = {vin: [] for vin in Input_V}

    rm = pyvisa.ResourceManager()

    print(f"Debug: Instrument addresses - supply: {power_supply_GPIB_address}, load: {electronic_load_GPIB_address}, DAQ: {data_logger_GPIB_address}")

    electronic_load = load.Chroma63600(electronic_load_GPIB_address)
    
    power_supply = powsup.N6705C(power_supply_GPIB_address)
    power_supply_channel = power_supply.GetChannel(power_supply_channel)
    sc = _scope.TEK_MSO5XB(lecory_usb_address, Simulate=False, Reset=True)    
    data_logger = daq.DAQ970A(data_logger_GPIB_address)
 

    locals_copy = locals().copy()
    for key, value in locals_copy.items():
        print(f"{key}: {value}")

    results = {vin: [] for vin in Input_V}  # Initialize a list for each input voltage
    # Initialize variables
    vcc_voltage = 0
    ldo_voltage = 0
    v_input_shunt = 0
    v_output_shunt = 0
    v_input_voltage = 0
    v_output_voltage = 0
    i_input_current = 0
    i_output_current = 0
    p_input_power = 0
    p_output_power = 0
    p_power_loss = 0
    efficiency = 0
    electronic_load_setpoint = 0
    electronic_load_current = 0
    electronic_load_voltage = 0
    Frequency = 0
    
    print("Debug: FRE =", FRE)
    print("Debug: check_int =", isinstance(FRE, int))
    
    max_vin = max(Input_V)
    min_vin = min(Input_V)
    print(f"Debug: max_vin = {max_vin}, min_vin = {min_vin}")
    
    input_length = len(Input_V)
    print(f"Debug: input_length = {input_length}")



    if max_vin <= Max_input_voltage and High_load_stop <= Max_load_current:

        try:

            print("Test started")

            #	Input shunt values

            r_input_shunt = input_shunt_max_voltage / input_shunt_max_current  # Input max shunt voltage (V) / max shunt current (A)

            #r_output_shunt = output_shunt_max_voltage / output_shunt_max_current  # Input max shunt voltage (V) / max shunt current (A)

            r_output_shunt = (output_shunt_max_voltage / output_shunt_max_current) - 0.00002432 #calibrated for new output shunt






            power_supply_channel.Configure_VoltageLevel(Level=min(Input_V), CurrentLimit=Input_I)
            power_supply_channel.Enable(True)


            data_logger.select_function('VOLT:DC', f'(@{input_v_ch},{input_i_ch},{output_v_ch},{output_i_ch},{vcc_ch},{ldo_ch})')
            data_logger.set_nplc('VOLT:DC', 2, f'(@{input_v_ch},{input_i_ch},{output_v_ch},{output_i_ch},{vcc_ch},{ldo_ch})')
            data_logger.route_to_scan(f'(@{input_v_ch},{input_i_ch},{output_v_ch},{output_i_ch},{vcc_ch},{ldo_ch})')


            # Set up electronic load
            electronic_load.set_channel(1)
            electronic_load.set_mode('CCL')
            electronic_load.set_current(0)
            electronic_load.output('ON')






            sc_ch1 = sc.GetChannel(Index=1)

            sc_ch1.display_overlay()
                
            sc_ch1.set_measurement(MeasureIndex=1, MeasureType='FREQUENCY', State='ON', Source=1)






            for input_voltage_setpoint in Input_V:  # Set input voltage range,loops the voltage
                
                

 

                #power_supply.write('SOUR:VOLT ' + str(input_voltage_setpoint))

                power_supply_channel.Configure_VoltageLevel(Level=input_voltage_setpoint, CurrentLimit=Input_I)
                            # Now use ProbeSetup on the channel object
                sc_ch1.ProbeSetup(
                    Coupling='DC',
                    Bandwidth='20E+06',  # 20 MHz bandwidth
                    Vrange=2.5,          # This will set to 0.25 V/div (2.5/10)
                    Offset=0,
                    Position=0,
                    Impedance=50,        # 50 ohm termination
                    Probe_Attn=1         # 1x probe attenuation
                )
                sc_ch1.delete_measurement(1)
                # Adjust vertical scale to 2.5 V/div for channel 1
                sc_ch1.set_vertical_scale(1, 0.2)

                # Set termination to 50 ohm for channel 1
                sc_ch1.set_termination(1, 50)

                # Adjust horizontal scale to 500 ns/div
                sc_ch1.horscale('2us')

                # Set trigger for channel 1
                sc_ch1.set_trigger(ch=1, level=1.25, slope='RISE')

                # Reset and reconfigure the frequency measurement
                
                sc_ch1.set_measurement(MeasureIndex=1, MeasureType='FREQUENCY', State='ON', Source=1)
                sc_ch1.set_measurement(
                    MeasureIndex=2,
                    MeasureType='TIE',  # Time Interval Error, a common jitter measurement
                    State='ON',
                    Source=1  # Assuming we want to measure jitter on Channel 1
                )
                sc.set_fast_acq('ON')
                
                screenshot_filename = f"screenshot_Vin_{input_voltage_setpoint}V.png"
                sc_ch1.saveimage(screenshot_filename)

                print("input in loop is", input_voltage_setpoint) #********************************

                time.sleep(1)





                for output_current_setpoint in np.arange(Low_load_start, Low_load_stop,

                                                        Low_load_step):  # Set output current range, loops the load current
                    
                    if get_stop_flag():
                        print("Test stopped by user")
                        break
             

                  
                    

                    electronic_load.set_mode('CCL')
                    electronic_load.set_current(output_current_setpoint)





                    time.sleep(int(low_load_timing))
                    

                    measurements = data_logger.read(delay=0.1).split(',')

                    # Convert channel numbers to 0-based index
                    input_v_index = int(input_v_ch) - 101
                    input_i_index = int(input_i_ch) - 101
                    output_v_index = int(output_v_ch) - 101
                    output_i_index = int(output_i_ch) - 101
                    vcc_index = int(vcc_ch) - 101
                    ldo_index = int(ldo_ch) - 101

                    v_input_voltage = float(measurements[input_v_index])
                    v_input_shunt = float(measurements[input_i_index])
                    v_output_voltage = float(measurements[output_v_index])
                    v_output_shunt = float(measurements[output_i_index])
                    vcc_voltage = float(measurements[vcc_index])
                    ldo_voltage = float(measurements[ldo_index])



                    # Get electronic load measurements
                    electronic_load_setpoint = float(electronic_load._query('CURR:STAT:L1?'))
                    electronic_load_current = float(electronic_load._query('MEAS:CURR?'))
                    electronic_load_voltage = float(electronic_load._query('MEAS:VOLT?'))
                    


                    # Allow time for acquisition
                    time.sleep(1)

                    if FRE==1:

                        #Frequency = lecroy.query(r"""vbs? 'return=app.measure.p1.out.result.value' """)



                        #width = lecroy.query(r"""vbs? 'return=app.measure.p2.out.result.value' """)

                       
                        Frequency = float(sc_ch1.get_val_measurement(Index=1))
                       
                    #	Calculations

                    i_input_current = float(v_input_shunt) / float(r_input_shunt)

                    p_input_power = v_input_voltage * i_input_current

                    i_output_current = v_output_shunt / r_output_shunt

                    p_output_power = v_output_voltage * i_output_current

                    p_power_loss = p_input_power - p_output_power

                    efficiency = 100.0 * p_output_power / p_input_power


                    results[input_voltage_setpoint].append({
                        'input_voltage_setpoint': input_voltage_setpoint,
                        'vcc_voltage': vcc_voltage,
                        'ldo_voltage': ldo_voltage,
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
                        'electronic_load_setpoint': float(electronic_load_setpoint),
                        'electronic_load_current': float(electronic_load_current),
                        'electronic_load_voltage': float(electronic_load_voltage),
                        'switching_frequency': float(Frequency) if FRE == 1 else None
                    })
                    print('Input Voltage Set Point =', input_voltage_setpoint)
                    
                    print('low load = : ', output_current_setpoint)

                    print('VCC = ', vcc_voltage)

                    print('PG = ', ldo_voltage)

                    print('Input Shunt Voltage = ', v_input_shunt)

                    print('Output Shunt voltage = ', v_output_shunt)

                    print('Input Voltage = ', v_input_voltage)

                    print('Output Voltage = ', v_output_voltage)

                    print('Input Current = ', i_input_current)

                    print('Output Current = ', i_output_current)

                    print('Input Power = ', p_input_power)

                    print('Output Power = ', p_output_power)

                    print('Power Loss = ', p_power_loss)

                    print('Efficiency = ', efficiency, '%')

                    # print('Chroma setpoint voltage is ', float(chroma_setpoint_voltage))

                    # print('Chroma setpoint current is ', float(chroma_setpoint_current))

                    #print('Chroma voltage is ', float(chroma_voltage))

                    #print('Chroma current is ', float(chroma_current))

                    print('electronic load setpoint is ', float(electronic_load_setpoint))

                    print('electronic load current is ', float(electronic_load_current))

                    print('electronic load voltage is ', float(electronic_load_voltage))

                    print('\n\n')

                for output_current_setpoint in np.arange(High_load_start, High_load_stop + 0.002,

                                                        High_load_step):  # Set output current range, loops the load current
                    if get_stop_flag():
                        print("Test stopped by user")
                        break
                   
                    
                    
                  
             
                    electronic_load.set_mode('CCH')
                    electronic_load.set_current(output_current_setpoint)



                    time.sleep(int(high_load_timing))

                    measurements = data_logger.read(delay=0.1).split(',')

                    # Convert channel numbers to 0-based index
                    input_v_index = int(input_v_ch) - 101
                    input_i_index = int(input_i_ch) - 101
                    output_v_index = int(output_v_ch) - 101
                    output_i_index = int(output_i_ch) - 101
                    vcc_index = int(vcc_ch) - 101
                    ldo_index = int(ldo_ch) - 101

                    v_input_voltage = float(measurements[input_v_index])
                    v_input_shunt = float(measurements[input_i_index])
                    v_output_voltage = float(measurements[output_v_index])
                    v_output_shunt = float(measurements[output_i_index])
                    vcc_voltage = float(measurements[vcc_index])
                    ldo_voltage = float(measurements[ldo_index])

                    # Get electronic load measurements
                    electronic_load_setpoint = float(electronic_load._query('CURR:STAT:L1?'))
                    electronic_load_current = float(electronic_load._query('MEAS:CURR?'))
                    electronic_load_voltage = float(electronic_load._query('MEAS:VOLT?'))
                    

                    if FRE == 1:

                        #Frequency = lecroy.query(r"""vbs? 'return=app.measure.p1.out.result.value' """)



                        #width = lecroy.query(r"""vbs? 'return=app.measure.p2.out.result.value' """) # **will need to make this selectable

                        Frequency = float(sc_ch1.get_val_measurement(Index=1))

                    #	Calculations

                    i_input_current = float(v_input_shunt) / float(r_input_shunt)

                    p_input_power = v_input_voltage * i_input_current

                    i_output_current = v_output_shunt / r_output_shunt

                    p_output_power = v_output_voltage * i_output_current

                    p_power_loss = p_input_power - p_output_power

                    efficiency = 100.0 * p_output_power / p_input_power


                    results[input_voltage_setpoint].append({
                        'input_voltage_setpoint': input_voltage_setpoint,
                        'vcc_voltage': vcc_voltage,
                        'ldo_voltage': ldo_voltage,
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
                        'electronic_load_setpoint': float(electronic_load_setpoint),
                        'electronic_load_current': float(electronic_load_current),
                        'electronic_load_voltage': float(electronic_load_voltage),
                        'switching_frequency': float(Frequency) if FRE == 1 else None
                    })
                    print('Input Voltage Set Point =', input_voltage_setpoint)
                    
                    print('high load = : ', output_current_setpoint)


                    print('VCC = ', vcc_voltage)

                    print('PG = ', ldo_voltage)

                    print('Input Shunt Voltage = ', v_input_shunt)

                    print('Output Shunt voltage = ', v_output_shunt)

                    print('Input Voltage = ', v_input_voltage)

                    print('Output Voltage = ', v_output_voltage)

                    print('Input Current = ', i_input_current)

                    print('Output Current = ', i_output_current)

                    print('Input Power = ', p_input_power)

                    print('Output Power = ', p_output_power)

                    print('Power Loss = ', p_power_loss)

                    print('Efficiency = ', efficiency, '%')

                    # print('Chroma setpoint voltage is ', float(chroma_setpoint_voltage))

                    # print('Chroma setpoint current is ', float(chroma_setpoint_current))

                    #print('Chroma voltage is ', float(chroma_voltage))

                    #print('Chroma current is ', float(chroma_current))

                    print('electronic load setpoint is ', float(electronic_load_setpoint))

                    print('electronic load current is ', float(electronic_load_current))

                    print('electronic load voltage is ', float(electronic_load_voltage))
 
                    print('\n\n')
                time.sleep(1)


            electronic_load.output('OFF')

            #power_supply.write('CONF:OUTP OFF')

            power_supply_channel.Enable(False)

            print("Test Complete")

        except ZeroDivisionError:
            set_stop_flag()

            print('Run Again:division by zero issue')

            

            #power_supply.write('CONF:OUTP OFF')

            power_supply_channel.Enable(False)
            electronic_load.output('OFF')

        except PermissionError:
            set_stop_flag()

            print('CLOSE the work book and RUN AGAIN or change work book name')

    


            power_supply_channel.Enable(False)
            electronic_load.output('OFF')

        except ValueError:
            set_stop_flag()

            print('check scope frequency measurement')


            power_supply_channel.Enable(False)
            electronic_load.output('OFF')

    else:

        print("Error: check I/O values")
        


    return results
