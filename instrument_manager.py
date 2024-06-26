import pyvisa
from config import INSTRUMENT_ADDRESSES, INSTRUMENT_CATEGORIES
from power_supply import power_supplies as PowerSupply
from e_load import ElectronicLoad
from DAQ import DataLogger as DAQ
from oscilloscope import Oscilloscope

class InstrumentManager:
    def __init__(self):
        self.rm = pyvisa.ResourceManager()
        self.instruments = {}
        self.connected_instruments = {}

    def find_devices(self):
        """Detect all connected instruments."""
        resources = self.rm.list_resources()
        for address in resources:
            try:
                instrument = self.rm.open_resource(address)
                idn = instrument.query("*IDN?").strip()
                for category, models in INSTRUMENT_CATEGORIES.items():
                    if any(model in idn for model in models):
                        self.instruments[category] = address
                        break
                instrument.close()
            except pyvisa.Error:
                pass  # Skip any devices that can't be opened or don't respond to *IDN?

    def connect_instruments(self):
        """Connect to all detected instruments."""
        for category, address in self.instruments.items():
            try:
                if category == 'supply':
                    self.connected_instruments[category] = PowerSupply(address)
                elif category == 'load':
                    self.connected_instruments[category] = ElectronicLoad(address)
                elif category == 'DAQ':
                    self.connected_instruments[category] = DAQ(address)
                elif category == 'o_scope':
                    self.connected_instruments[category] = Oscilloscope(address)
            except pyvisa.Error as e:
                print(f"Error connecting to {category}: {e}")

    def get_instrument(self, identifier):
        """Get a specific instrument by category or address."""
        if identifier in self.connected_instruments:
            return self.connected_instruments[identifier]
        else:
            # If not found by category, try to find by address
            for category, instrument in self.connected_instruments.items():
                if hasattr(instrument, 'address') and instrument.address == identifier:
                    return instrument
            raise ValueError(f"No instrument with identifier '{identifier}' is connected.")

    def disconnect_all(self):
        """Disconnect from all instruments."""
        for instrument in self.connected_instruments.values():
            if hasattr(instrument, 'close'):
                instrument.close()
        self.connected_instruments.clear()

    def reset_all(self):
        """Reset all connected instruments to their default states."""
        for instrument in self.connected_instruments.values():
            if hasattr(instrument, 'reset'):
                instrument.reset()

    def get_all_instrument_info(self):
        """Get information about all connected instruments."""
        info = {}
        for category, instrument in self.connected_instruments.items():
            if hasattr(instrument, 'get_info'):
                info[category] = instrument.get_info()
            else:
                info[category] = f"Connected (Address: {getattr(instrument, 'address', 'Unknown')})"
        return info

    def verify_connections(self):
        """Verify that all required instruments are connected."""
        required_instruments = set(INSTRUMENT_ADDRESSES.keys())
        connected_instruments = set(self.connected_instruments.keys())
        missing_instruments = required_instruments - connected_instruments
        if missing_instruments:
            raise ConnectionError(f"Missing required instruments: {', '.join(missing_instruments)}")
        return True

    def configure_for_test(self, test_config):
        """Configure all instruments for a specific test."""
        for category, instrument in self.connected_instruments.items():
            if hasattr(instrument, 'configure_for_test'):
                instrument.configure_for_test(test_config)

    def get_instrument_errors(self):
        """Get any error messages from all connected instruments."""
        errors = {}
        for category, instrument in self.connected_instruments.items():
            if hasattr(instrument, 'get_error'):
                error = instrument.get_error()
                if error:
                    errors[category] = error
        return errors