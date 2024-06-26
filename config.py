# config.py

# GUI Constants
WINDOW_SIZE = "2000x1200"
FONT_NORMAL = ("times new roman", 12)
FONT_BOLD = ("times new roman", 12, "bold")
FONT_TITLE = ("times new roman", 25, "bold")
BUTTON_FONT = ("Courier New", 12, "bold")

# Instrument Categories
INSTRUMENT_CATEGORIES = {
    'supply': ['E3649A', '62012', '62006P', 'N6705C'],
    'o_scope': ['HDO6104A', 'MSO56', 'MSO54'],
    'load': ['63600'],
    'DAQ': ['34970', 'DAQ973'],
    'meter': ['34461']
}

# Validation Constants
MIN_INPUT_VOLTAGE = 4
MAX_INPUT_VOLTAGE = 16
MAX_OUTPUT_CURRENT = 20

# DAQ Options
DAQ_OPTIONS = ['input V', 'input I', 'output V', 'output I', 'Vcc', 'LDO']

# Power Supply Channels
POWER_SUPPLY_CHANNELS = [' 1', ' 2', ' 3', ' 4']

# Default Settings
DEFAULT_SETTINGS = {
    'power_supply': {
        'vin': 12,
        'iin': 2,
        'channel': ' 1'
    },
    'daq': {
        'ch1': 'input V',
        'ch2': 'input I',
        'ch3': 'output V',
        'ch4': 'output I',
        'ch5': 'Vcc',
        'ch6': 'LDO'
    },
    'load': {
        'low_load': {'start': 0.1, 'step': 0.1, 'stop': 1.0},
        'high_load': {'start': 1.0, 'step': 0.5, 'stop': 5.0},
        'low_load_delay': 3, 
        'high_load_delay': 3  
    },
    'protection': {
        'max_vin': 16,
        'max_iin': 3,
        'max_iout': 6
    },
    'current_shunt': {
        'input_max_v': 0.1,
        'input_max_i': 5,
        'output_max_v': 0.1,
        'output_max_i': 20
    }
}

# Test Configuration


TEST_CONFIG = {
    'input_shunt_max_voltage': 0.1,
    'input_shunt_max_current': 5,
    'output_shunt_max_voltage': 0.1,
    'output_shunt_max_current': 20,
    'settling_time': 1,
    'max_vin': 12,
    'max_iin': 2,
    'max_iout': 5,
    'output_file': 'output',
    'low_load_timing': 1,
    'high_load_timing': 1,
    'FRE': 1
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