
import numpy as np

import pyvisa

import time

import xlsxwriter

from power_supply import *



#from measure_eff_config import input_shunt_max_voltage, input_shunt_max_current, output_shunt_max_voltage, \

    #output_shunt_max_current, power_supply_GPIB_address, data_logger_GPIB_address, \

    #electronic_load_GPIB_address, lecory_usb_address, input_v_ch, input_i_ch, output_v_ch, output_i_ch, VCC, temp_type, \

    #Max_input_voltage, Max_input_current, Max_output_voltage, Max_load_current, output_file, \

    #Input_V, Input_I, Low_load_start, Low_load_step, Low_load_stop, High_load_stop, High_load_step, low_load_timing,\

    #high_load_timing



def eff(input_shunt_max_voltage, input_shunt_max_current, output_shunt_max_voltage, output_shunt_max_current,

        power_supply_GPIB_address, data_logger_GPIB_address, electronic_load_GPIB_address, lecory_usb_address,

        input_v_ch, input_i_ch, output_v_ch, output_i_ch, vcc_ch, ldo_ch,  Max_input_voltage, Max_input_current,

        Max_load_current, output_file, Input_V, Input_I, Low_load_start, Low_load_step, Low_load_stop, High_load_stop,

        High_load_step, low_load_timing, high_load_timing, FRE):
    print(f"""
        Input Shunt Parameters:
            - Max Voltage: {input_shunt_max_voltage}
            - Max Current: {input_shunt_max_current}

        Output Shunt Parameters:
            - Max Voltage: {output_shunt_max_voltage}
            - Max Current: {output_shunt_max_current}

        GPIB Addresses:
            - Power Supply: {power_supply_GPIB_address}
            - Data Logger: {data_logger_GPIB_address}
            - Electronic Load: {electronic_load_GPIB_address}
            - LeCroy: {lecory_usb_address}

        Channel Assignments:
            - Input Voltage: {input_v_ch}
            - Input Current: {input_i_ch}
            - Output Voltage: {output_v_ch}
            - Output Current: {output_i_ch}
            - Vcc: {vcc_ch}
            - LDO: {ldo_ch}

        Maximum Ratings:
            - Input Voltage: {Max_input_voltage}
            - Input Current: {Max_input_current}
            - Load Current: {Max_load_current}

        Output File: {output_file}

        Load Sweep Parameters:
            - Input Voltage: {Input_V}
            - Input Current: {Input_I}

        Low Load Sweep:
            - Start: {Low_load_start}
            - Step: {Low_load_step}
            - Stop: {Low_load_stop}

        High Load Sweep:
            - Start: (implicitly defined by Low_load_stop)
            - Step: {High_load_step}
            - Stop: {High_load_stop}

        Timing Parameters:
            - Low Load: {low_load_timing}
            - High Load: {high_load_timing}

        Frequency: {FRE}
        """)
    #FRE = 1

    print("FRE = ", FRE)

    check_int = isinstance(FRE, int)

    print(check_int)

    max_vin = max(Input_V)

    min_vin = min(Input_V)

    print(min_vin)

    input_length = len(Input_V)



    index = 0

    index2 = 0

    index3 = 0

    index4 = 3

    index_start_list = []

    index_end_list = []



    if max_vin <= Max_input_voltage and High_load_stop <= Max_load_current:

        try:

            print("Test started")

            #	Input shunt values

            r_input_shunt = input_shunt_max_voltage / input_shunt_max_current  # Input max shunt voltage (V) / max shunt current (A)

            #r_output_shunt = output_shunt_max_voltage / output_shunt_max_current  # Input max shunt voltage (V) / max shunt current (A)

            r_output_shunt = (output_shunt_max_voltage / output_shunt_max_current) - 0.00002432 #calibrated for new output shunt



            #  DAQ address

            # temp_add=' ' + '(@' + str(temp_ch) + ')'

            input_v_add = ' ' + '(@' + str(input_v_ch) + ')'

            vcc_v_add = ' ' + '(@' + str(vcc_ch) + ')'

            ldo_v_add = ' ' + '(@' + str(ldo_ch) + ')'

            input_i_add = ' ' + '(@' + str(input_i_ch) + ')'

            output_v_add = ' ' + '(@' + str(output_v_ch) + ')'

            output_i_add = ' ' + '(@' + str(output_i_ch) + ')'



            rm = pyvisa.ResourceManager()

            rm.list_resources()

            print("we are here1")

            check_string = isinstance(power_supply_GPIB_address, str)

            print(check_string)



            #power_supply = rm.open_resource(power_supply_GPIB_address) #**********************



            p_supply = rm.open_resource(power_supply_GPIB_address)

            Power_supply = power_supplies(p_supply)

            supply_type = rm.open_resource(power_supply_GPIB_address).query('*IDN?')



            data_logger = rm.open_resource(data_logger_GPIB_address)

            electronic_load = rm.open_resource(electronic_load_GPIB_address)

            #electronic_load_5LDO = rm.open_resource('GPIB0::' + electronic_load_GPIB_address + '::INSTR')

            #electronic_load_3p3LDO = rm.open_resource('GPIB0::' + electronic_load_GPIB_address + '::INSTR')

            lecroy = rm.open_resource(lecory_usb_address)

            print("I'm here1")

            lecroy.write('COMM_HEADER OFF')  # need this command to remove "vbs" header

            data_logger.write('*CLS')

            # data_logger.write('CONF:TEMP TC,'+ temp_type  + ','+ temp_add)

            print("Here I am111")

            if supply_type.find('62006P') > -1 or supply_type.find('62012') > -1:

                p_supply.write('SOUR:VOLT:LIMIT:HIGH ' + str(Max_input_voltage))

                p_supply.write('SOUR:CURR:LIMIT:HIGH ' + str(Max_input_current))



            #power_supply.write('SOUR:VOLT ' + str(min_vin))  # Source voltage to Patron board

            Power_supply.set_voltage(Input_V, supply_type)

            #power_supply.write('SOUR:CURR ' + str(Input_I))

            Power_supply.set_current(Input_I, supply_type)

            #power_supply.write('CONF:OUTP ON')

            Power_supply.turn_on_supply(supply_type)

            #input_voltage_setpoint = float(power_supply.query('SOUR:VOLT?'))



            electronic_load.write('CHAN 1')

            #electronic_load_3p3LDO.write('CHAN 3')

            #electronic_load_5LDO.write('CHAN 4')

            electronic_load.write('CONF:SOUND OFF')

            electronic_load.write('CURR:STAT:L1 0')

            electronic_load.write('CONF:VOLT:L1 0')

            electronic_load.write('LOAD ON')



            # set up scope to measure frequency

            if FRE==1:

                #lecroy.write(r"""vbs 'app.measure.showmeasure = true ' """)

                #lecroy.write(r"""vbs 'app.measure.statson = true ' """)

                #lecroy.write(r"""vbs 'app.measure.p1.view = true ' """)

                #lecroy.write(r"""vbs 'app.measure.p1.paramengine = "Frequency" ' """)

                #lecroy.write(r"""vbs 'app.measure.p1.source1 = "C1" ' """)



                #lecroy.write(r"""vbs 'app.measure.showmeasure = true ' """)

                #lecroy.write(r"""vbs 'app.measure.statson = true ' """)

                #lecroy.write(r"""vbs 'app.measure.p2.view = true ' """)

                #lecroy.write(r"""vbs 'app.measure.p2.paramengine = "width" ' """)

                #lecroy.write(r"""vbs 'app.measure.p1.source1 = "C1" ' """)





                lecroy.write("display:waveview1:ch2:state 0")  # Turn off ch2 waveform

                lecroy.write("display:waveview1:ch3:state 0")

                lecroy.write("display:waveview1:ch4:state 0")

                lecroy.write("display:waveview1:ch5:state 0")

                lecroy.write("display:waveview1:ch6:state 0")

                lecroy.write("display:waveview1:ch1:state 1")  # turn on ch1 waveform

                time.sleep(2)

                lecroy.write('HOR:SCA 20E-6')  # set horizontal scale to 20ms

                lecroy.write("MEASUREMENT:MEAS1:TYPE FREQUENCY")  # set to measure frequency

                lecroy.write("MEASUREMENT:MEAS1:SOURCE CH1") # set the source to ch1

                lecroy.write('CH1:BAN 20E+06')  # set bandwidth to 20MHz

                time.sleep(2)

                lecroy.write("TRIGger:A:TYPe EDGE")  # set to edge trigger

                lecroy.write("TRIGger:A:EDGE:SOUrce CH1")  # set ch1 to be the edge trigger source

                lecroy.write("TRIGger:A SETLevel")  # set the triger level to 50%



                time.sleep(1)



                # set up scope to measure frequency

                #str(lecroy.write("MEASUREMENT:MEAS1:TYPE FREQUENCY"))  # set to measure frequency

                #lecroy.write("MEASUREMENT:MEAS1:TYPE FREQUENCY")  # set to measure frequency

                #lecroy.write("MEASUREMENT:MEAS1:SOURCE CH1") # set the source to ch1



            workbook = xlsxwriter.Workbook(output_file + '.xlsx')  # Name this file for if needed

            worksheet = workbook.add_worksheet()



            worksheet.write(0, 1, 'input_voltage_setpoint')

            # worksheet.write(1, 2, 'temperature')

            worksheet.write(0, 2, 'VCC')

            worksheet.write(0, 3, 'PG')

            worksheet.write(0, 4, 'v_input_shunt')

            worksheet.write(0, 5, 'v_output_shunt')

            worksheet.write(0, 6, 'v_input_voltage')

            worksheet.write(0, 7, 'v_output_voltage')

            worksheet.write(0, 8, 'i_input_current')

            worksheet.write(0, 9, 'i_output_current')

            worksheet.write(0, 10, 'p_input_power')

            worksheet.write(0, 11, 'p_output_power')

            worksheet.write(0, 12, 'p_power_loss')

            worksheet.write(0, 13, 'efficiency')

            # worksheet.write(1, 13, 'chroma_setpoint_voltage')

            # worksheet.write(1, 14, 'chroma_setpoint_current')

            worksheet.write(0, 14, 'electronic_load_setpoint')

            worksheet.write(0, 15, 'electronic_load_current')

            worksheet.write(0, 16, 'electronic_load_voltage')

            worksheet.write(0, 17, 'switching_frequency')







            for input_voltage_setpoint in Input_V:  # Set input voltage range,loops the voltage

                index = index + 1

                #power_supply.write('SOUR:VOLT ' + str(input_voltage_setpoint))

                Power_supply.set_voltage(input_voltage_setpoint, supply_type)

                print("input in loop is", input_voltage_setpoint) #********************************

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

                elif input_voltage_setpoint > 5 and input_voltage_setpoint < 15:

                    lecroy.write('CH1:SCA 5')  # set vertical scale to 10V

                elif input_voltage_setpoint > 15 and input_voltage_setpoint < 30:

                    lecroy.write('CH1:SCA 10')  # set vertical scale to 10V

                elif input_voltage_setpoint > 30:

                    lecroy.write('CH1:SCA 20')  # set vertical scale to 20V

                else:

                    lecroy.write('CH1:SCA 5')  # set vertical scale to 5V



                for output_current_setpoint in np.arange(Low_load_start, Low_load_stop,

                                                        Low_load_step):  # Set output current range, loops the load current

                    index = index + 1

                    electronic_load.write('MODE CCL')

                    electronic_load.write('CURR:STAT:L1 ', str(output_current_setpoint))



                    #electronic_load_5LDO.write('LOAD ON')

                    #electronic_load_3p3LDO.write('LOAD ON')



                    time.sleep(int(low_load_timing))

                    # temperature = float(data_logger.query('MEAS:TEMP?' + temp_add))

                    # v_input_shunt = float(data_logger.query('MEAS:VOLT:DC?' + input_i_add))

                    data_logger.write('CONF:VOLT:DC AUTO, MAX,' + input_i_add)

                    data_logger.write('SENS:VOLT:DC:NPLC 2,' + input_i_add)

                    data_logger.write('TRIG:SOUR IMM')

                    v_input_shunt = float(data_logger.query('READ?'))

                    # v_output_shunt = float(data_logger.query('MEAS:VOLT:DC?' + output_i_add))

                    data_logger.write('CONF:VOLT:DC AUTO, MAX,' + output_i_add)

                    data_logger.write('SENS:VOLT:DC:NPLC 2,' + output_i_add)

                    data_logger.write('TRIG:SOUR IMM')

                    v_output_shunt = float(data_logger.query('READ?'))

                    # v_input_voltage = float(data_logger.query('MEAS:VOLT:DC?' + input_v_add))

                    data_logger.write('CONF:VOLT:DC AUTO, MAX,' + input_v_add)

                    data_logger.write('SENS:VOLT:DC:NPLC 2,' + input_v_add)

                    data_logger.write('TRIG:SOUR IMM')

                    v_input_voltage = float(data_logger.query('READ?'))

                    # v_output_voltage = float(data_logger.query('MEAS:VOLT:DC?' + output_v_add))

                    data_logger.write('CONF:VOLT:DC AUTO, MAX,' + output_v_add)

                    data_logger.write('SENS:VOLT:DC:NPLC 2,' + output_v_add)

                    data_logger.write('TRIG:SOUR IMM')

                    v_output_voltage = float(data_logger.query('READ?'))



                    data_logger.write('CONF:VOLT:DC AUTO, MAX,' + vcc_v_add)

                    data_logger.write('SENS:VOLT:DC:NPLC 2,' + vcc_v_add)

                    data_logger.write('TRIG:SOUR IMM')

                    vcc_voltage = float(data_logger.query('READ?'))



                    data_logger.write('CONF:VOLT:DC AUTO, MAX,' + ldo_v_add)

                    data_logger.write('SENS:VOLT:DC:NPLC 2,' + ldo_v_add)

                    data_logger.write('TRIG:SOUR IMM')

                    ldo_voltage = float(data_logger.query('READ?'))





                    electronic_load_setpoint = electronic_load.query('CURR:STAT:L1?')

                    electronic_load_current = electronic_load.query('MEAS:CURR?')

                    electronic_load_voltage = electronic_load.query('MEAS:VOLT?')

                    if FRE==1:

                        #Frequency = lecroy.query(r"""vbs? 'return=app.measure.p1.out.result.value' """)



                        #width = lecroy.query(r"""vbs? 'return=app.measure.p2.out.result.value' """)

                        Frequency = float(lecroy.query("MEASUrement:MEAS1:VALue?"))  # call for value and store in variable

                    #	Calculations

                    i_input_current = float(v_input_shunt) / float(r_input_shunt)

                    p_input_power = v_input_voltage * i_input_current

                    i_output_current = v_output_shunt / r_output_shunt

                    p_output_power = v_output_voltage * i_output_current

                    p_power_loss = p_input_power - p_output_power

                    efficiency = 100.0 * p_output_power / p_input_power



                    print('Input Voltage Set Point', input_voltage_setpoint)

                    # print('Temperature = ', temperature)

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

                    if FRE==1:

                        print("Frequency = {0}".format(Frequency))



                        #print("TON = {0}".format(width))

                    print(' ')

                    worksheet.write(index, 1, input_voltage_setpoint)

                    # worksheet.write(index, 2, temperature)

                    worksheet.write(index, 2, vcc_voltage)

                    worksheet.write(index, 3, ldo_voltage)

                    worksheet.write(index, 4, v_input_shunt)

                    worksheet.write(index, 5, v_output_shunt)

                    worksheet.write(index, 6, v_input_voltage)

                    worksheet.write(index, 7, v_output_voltage)

                    worksheet.write(index, 8, i_input_current)

                    worksheet.write(index, 9, i_output_current)

                    worksheet.write(index, 10, p_input_power)

                    worksheet.write(index, 11, p_output_power)

                    worksheet.write(index, 12, p_power_loss)

                    worksheet.write(index, 13, efficiency)

                    # worksheet.write(index, 13, float(chroma_setpoint_voltage))

                    # worksheet.write(index, 14, float(chroma_setpoint_current))

                    #worksheet.write(index, 14, float(chroma_voltage))

                    #worksheet.write(index, 15, float(chroma_current))

                    worksheet.write(index, 14, float(electronic_load_setpoint))

                    worksheet.write(index, 15, float(electronic_load_current))

                    worksheet.write(index, 16, float(electronic_load_voltage))

                    if FRE==1:

                        worksheet.write(index, 17, float(Frequency))

                        #worksheet.write(index, 19, float(Frequency))



                        #worksheet.write(index, 20, float(width))



                    worksheet.write(index, 18, ' ')

                #electronic_load_5LDO.write('LOAD OFF')

                #electronic_load_3p3LDO.write('LOAD OFF')



                for output_current_setpoint in np.arange(Low_load_stop, High_load_stop + 0.002,

                                                        High_load_step):  # Set output current range, loops the load current

                    index = index + 1

                    electronic_load.write('MODE CCH')

                    electronic_load.write('CURR:STAT:L1 ', str(output_current_setpoint))



                    #electronic_load_5LDO.write('LOAD ON')

                    #electronic_load_3p3LDO.write('LOAD ON')



                    time.sleep(int(high_load_timing))

                    # temperature = float(data_logger.query('MEAS:TEMP?' + temp_add))

                    # v_input_shunt = float(data_logger.query('MEAS:VOLT:DC?' + input_i_add))

                    data_logger.write('CONF:VOLT:DC AUTO, MAX,' + input_i_add)

                    data_logger.write('SENS:VOLT:DC:NPLC 2,' + input_i_add)

                    data_logger.write('TRIG:SOUR IMM')

                    v_input_shunt = float(data_logger.query('READ?'))

                    # v_output_shunt = float(data_logger.query('MEAS:VOLT:DC?' + output_i_add))

                    data_logger.write('CONF:VOLT:DC AUTO, MAX,' + output_i_add)

                    data_logger.write('SENS:VOLT:DC:NPLC 2,' + output_i_add)

                    data_logger.write('TRIG:SOUR IMM')

                    v_output_shunt = float(data_logger.query('READ?'))

                    # v_input_voltage = float(data_logger.query('MEAS:VOLT:DC?' + input_v_add))

                    data_logger.write('CONF:VOLT:DC AUTO, MAX,' + input_v_add)

                    data_logger.write('SENS:VOLT:DC:NPLC 2,' + input_v_add)

                    data_logger.write('TRIG:SOUR IMM')

                    v_input_voltage = float(data_logger.query('READ?'))

                    # v_output_voltage = float(data_logger.query('MEAS:VOLT:DC?' + output_v_add))

                    data_logger.write('CONF:VOLT:DC AUTO, MAX,' + output_v_add)

                    data_logger.write('SENS:VOLT:DC:NPLC 2,' + output_v_add)

                    data_logger.write('TRIG:SOUR IMM')

                    v_output_voltage = float(data_logger.query('READ?'))



                    data_logger.write('CONF:VOLT:DC AUTO, MAX,' + vcc_v_add)

                    data_logger.write('SENS:VOLT:DC:NPLC 2,' + vcc_v_add)

                    data_logger.write('TRIG:SOUR IMM')

                    vcc_voltage = float(data_logger.query('READ?'))



                    data_logger.write('CONF:VOLT:DC AUTO, MAX,' + ldo_v_add)

                    data_logger.write('SENS:VOLT:DC:NPLC 2,' + ldo_v_add)

                    data_logger.write('TRIG:SOUR IMM')

                    ldo_voltage = float(data_logger.query('READ?'))



                    electronic_load_setpoint = electronic_load.query('CURR:STAT:L1?')

                    electronic_load_current = electronic_load.query('MEAS:CURR?')

                    electronic_load_voltage = electronic_load.query('MEAS:VOLT?')

                    if FRE == 1:

                        #Frequency = lecroy.query(r"""vbs? 'return=app.measure.p1.out.result.value' """)



                        #width = lecroy.query(r"""vbs? 'return=app.measure.p2.out.result.value' """) # **will need to make this selectable

                        Frequency = float(lecroy.query("MEASUrement:MEAS1:VALue?"))  # call for value and store in variable

                    #	Calculations

                    i_input_current = float(v_input_shunt) / float(r_input_shunt)

                    p_input_power = v_input_voltage * i_input_current

                    i_output_current = v_output_shunt / r_output_shunt

                    p_output_power = v_output_voltage * i_output_current

                    p_power_loss = p_input_power - p_output_power

                    efficiency = 100.0 * p_output_power / p_input_power



                    print('Input Voltage Set Point', input_voltage_setpoint)

                    # print('Temperature = ', temperature)

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

                    if FRE == 1:

                        print("Frequency = {0}".format(Frequency))



                        #print("TON = {0}".format(width))

                    print(' ')

                    worksheet.write(index, 1, input_voltage_setpoint)

                    # worksheet.write(index, 2, temperature)

                    worksheet.write(index, 2, vcc_voltage)

                    worksheet.write(index, 3, ldo_voltage)

                    worksheet.write(index, 4, v_input_shunt)

                    worksheet.write(index, 5, v_output_shunt)

                    worksheet.write(index, 6, v_input_voltage)

                    worksheet.write(index, 7, v_output_voltage)

                    worksheet.write(index, 8, i_input_current)

                    worksheet.write(index, 9, i_output_current)

                    worksheet.write(index, 10, p_input_power)

                    worksheet.write(index, 11, p_output_power)

                    worksheet.write(index, 12, p_power_loss)

                    worksheet.write(index, 13, efficiency)

                    # worksheet.write(index, 13, float(chroma_setpoint_voltage))

                    # worksheet.write(index, 14, float(chroma_setpoint_current))

                    #worksheet.write(index, 14, float(chroma_voltage))

                    #worksheet.write(index, 15, float(chroma_current))

                    worksheet.write(index, 14, float(electronic_load_setpoint))

                    worksheet.write(index, 15, float(electronic_load_current))

                    worksheet.write(index, 16, float(electronic_load_voltage))

                    if FRE == 1:

                        worksheet.write(index, 17, float(Frequency))



                        #worksheet.write(index, 18, float(width))

                    worksheet.write(index, 18, ' ')

                electronic_load.write('CHAN 3')

                electronic_load.write('LOAD OFF')

                time.sleep(1)

                electronic_load.write('CHAN 4')

                electronic_load.write('LOAD OFF')

                index = index + 1 #This is where it skip a line for each VIN

                index3 = index - 1 #FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

                index_end_list.append(index3) #List of end point of graph

                index_start_list.append(index4) #First value of list is define by index4 outside the loop then

                #innder loop of index4 takes over for the rest of the start_list

                index4 = index + 3 #This is where the second, third, fouth, ect.. graph starting point



                new_list = [None] * (len(index_start_list) + len(index_end_list)) #add lists together

                new_list[::2] = index_start_list ##add lists together

                new_list[1::2] = index_end_list ##add lists together



            index_2 = 1

            index_3 = 0

            # plotting the data

            # plotting Efficiency

            print("new_list is", new_list)



            """index_list = []

            index_list.append(index)

            print("you are here index", index_list )"""

            chart_list = workbook.add_chart({"type": "scatter", "subtype": "smooth lines and markers"})

            chart_list_1 = workbook.add_chart({"type": "scatter", "subtype": "smooth lines and markers"})

            chart_list_2 = workbook.add_chart({"type": "scatter", "subtype": "smooth lines and markers"})

            chart_list_3 = workbook.add_chart({"type": "scatter", "subtype": "smooth lines and markers"})

            chart_list_4 = workbook.add_chart({"type": "scatter", "subtype": "smooth lines and markers"})

            for i in range (len(index_start_list)):

                pos = new_list[index_2]

                #chart_list = workbook.add_chart({"type": "scatter", "subtype": "smooth lines and markers"})

                chart_list.add_series({

                    "name" : "=Sheet1!$B$" + str(pos),

                    'categories': ['Sheet1', new_list[index_3], 9, new_list[index_2], 9],

                    "values": ['Sheet1', new_list[index_3], 13, new_list[index_2], 13],

                })



                # plotting load regulation

                chart_list_1.add_series({

                    "name": "=Sheet1!$B$" + str(pos),

                    'categories': ['Sheet1', new_list[index_3], 9, new_list[index_2], 9],

                    "values": ['Sheet1', new_list[index_3], 7, new_list[index_2], 7],

                })



                # plotting 5VLDO regulation

                chart_list_2.add_series({

                    "name": "=Sheet1!$B$" + str(pos),

                    'categories': ['Sheet1', new_list[index_3], 9, new_list[index_2], 9],

                    "values": ['Sheet1', new_list[index_3], 2, new_list[index_2], 2],

                })

                # plotting 3.3VLDO regulation

                chart_list_3.add_series({

                    "name": "=Sheet1!$B$" + str(pos),

                    'categories': ['Sheet1', new_list[index_3], 9, new_list[index_2], 9],

                    "values": ['Sheet1', new_list[index_3], 3, new_list[index_2], 3],

                })

                # plotting Frequency regulation

                chart_list_4.add_series({

                    "name": "=Sheet1!$B$" + str(pos),

                    'categories': ['Sheet1', new_list[index_3], 9, new_list[index_2], 9],

                    "values": ['Sheet1', new_list[index_3], 17, new_list[index_2], 17],

                })

                index_2 = index_2 + 2

                print("index_2 is", index_2)

                index_3 = index_3 + 2

                print("index_3 is", index_3)



            pos = index_2

            print("index_2 outside loop is", index_2)

            print("pos is", pos)

            worksheet.insert_chart('E20', chart_list)

            chart_list.set_title({'name': 'Efficiency Measurement', 'name_font': {'size': 14, 'bold': True}})



            # Add x-axis label

            chart_list.set_x_axis({'name': 'Load Current(A)', 'major_gridlines': {'visible': True},
                                    'name_font': {'size': 14, 'bold': True}})



            # Add y-axis label

            chart_list.set_y_axis({'name': 'Efficiency (%)', 'name_font': {'size': 14, 'bold': True}})

            #*************************************

            worksheet.insert_chart('O20', chart_list_1)

            chart_list_1.set_title({'name': 'Load Regulation','name_font': {'size': 14, 'bold': True}})



            # Add x-axis label

            chart_list_1.set_x_axis({'name': 'Load Current(A)', 'major_gridlines': {'visible': True},

                                    'name_font': {'size': 14, 'bold': True}})



            # Add y-axis label

            chart_list_1.set_y_axis({'name': 'Output Voltage(V)', 'name_font': {'size': 14, 'bold': True}})

            # *************************************



            worksheet.insert_chart('F22', chart_list_2)

            chart_list_2.set_title({'name': 'VCC Regulation', 'name_font': {'size': 14, 'bold': True}})



            # Add x-axis label

            chart_list_2.set_x_axis({'name': 'Load Current(A)', 'major_gridlines': {'visible': True},

                                    'name_font': {'size': 14, 'bold': True}})



            # Add y-axis label

            chart_list_2.set_y_axis({'name': 'VCC Voltage(V)', 'name_font': {'size': 14, 'bold': True}})

            # *************************************



            worksheet.insert_chart('P22', chart_list_3)

            chart_list_3.set_title({'name': 'PG Regulation', 'name_font': {'size': 14, 'bold': True}})



            # Add x-axis label

            chart_list_3.set_x_axis({'name': 'Load Current(A)', 'major_gridlines': {'visible': True},

                                    'name_font': {'size': 14, 'bold': True}})



            # Add y-axis label

            chart_list_3.set_y_axis({'name': 'PG Voltage(V)', 'name_font': {'size': 14, 'bold': True}})



            worksheet.insert_chart('Q24', chart_list_4)

            chart_list_4.set_title({'name': 'FSW Regulation', 'name_font': {'size': 14, 'bold': True}})



            # Add x-axis label

            chart_list_4.set_x_axis({'name': 'Load Current(A)', 'major_gridlines': {'visible': True},

                                    'name_font': {'size': 14, 'bold': True}})



            # Add y-axis label

            chart_list_4.set_y_axis({'name': 'Frequency(Hz)', 'name_font': {'size': 14, 'bold': True}})



            workbook.close()

            electronic_load.write('CHAN 1')

            electronic_load.write('LOAD OFF')

            #power_supply.write('CONF:OUTP OFF')

            Power_supply.turn_off_supply(supply_type)

            print("Test Complete")

        except ZeroDivisionError:

            print('Run Again:division by zero issue')

            electronic_load.write('LOAD OFF')

            #power_supply.write('CONF:OUTP OFF')

            Power_supply.turn_off_supply(supply_type)

        except PermissionError:

            print('CLOSE the work book and RUN AGAIN or change work book name')

            electronic_load.write('LOAD OFF')

            #power_supply.write('CONF:OUTP OFF')

            Power_supply.turn_off_supply(supply_type)

        except ValueError:

            print('check scope frequency measurement')

            electronic_load.write('LOAD OFF')

            #power_supply.write('CONF:OUTP OFF')

            Power_supply.turn_off_supply(supply_type)



    else:

        print("Error: check I/O values")

