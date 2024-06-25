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

# protection constant 
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
        'vin': 12.0,
        'iin': 5.0,
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
        'low_load': {
            'start': 0.1,
            'step': 0.1,
            'stop': 1.0
        },
        'high_load': {
            'start': 1.0,
            'step': 0.5,
            'stop': 5.0
        }
    },
    'protection': {
        'max_vin': 16.0,
        'max_iin': 5.0,
        'max_iout': 6.0
    },
    'current_shunt': {
        'input_max_v': 0.1,
        'input_max_i': 5,
        'output_max_v': 0.1,
        'output_max_i': 20
    }
}