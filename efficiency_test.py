import numpy as np
import time
import xlsxwriter
from config import TEST_CONFIG, INSTRUMENT_ADDRESSES, CHANNELS

class EfficiencyTest:
    def __init__(self, instrument_manager):
        self.instrument_manager = instrument_manager
        self.config = TEST_CONFIG.copy()
        self.instruments = {}
        self.test_running = False

    def set_instruments(self, **kwargs):
        self.instruments.update(kwargs)

    def setup_instruments(self):
        for name, address in INSTRUMENT_ADDRESSES.items():
            if name not in self.instruments:
                self.instruments[name] = self.instrument_manager.get_instrument(name)

    def set_test_parameters(self, **kwargs):
        self.config.update(kwargs)

    def run_test(self):
        self.test_running = True
        try:
            if not self.instruments:
                self.setup_instruments()
            self.configure_instruments()
            self.perform_measurements()
            return "Test completed successfully"
        except Exception as e:
            return f"Error during test: {str(e)}"
        finally:
            self.cleanup()

    def configure_instruments(self):
        # Configure power supply
        supply = self.instruments['supply']
        supply.set_voltage(self.config['Input_V'])
        supply.set_current(self.config['Input_I'])
        supply.turn_on()

        # Configure electronic load
        load = self.instruments['load']
        load.set_mode('CCL')
        load.set_current(self.config['Low_load_start'])
        load.turn_on()

        # Configure DAQ
        daq = self.instruments['DAQ']
        for channel_name, channel_number in CHANNELS.items():
            daq.configure_channel(channel_number, 'VOLT:DC', 'AUTO')

        # Configure oscilloscope (if frequency measurement is enabled)
        if self.config['FRE']:
            scope = self.instruments['o_scope']
            # Add oscilloscope configuration here

    def perform_measurements(self):
        workbook = xlsxwriter.Workbook(self.config['output_file'] + '.xlsx')
        worksheet = workbook.add_worksheet()

        # Add headers to worksheet

        for input_voltage in self.config['Input_V']:
            self.instruments['supply'].set_voltage(input_voltage)
            
            # Low load measurements
            for output_current in np.arange(self.config['Low_load_start'], 
                                            self.config['Low_load_stop'],
                                            self.config['Low_load_step']):
                if not self.test_running:
                    break
                self.measure_and_record(output_current, worksheet)
                time.sleep(self.config['low_load_timing'])

            # High load measurements
            for output_current in np.arange(self.config['Low_load_stop'], 
                                            self.config['High_load_stop'] + 0.002,
                                            self.config['High_load_step']):
                if not self.test_running:
                    break
                self.measure_and_record(output_current, worksheet)
                time.sleep(self.config['high_load_timing'])

        self.create_charts(workbook, worksheet)
        workbook.close()

    def measure_and_record(self, output_current, worksheet):
        # Set electronic load current
        self.instruments['load'].set_current(output_current)

        # Measure voltages and currents using DAQ
        measurements = self.measure_voltages_and_currents()

        # Calculate efficiency
        efficiency = self.calculate_efficiency(measurements)

        # Record data in worksheet
        # Add code to write measurements and calculated values to worksheet

    def measure_voltages_and_currents(self):
        daq = self.instruments['DAQ']
        measurements = {}
        for channel_name, channel_number in CHANNELS.items():
            measurements[channel_name] = daq.measure(channel_number)
        return measurements

    def calculate_efficiency(self, measurements):
        input_power = measurements['input_v'] * measurements['input_i']
        output_power = measurements['output_v'] * measurements['output_i']
        return (output_power / input_power) * 100

    def create_charts(self, workbook, worksheet):
        # Implement chart creation logic here
        pass

    def stop_test(self):
        self.test_running = False

    def cleanup(self):
        for instrument in self.instruments.values():
            instrument.close()