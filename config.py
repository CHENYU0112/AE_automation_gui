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