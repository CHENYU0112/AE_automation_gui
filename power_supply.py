import pyvisa as visa

rm = visa.ResourceManager()

rm.list_resources()



"""key_usb_address = "0x2A8D::0x0F02::MY56005805"

n6705c_supply = rm.open_resource('USB0::' +key_usb_address + '::INSTR')

n6705c_supply.write('*CLS')

time.sleep(1)

#key_I_meter.write('CONF:CURR:DC AUTO, MAX,')

n6705c_supply.write('SOUR:VOLT:LEV:IMM:AMPL 12,(@1)')

n6705c_supply.write('SOUR:CURR:LEV:IMM:AMPL 2,(@1)')

n6705c_supply.write('OUTP ON,(@1)')"""



class power_supplies:
    def __init__(self, p_supply):
        self.PS = p_supply
        



    def set_voltage(self,value,address):

        v_value = str(value)

        supply_type = address

        if supply_type.find('N6705C') > -1: #for KEYSIGHT N6705C

            self.PS.write('SOUR:VOLT:LEV:IMM:AMPL ' + v_value + ',(@1)')

        else: # for CHROMA 6200 series

            self.PS.write('SOUR:VOLT ' + v_value)



    def set_current(self,value,address):

        v_value = str(value)

        supply_type = address

        if supply_type.find('N6705C') > -1: #for KEYSIGHT N6705C

            self.PS.write('SOUR:CURR:LEV:IMM:AMPL ' + v_value + ',(@1)')

        else: # for CHROMA 6200 series

            self.PS.write('SOUR:CURR ' + v_value)



    def turn_on_supply(self,address):

        supply_type = address

        if supply_type.find('N6705C') > -1: #for KEYSIGHT N6705C

            self.PS.write('OUTP ON,(@1)')

        else: # for CHROMA 6200 series

            self.PS.write('CONF:OUTP ON')



    def turn_off_supply(self,address):

        supply_type = address

        if supply_type.find('N6705C') > -1: #for KEYSIGHT N6705C

            self.PS.write('OUTP OFF,(@1)')

        else: # for CHROMA 6200 series

            self.PS.write('CONF:OUTP OFF')