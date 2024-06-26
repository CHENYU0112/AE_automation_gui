TEST_CONFIG = {
    'input_shunt_resistance': 0.02,
    'output_shunt_resistance': 0.005,
    'settling_time': 1
}

INSTRUMENT_ADDRESSES = {
    'supply': "USB0::0x2A8D::0x0F02::MY56007118::INSTR",  # power supply
    'load': "USB0::0x0A69::0x083E::636005007924::INSTR",  # load
    'DAQ': "USB0::0x2A8D::0x8501::MY59005729::INSTR",  # DAQ
    'o_scope': "USB0::0x0699::0x0522::B027098::INSTR"  # oscilloscope
}

CHANNELS = {
    'input_v': 101,
    'input_i': 102,
    'output_v': 103,
    'output_i': 104,
    'vcc': 105,
    'ldo': 106
}