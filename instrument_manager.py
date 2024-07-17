import pyvisa
from config import INSTRUMENT_ADDRESSES, INSTRUMENT_CATEGORIES
from pverifyDrivers import _scope
from pverifyDrivers import powsup
from pverifyDrivers import daq
from pverifyDrivers import load
class InstrumentManager:
    def __init__(self):
        self.rm = pyvisa.ResourceManager()
        self.instruments = {category: {'address': 'Not detected', 'model': 'Not detected'} for category in INSTRUMENT_CATEGORIES.keys()}
        self.connected_instruments = {}
        
    def initialize_instruments(self):
        """Initialize instruments based on their detected models."""
        initialized_instruments = {}

        try:
            # Initialize electronic load
            load_address = self.get_instrument_address('load')
            load_model = self.get_instrument_model('load')
            if '63600' in load_model:
                initialized_instruments['load'] = load.Chroma63600(load_address)
            elif 'PLA800' in load_model:
                initialized_instruments['load'] = load.AMETEKPLA800(load_address)
            else:
                raise ValueError(f"Unsupported electronic load model: {load_model}")

            # Initialize power supply
            power_supply_address = self.get_instrument_address('supply')
            power_supply_model = self.get_instrument_model('supply')
            if 'N6705C' in power_supply_model:
                initialized_instruments['supply'] = powsup.N6705C(power_supply_address)
            elif 'E3633A' in power_supply_model:
                initialized_instruments['supply'] = powsup.AgE36xx(power_supply_address)
            elif '2260B' in power_supply_model or '2230' in power_supply_model:
                initialized_instruments['supply'] = powsup.Keith_2260B(power_supply_address)
            else:
                raise ValueError(f"Unsupported power supply model: {power_supply_model}")

            # Initialize DAQ
            daq_address = self.get_instrument_address('DAQ')
            daq_model = self.get_instrument_model('DAQ')
            if 'DAQ970A' in daq_model or 'DAQ973A' in daq_model:
                initialized_instruments['DAQ'] = daq.DAQ970A(daq_address)
            elif '34970' in daq_model:
                initialized_instruments['DAQ'] = daq.AG34970(daq_address)
            elif 'DAQ6510' in daq_model:
                initialized_instruments['DAQ'] = daq.Keithley6510(daq_address)
            else:
                raise ValueError(f"Unsupported DAQ model: {daq_model}")

            # Initialize oscilloscope (if needed for other tests)
            scope_address = self.get_instrument_address('o_scope')
            scope_model = self.get_instrument_model('o_scope')
            if 'MSO54' in scope_model or 'MSO56' in scope_model:
                initialized_instruments['o_scope'] = _scope.TEK_MSO5XB(scope_address, Simulate=False, Reset=True)
            elif 'MDO4104C' in scope_model:
                initialized_instruments['o_scope'] = _scope.Tkdpo4k(scope_address, Simulate=False, Reset=True)
            elif 'HDO6104A' in scope_model:
                initialized_instruments['o_scope'] = _scope.TekScope(scope_address, Simulate=False, Reset=True)
            else:
                print(f"Warning: Unsupported oscilloscope model: {scope_model}. Skipping initialization.")

        except Exception as e:
            print(f"Error initializing instruments: {str(e)}")

        return initialized_instruments

    
    def find_devices(self):
        """Detect all connected instruments."""
        resources = self.rm.list_resources()
        print(f"Available resources: {resources}")
        for address in resources:
            try:
                instrument = self.rm.open_resource(address)
                idn = instrument.query("*IDN?").strip()
                print(f"Device at {address} identified as: {idn}")
                idn_parts = idn.split(',')
                if len(idn_parts) >= 2:
                    model = idn_parts[1].strip()
                    for category, models in INSTRUMENT_CATEGORIES.items():
                        if any(m in model for m in models):
                            self.instruments[category] = {'address': address, 'model': model}
                            print(f"Categorized as {category}: {model}")
                            break
                instrument.close()
            except pyvisa.Error as e:
                print(f"Error querying device at {address}: {e}")
            except Exception as e:
                print(f"Unexpected error for device at {address}: {e}")
        
        print("Final instrument configuration:")
        for category, info in self.instruments.items():
            print(f"{category}: {info}")


    def get_instrument_address(self, category):
        """Get the address of a specific instrument category."""
        address = self.instruments[category]['address']
        if address == 'Not detected':
            raise ValueError(f"No {category} instrument detected")
        return str(address)  # Ensure the address is a string

    def connect_instruments(self):
        """Connect to all detected instruments."""
        for category, instrument_info in self.instruments.items():
            address = instrument_info['address']
            if address != 'Not detected':
                try:
                    address = str(address)  # Ensure address is a string
                    self.connected_instruments[category] = self.rm.open_resource(address)
                    print(f"Successfully connected to {category} at address: {address}")
                except Exception as e:
                    print(f"Error connecting to {category}: {e}")
    def get_instrument(self, identifier):
        """Get a specific instrument by category or address."""
        if identifier in self.connected_instruments:
            return self.connected_instruments[identifier]
        else:
            # If not found by category, try to find by address
            for category, instrument in self.connected_instruments.items():
                if hasattr(instrument, 'resource_name') and instrument.resource_name == identifier:
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
            if hasattr(instrument, 'write'):
                instrument.write("*RST")

    def get_all_instrument_info(self):
        """Get information about all connected instruments."""
        info = {}
        for category, instrument in self.connected_instruments.items():
            if hasattr(instrument, 'query'):
                info[category] = instrument.query("*IDN?").strip()
            else:
                info[category] = f"Connected (Address: {getattr(instrument, 'resource_name', 'Unknown')})"
        return info

    # def verify_connections(self):
    #     """Verify that all required instruments are connected."""
    #     required_instruments = set(INSTRUMENT_CATEGORIES.keys())
    #     connected_instruments = set(self.connected_instruments.keys())
    #     missing_instruments = required_instruments - connected_instruments
    #     if missing_instruments:
    #         raise ConnectionError(f"Missing required instruments: {', '.join(missing_instruments)}")
    #     return True

    def configure_for_test(self, test_config):
        """Configure all instruments for a specific test."""
        # This method would need to be implemented based on your specific test requirements
        pass

    def get_instrument_errors(self):
        """Get any error messages from all connected instruments."""
        errors = {}
        for category, instrument in self.connected_instruments.items():
            if hasattr(instrument, 'query'):
                error = instrument.query("SYST:ERR?").strip()
                if error != "+0,\"No error\"":
                    errors[category] = error
        return errors
    
    def get_instrument_model(self, category):
        """Get the model name of a specific instrument category."""
        return self.instruments[category]['model']    