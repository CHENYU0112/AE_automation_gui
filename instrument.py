import pyvisa as visa

# Function to attempt instrument connection and handle errors
def connect_instrument(resource_name):
  try:
    rm = visa.ResourceManager()  # Initialize VISA Resource Manager
    instrument = rm.open_resource(resource_name)  # Open instrument resource
    print(f"Instrument '{resource_name}' connected successfully!")
    instrument.close()  # Close the connection (optional for testing)
  except visa.VisaError as error:
    print(f"Error connecting to instrument '{resource_name}': {error}")

# Define instrument resource strings (replace with your actual strings)
instrument_strings = [
    "USB0::0x0A69::0x083E::636005007924::INSTR", #load 
    "USB0::0x2A8D::0x0F02::MY56007118::INSTR",  #power supply 
    "USB0::0x2A8D::0x8501::MY59005729::INSTR",  #DAQ
    "USB0::0x0699::0x0522::B027098::INSTR"    #oscil
]

# Connect to each instrument
for instrument_string in instrument_strings:
  connect_instrument(instrument_string)

# Optional: Instrument discovery (already included in your script)
print("\nChecking for available instruments:")
rm = visa.ResourceManager()
instruments = rm.list_resources()
for instrument in instruments:
  print(instrument)