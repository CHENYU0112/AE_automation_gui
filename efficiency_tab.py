import tkinter as tk
from tkinter import ttk, messagebox
import threading
import queue
import sys
import time
import numpy as np
from io import StringIO
from efficiency_test import EfficiencyTest
<<<<<<< HEAD
from measure_eff_Tek import eff, set_stop_flag, reset_stop_flag,get_stop_flag
=======
from measure_eff_Tek import *
>>>>>>> weekly_update
from config import *





class EfficiencyTab(tk.Frame):
    def __init__(self, parent, instrument_manager, setting_frame):
        super().__init__(parent)
        self.instrument_manager = instrument_manager
        self.setting_frame = setting_frame
        self.efficiency_test = EfficiencyTest(instrument_manager)
        self.test_running = False
        self.output_queue = queue.Queue()
        self.create_widgets()

    def create_widgets(self):
        self.create_control_frame()
        self.create_results_area()
        self.create_excel_output_area()


    def create_control_frame(self):
        control_frame = tk.Frame(self, bd=2, relief=tk.RIDGE)
        control_frame.pack(pady=10, padx=10, fill=tk.X)

        self.start_button = tk.Button(control_frame, text="Start Efficiency Test", command=self.start_efficiency_test)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(control_frame, text="Stop Test", command=self.stop_efficiency_test, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(control_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
    def create_results_area(self):
<<<<<<< HEAD
        results_frame = tk.Frame(self)
        results_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, pady=10, padx=10)

        results_label = tk.Label(results_frame, text="Test Output", font=("Arial", 12, "bold"))
        results_label.pack()

        text_frame = tk.Frame(results_frame)
        text_frame.pack(expand=True, fill=tk.BOTH)

        self.results_text = tk.Text(text_frame, height=20, width=60)
        self.results_text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(text_frame, command=self.results_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.results_text.config(yscrollcommand=scrollbar.set, state=tk.DISABLED)
        
    def create_excel_output_area(self):
        excel_frame = tk.Frame(self)
        excel_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, pady=10, padx=10)

        excel_label = tk.Label(excel_frame, text="Excel Output", font=("Arial", 12, "bold"))
        excel_label.pack()

        self.excel_text = tk.Text(excel_frame, height=20, width=60)
        self.excel_text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(excel_frame, command=self.excel_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.excel_text.config(yscrollcommand=scrollbar.set, state=tk.DISABLED)
=======
        results_frame = tk.Frame(self, bd=2, relief=tk.RIDGE)
        results_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)  # Added expand=True

        # Increased height and width for both text widgets
        self.results_text = tk.Text(results_frame, height=30, width=40)
        self.results_text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, pady=10, padx=10)

        self.output_text = tk.Text(results_frame, height=30, width=80)
        self.output_text.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, pady=10, padx=10)


>>>>>>> weekly_update
        
    def start_efficiency_test(self):
        if self.test_running:
            messagebox.showwarning("Warning", "Test is already running")
            return

        try:
            settings = self.setting_frame.get_all_values()
            

            self.test_running = True
            reset_stop_flag()  # Reset the global stop flag
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

            self.redirect_output()
            self.test_thread = threading.Thread(target=self.run_test_thread, args=(settings,))
            self.test_thread.start()
<<<<<<< HEAD

          #  self.after(100, self.check_test_thread)
=======
            reset_stop_flag()
            self.after(100, self.check_test_thread)
>>>>>>> weekly_update
            self.after(100, self.update_output)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.test_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
    def redirect_output(self):
        self.old_stdout = sys.stdout
        sys.stdout = StringIO()

    def restore_output(self):
        sys.stdout = self.old_stdout

    def update_output(self):
        if self.test_running:
            output = sys.stdout.getvalue()
            if output:
                self.results_text.insert(tk.END, output)
                self.results_text.see(tk.END)
                sys.stdout.truncate(0)
                sys.stdout.seek(0)
            self.after(100, self.update_output)
            
    def run_test_thread(self, settings):
        try:
            validated_settings = self.validate_eff_data(settings)
            if validated_settings:
                self.print_validated_settings(validated_settings)
                self.setup_progress_bar(validated_settings)
                self.start_time = time.time()
<<<<<<< HEAD
                self.after(0, self.update_progress_by_time)                   
                eff(**validated_settings)
                self.update_results("Test completed successfully!")
=======
                self.after(0, self.update_progress_by_time)  # Start progress updates
                _stop_flag=False
                eff(**validated_settings)
                self.update_results(f"Stop flag set to: {get_stop_flag()}")
    
                if get_stop_flag():
                    self.update_results("Test stopped!")
                else:
                    self.update_results("Test completed successfully!")
            else:
                self.update_results("Invalid settings. Please check the input values.")
>>>>>>> weekly_update
        except Exception as e:
            self.update_results(f"Error during test: {str(e)}")
        finally:
            self.test_running = False
            reset_stop_flag()
            self.restore_output()
            self.progress_var.set(100)
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            
            
    def setup_progress_bar(self, settings):
        input_v_count = len(settings['Input_V'])
        low_load_steps = len(np.arange(settings['Low_load_start'], settings['Low_load_stop'], settings['Low_load_step']))
        high_load_steps = len(np.arange(settings['Low_load_stop'], settings['High_load_stop'] + 0.002, settings['High_load_step']))
        
        total_steps = input_v_count * (low_load_steps + high_load_steps)
        total_time = (low_load_steps * settings['low_load_timing'] + 
                    high_load_steps * settings['high_load_timing']) * input_v_count
        
        self.total_estimated_time = total_time
        self.progress_update_interval = 0.5  # Update every 0.5 seconds
        
    def update_progress_by_time(self):
        if not hasattr(self, 'start_time'):
            self.start_time = time.time()
        
        elapsed_time = time.time() - self.start_time
        progress = min(elapsed_time / self.total_estimated_time * 100, 100)
        self.progress_var.set(progress)
        
        if progress < 100 and self.test_running:
            self.after(int(self.progress_update_interval * 1000), self.update_progress_by_time)
        else:
            self.progress_var.set(100)
        

    def update_progress(self, step):
        progress = (step / self.total_progress_steps) * 100
        self.progress_var.set(progress)

    def check_if_stopped(self):
        return not self.test_running

    def check_test_thread(self):
        if self.test_thread.is_alive():
            self.after(100, self.check_test_thread)
        else:
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def stop_efficiency_test(self):
        if not self.test_running:
            return
      
        self.test_running = False
        self.update_results("Test stopped by user.")
<<<<<<< HEAD
        set_stop_flag()  # Set the global stop flag
=======
        set_stop_flag()
        

>>>>>>> weekly_update
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.progress_var.set(100)  # Set progress to 100% when stopped


    def update_progress(self, value):
        self.progress_var.set(value)

    def update_results(self, message):
        def update():
            self.results_text.config(state=tk.NORMAL)
            self.results_text.insert(tk.END, message + "\n")
            self.results_text.see(tk.END)
            self.results_text.config(state=tk.DISABLED)
        self.after(0, update)
        
    def update_excel_output(self, data):
        self.excel_text.config(state=tk.NORMAL)
        self.excel_text.delete(1.0, tk.END)
        self.excel_text.insert(tk.END, data)
        self.excel_text.config(state=tk.DISABLED)

    def lock_frame(self):
        self.start_button.config(state=tk.DISABLED)

    def unlock_frame(self):
        self.start_button.config(state=tk.NORMAL)

    def print_validated_settings(self, validated_settings):
        print_string = f"""
        Input Shunt Parameters:
            - Max Voltage: {validated_settings['input_shunt_max_voltage']}
            - Max Current: {validated_settings['input_shunt_max_current']}

        Output Shunt Parameters:
            - Max Voltage: {validated_settings['output_shunt_max_voltage']}
            - Max Current: {validated_settings['output_shunt_max_current']}

        GPIB Addresses:
            - Power Supply: {validated_settings['power_supply_GPIB_address']}
            - Data Logger: {validated_settings['data_logger_GPIB_address']}
            - Electronic Load: {validated_settings['electronic_load_GPIB_address']}
            - LeCroy: {validated_settings['lecory_usb_address']}

        Channel Assignments:
            - Input Voltage: {validated_settings['input_v_ch']}
            - Input Current: {validated_settings['input_i_ch']}
            - Output Voltage: {validated_settings['output_v_ch']}
            - Output Current: {validated_settings['output_i_ch']}
            - Vcc: {validated_settings['vcc_ch']}
            - LDO: {validated_settings['ldo_ch']}

        Maximum Ratings:
            - Input Voltage: {validated_settings['Max_input_voltage']}
            - Input Current: {validated_settings['Max_input_current']}
            - Load Current: {validated_settings['Max_load_current']}

        Output File: {validated_settings['output_file']}

        Load Sweep Parameters:
            - Input Voltage: {validated_settings['Input_V']}
            - Input Current: {validated_settings['Input_I']}

        Low Load Sweep:
            - Start: {validated_settings['Low_load_start']}
            - Step: {validated_settings['Low_load_step']}
            - Stop: {validated_settings['Low_load_stop']}

        High Load Sweep:
            - Start:{validated_settings['High_load_start']}
            - Step: {validated_settings['High_load_step']}
            - Stop: {validated_settings['High_load_stop']}

        Timing Parameters:
            - Low Load: {validated_settings['low_load_timing']}
            - High Load: {validated_settings['high_load_timing']}

        Frequency: {validated_settings['FRE']}
        """
        self.update_results(print_string)
        # Print argument name, data type, and value
        # type_string = "Argument Types and Values:\n"
        # for arg, value in validated_settings.items():
        #     arg_string = f"{arg}: {type(value)} - {value}\n"
        #     print(arg_string)  # Print to console
        #     type_string += arg_string  # Add to GUI update string

        # # Update GUI with types and values
        # self.update_results(type_string)

    def validate_eff_data(self, values):
        try:
            # Extract and validate shunt settings
            shunt_settings = values['shunt_settings']
            input_shunt_max_voltage, input_shunt_max_current, output_shunt_max_voltage, output_shunt_max_current = shunt_settings
            
            # Extract and validate GPIB addresses
            power_supply_GPIB_address = self.instrument_manager.instruments.get('supply', '')
            data_logger_GPIB_address = self.instrument_manager.instruments.get('DAQ', '')
            electronic_load_GPIB_address = self.instrument_manager.instruments.get('load', '')
            lecory_usb_address = self.instrument_manager.instruments.get('o_scope', '')
            
            # Create a mapping for DAQ channels to numeric values
            channel_mapping = {
                'input V': '101',
                'input I': '102',
                'output V': '103',
                'output I': '104',
                'Vcc': '105',
                'LDO': '106'
            }

            # Extract and validate channel assignments
            daq_channels = values['daq_channels']
            channel_assignments = {
                'input_v_ch': '',
                'input_i_ch': '',
                'output_v_ch': '',
                'output_i_ch': '',
                'vcc_ch': '',
                'ldo_ch': ''
            }

            for i, channel in enumerate(daq_channels, start=1):
                if channel in channel_mapping:
                    channel_key = f"{channel.lower().replace(' ', '_')}_ch"
                    channel_assignments[channel_key] = str(100 + i)  # Convert to string to match expected type

            # Ensure all channels are assigned
            if '' in channel_assignments.values():
                raise ValueError("Not all required channels are assigned")
            
            # Extract and validate maximum ratings
            Max_input_voltage = values['max_vin']
            Max_input_current = values['max_iin']
            Max_load_current = values['max_iout']
            
            # Extract and validate load sweep parameters
            Input_V = [values['input_v']]  # Wrap in list to match expected type
            Input_I = values['input_i']
            
            # Extract and validate low load sweep
            Low_load_start = values['low_load']['start']
            Low_load_step = values['low_load']['step']
            Low_load_stop = values['low_load']['stop']
            
            # Extract and validate high load sweep
            High_load_start = values['high_load']['start']
            High_load_stop = values['high_load']['stop']
            High_load_step = values['high_load']['step']
            
            # Extract and validate timing parameters
            low_load_timing = values['low_load']['delay']
            high_load_timing = values['high_load']['delay']
            
            # Set FRE to 1 as it's not in the original settings
            FRE = 1
            
            # Create a dictionary with all the parameters
            eff_params = {
                'input_shunt_max_voltage': input_shunt_max_voltage,
                'input_shunt_max_current': input_shunt_max_current,
                'output_shunt_max_voltage': output_shunt_max_voltage,
                'output_shunt_max_current': output_shunt_max_current,
                'power_supply_GPIB_address': power_supply_GPIB_address,
                'data_logger_GPIB_address': data_logger_GPIB_address,
                'electronic_load_GPIB_address': electronic_load_GPIB_address,
                'lecory_usb_address': lecory_usb_address,
                'Max_input_voltage': Max_input_voltage,
                'Max_input_current': Max_input_current,
                'Max_load_current': Max_load_current,
                'output_file': 'efficiency_test_results',  # You might want to generate this dynamically
                'Input_V': Input_V,
                'Input_I': Input_I,
                'Low_load_start': Low_load_start,
                'Low_load_step': Low_load_step,
                'Low_load_stop': Low_load_stop,
                'High_load_start': High_load_start,
                'High_load_stop': High_load_stop,
                'High_load_step': High_load_step,
                'low_load_timing': low_load_timing,
                'high_load_timing': high_load_timing,
                'FRE': FRE
            }
            
            # Update eff_params with the correct channel assignments
            eff_params.update(channel_assignments)
            
            # Validate data types
            for key, value in eff_params.items():
                if key in ['Input_V']:
                    if not isinstance(value, list) or not all(isinstance(v, float) for v in value):
                        raise ValueError(f"{key} must be a list of floats")
                elif key in ['FRE']:
                    if not isinstance(value, int):
                        raise ValueError(f"{key} must be an integer")
                elif key in ['power_supply_GPIB_address', 'data_logger_GPIB_address', 'electronic_load_GPIB_address', 'lecory_usb_address', 'input_v_ch', 'input_i_ch', 'output_v_ch', 'output_i_ch', 'vcc_ch', 'ldo_ch', 'output_file']:
                    if not isinstance(value, str):
                        raise ValueError(f"{key} must be a string")
                elif not isinstance(value, float):
                    raise ValueError(f"{key} must be a float")
            
            return eff_params
        
        except KeyError as e:
            raise ValueError(f"Missing required parameter: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error in validating data: {str(e)}")
            

            



 