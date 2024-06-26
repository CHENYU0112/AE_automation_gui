import pyvisa as visa

class DataLogger:
    def __init__(self, address):
        rm = visa.ResourceManager()
        self.logger = rm.open_resource(address)

    def clear(self):
        self.logger.write('*CLS')

    def configure_voltage(self, channel):
        self.logger.write(f'CONF:VOLT:DC AUTO, MAX, (@{channel})')
        self.logger.write(f'SENS:VOLT:DC:NPLC 2, (@{channel})')

    def measure_voltage(self, channel):
        return float(self.logger.query(f'MEAS:VOLT:DC? (@{channel})'))

    def close(self):
        self.logger.close()