# config.py

# Global stop flag
stop_flag = False

def set_stop_flag():
    global stop_flag
    stop_flag = True

def reset_stop_flag():
    global stop_flag
    stop_flag = False

def get_stop_flag():
    global stop_flag
    return stop_flag

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

# DAQ Options
Scope_OPTIONS = ['input V', 'SW', 'output V', 'IL', 'PGD', 'output I']

# Power Supply Channels
POWER_SUPPLY_CHANNELS = [' 1', ' 2', ' 3', ' 4']

# IC Options
IC_OPTIONS = ['DEFAULT', 'TDA48820A']

# Test Types
TEST_TYPES = ['Efficiency','Transient','Switching Node']

# Default Settings
DEFAULT_SETTINGS = {
    'power_supply': {
        'vin': 12,
        'iin': 5,
        'vin_channel': ' 1',
        'vcc': 3.3, 
        'icc': 5,  
        'vcc_channel': ' 2'  
    },
    'daq': {
        'ch1': 'input V',
        'ch2': 'input I',
        'ch3': 'output V',
        'ch4': 'output I',
        'ch5': 'Vcc',
        'ch6': 'LDO'
    },
    'scope': {
        'ch1': 'SW',
        'ch2': 'input V',
        'ch3': 'output V',
        'ch4': 'IL',
        'ch5':'PGD',
        'ch6':'output I'
    },
    'load': {
        'low_load': {'start': 0.0, 'step': 0.5, 'stop': 1.0, 'delay': 1},
        'high_load': {'start': 1.0, 'step': 1.0, 'stop': 15.0, 'delay': 1}
    },
    'protection': {
        'max_vin': 16,
        'max_iin': 6,
        'max_iout': 20
    },
    'current_shunt': {
        'input_max_v': 0.1,
        'input_max_i': 5,
        'output_max_v': 0.1,
        'output_max_i': 20
    }
}

# TDA48820A Settings
TDA48820A_SETTINGS = {
    'power_supply': {
        'vin': 12,
        'iin': 3,
        'vin_channel': ' 1',
        'vcc': 3,  
        'icc': 5,  
        'vcc_channel': ' 2'  
    },
    'daq': {
        'ch1': 'input V',
        'ch2': 'input I',
        'ch3': 'output V',
        'ch4': 'output I',
        'ch5': 'Vcc',
        'ch6': 'LDO'
    },
    'scope': {
        'ch1':   'SW',
        'ch2':  'input V',
        'ch3': 'output V',
        'ch4': 'IL',
        'ch5':'PGD',
        'ch6':'output I'
    },
    'load': {
        'low_load': {'start': 0.0, 'step': 0.2, 'stop': 1.0, 'delay': 1},
        'high_load': {'start': 1.0, 'step': 0.5, 'stop': 3.0, 'delay': 1}
    },
    'protection': {
        'max_vin': 14,
        'max_iin': 4,
        'max_iout': 15
    },
    'current_shunt': {
        'input_max_v': 0.1,
        'input_max_i': 5,
        'output_max_v': 0.1,
        'output_max_i': 20
    }
}

# IC Default Settings
IC_DEFAULT_SETTINGS = {
    'DEFAULT': DEFAULT_SETTINGS,
    'TDA48820A': TDA48820A_SETTINGS
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