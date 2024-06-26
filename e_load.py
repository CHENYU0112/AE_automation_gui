import pyvisa as visa

class ElectronicLoad:
    def __init__(self, address):
        rm = visa.ResourceManager()
        self.load = rm.open_resource(address)

    def set_channel(self, channel):
        self.load.write(f'CHAN {channel}')

    def set_cc_mode(self):
        self.load.write('MODE CCL')

    def set_current(self, current):
        self.load.write(f'CURR:STAT:L1 {current}')

    def turn_on_load(self):
        self.load.write('LOAD ON')

    def turn_off_load(self):
        self.load.write('LOAD OFF')

    def measure_current(self):
        return float(self.load.query('MEAS:CURR?'))

    def measure_voltage(self):
        return float(self.load.query('MEAS:VOLT?'))

    def close(self):
        self.load.close()