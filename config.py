# config.py


# INSTRUMENT_ADDRESSES
INSTRUMENT_ADDRESSES = {
    #supply
    'Keithley_2230-30-6': "USB0::0x05E6::0x2230::8052250147776700086::INSTR",
    'Keysight_E3633A': "USB0::0x2A8D::0x3302::MY61000357::INSTR",
    'Keysight_N6705C': "USB0::0x2A8D::0x0F02::MY56006352::INSTR",
    'Keithley_2260B-30-108': "ASRL4::INSTR",
    'Keithley_2230G-30-1': "USB0::0x05E6::0x2230::9209788::INSTR",
    
    #meter
    'Keysight_2461': "USB0::0x05E6::0x2461::04574506::INSTR",
    'Keysight_34465A': "USB0::0x2A8D::0x0101::MY60085233::INSTR",
    
    #scope
    'Tektronix_MDO4104C': "USB0::0x0699::0x0456::B021134::INSTR",
    'Tektronix_MSO54': "USB0::0x0699::0x0522::B013692::INSTR",
    'Teledyne_T3AFG120': "USB0::0xF4ED::0xEE3A::T010ZC21190190::INSTR",
    
    #function generator
    'Teledyne_8108_HDO': "USB0::0x05FF::0x1023::5004N60791::INSTR",
    'Tektronix_AFG31152': "USB0::0x0699::0x035C::B010673::INSTR",
    
    #e-load
    'Keysight_EL34243A': "USB0::0x2A8D::0x3902::MY61001578::INSTR",
    'Keithley_2380-120-60': "ASRL3::INSTR, Address=1",
    'Ametek_PLA800-60-300': "ASRL3::INSTR, Address=4",
    'Chroma_Electronic_Load': "USB0::0x0A69::0x0879::639034L01393::INSTR",
    
    #DAQ
    'Keithley_6510' : "USB0::0x05E6::0x6510::04569274::INSTR"
}

# Instrument Categories
INSTRUMENT_CATEGORIES = {
    'supply': ['2230', 'E3633A', '2260B', 'N6705C', '2230G'],
    'o_scope': ['HDO6104A', 'MSO56', 'MSO54' ,'MDO4104C'  ,'T3AFG120'],
    'load': ['63600' ,'EL34243A' , '2380' ,'PLA800'],
    'DAQ': ['34970', 'DAQ973' ,'DAQ6510'],
    'meter': ['2461', '34465A']
}

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

# Validation Constants
MIN_INPUT_VOLTAGE = 4
MAX_INPUT_VOLTAGE = 16
MAX_OUTPUT_CURRENT = 20

# DAQ Options
DAQ_OPTIONS = ['input V', 'input I', 'output V', 'output I', 'Vcc', 'LDO']

# Scope Options
Scope_OPTIONS = ['input V', 'SW', 'output V', 'IL', 'PGD', 'output I']

# Power Supply Channels
POWER_SUPPLY_CHANNELS = [' 1', ' 2', ' 3', ' 4']

# IC Options
IC_OPTIONS = ['DEFAULT', 'TDA48820A']

# Test Types
TEST_TYPES = ['Efficiency', 'Transient', 'Switching Node']

# Default Settings for each test type
EFFICIENCY_DEFAULT_SETTINGS = {
    'power_supply': {
        'vin': 10,
        'iin': 5,
        'vin_channel': ' 1',
        'vcc': 3.3, 
        'icc': 1,  
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

TRANSIENT_DEFAULT_SETTINGS = {
    'power_supply': {
        'vin': 12,
        'iin': 5,
        'vin_channel': ' 1',
        'vcc': 3.3,
        'icc': 1,
        'vcc_channel': ' 2'
    },
    'scope': {
        'ch1': 'SW',
        'ch2': 'input V',
        'ch3': 'output V',
        'ch4': 'IL',
        'ch5': 'PGD',
        'ch6': 'output I',
        'default_us_div': 1,
        'default_persistence': False
    },
    'load': {
        'i_low': 1,
        'i_high': 3,
        'low_time': 100,
        'high_time': 100,
        'rising_sr': 1,
        'falling_sr': 1,
        'default_load_level': 'L'
    },
    'protection': {
        'max_vin': 16,
        'max_iin': 6,
        'max_iout': 20
    },
    'pass_fail': {
        'overshoot': 5,  # in %
        'undershoot': 5  # in %
    }
}

SWITCHING_NODE_DEFAULT_SETTINGS = {
    'power_supply': {
        'vin': [5,9,12,16],
        'iin': 5,
        'vin_channel': ' 1',
        'vcc': 3.3,
        'icc': 1,
        'vcc_channel': ' 2'
    },
    'scope': {
        'ch1': 'SW',
        'ch2': 'input V',
        'ch3': 'output V',
        'ch4': 'IL',
        'ch5': 'PGD',
        'ch6': 'output I',
        'default_us_div': 0.1,
        'default_persistence': True
    },
    'load': {
        'load_values': [0,5,10]
    },
    'protection': {
        'max_vin': 16,
        'max_iin': 6,
        'max_iout': 20
    }
}

# Default Settings
DEFAULT_SETTINGS = {
    'Efficiency': EFFICIENCY_DEFAULT_SETTINGS,
    'Transient': TRANSIENT_DEFAULT_SETTINGS,
    'Switching Node': SWITCHING_NODE_DEFAULT_SETTINGS
}

# TDA48820A Settings
TDA48820A_SETTINGS = {
    'Efficiency': {
        'power_supply': {
            'vin': 12,
            'iin': 3,
            'vin_channel': ' 1',
            'vcc': 3,  
            'icc': 1,  
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
    },
    'Transient': {
        'power_supply': {
            'vin': 12,
            'iin': 3,
            'vin_channel': ' 1',
            'vcc_enabled': False,
            'vcc': 3,  
            'icc': 1,  
            'vcc_channel': ' 2'  
        },
        'scope': {
            'ch1': 'SW',
            'ch2': 'input V',
            'ch3': 'output V',
            'ch4': 'IL',
            'ch5': 'PGD',
            'ch6': 'output I',
            'default_us_div': 40,
            'default_persistence': False
        },
        'load': {
            'i_low': 0,
            'i_high': 10,
            'low_time': 100,
            'high_time': 100,
            'rising_sr': 8,
            'falling_sr': 8,
            'default_load_level': 'H'
        },
        'protection': {
            'max_vin': 14,
            'max_iin': 4,
            'max_iout': 15
        },
        'pass_fail': {
            'overshoot': 5,  # in %
            'undershoot': 5  # in %
        },
    },
    'Switching Node': {
        'power_supply': {
            'vin': [5,9],
            'iin': 3,
            'vin_channel': ' 1',
            'vcc': 3,
            'icc': 1,
            'vcc_channel': ' 2'
        },
        'scope': {
            'ch1': 'SW',
            'ch2': 'input V',
            'ch3': 'output V',
            'ch4': 'IL',
            'ch5': 'PGD',
            'ch6': 'output I',
            'default_us_div': 0.1,
            'default_persistence': True
        },
        'load': {
            'load_values': [0,5,10]
        },
        'protection': {
            'max_vin': 14,
            'max_iin': 4,
            'max_iout': 15
        }
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



# CHANNELS
CHANNELS = {
    'input_v': 101,
    'input_i': 102,
    'output_v': 103,
    'output_i': 104,
    'vcc': 105,
    'ldo': 106
}