import pyvisa as visa

class Oscilloscope:
    def __init__(self, address):
        rm = visa.ResourceManager()
        self.scope = rm.open_resource(address)

    def setup(self):
        self.scope.write('COMM_HEADER OFF')
        self.scope.write("display:waveview1:ch1:state 1")
        self.scope.write('HOR:SCA 20E-6')
        self.scope.write("MEASUREMENT:MEAS1:TYPE FREQUENCY")
        self.scope.write("MEASUREMENT:MEAS1:SOURCE CH1")
        self.scope.write('CH1:BAN 20E+06')
        self.scope.write("TRIGger:A:TYPe EDGE")
        self.scope.write("TRIGger:A:EDGE:SOUrce CH1")
        self.scope.write("TRIGger:A SETLevel")

    def measure_frequency(self):
        return float(self.scope.query("MEASUrement:MEAS1:VALue?"))

    def close(self):
        self.scope.close()