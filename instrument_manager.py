from config import *
import pyvisa as visa
class InstrumentManager:
    def __init__(self):
        self.rm = visa.ResourceManager()
        self.instruments = {category: [] for category in INSTRUMENT_CATEGORIES}

    def find_devices(self):
        for dev in self.rm.list_resources():
            if 'USB0' in dev or 'GPIB0' in dev:
                device_name = self.rm.open_resource(dev).query('*IDN?')
                self.categorize_device(dev, device_name)

    def categorize_device(self, dev: str, device_name: str):
        for category, models in INSTRUMENT_CATEGORIES.items():
            if any(model in device_name for model in models):
                self.instruments[category].append(dev)
                break
