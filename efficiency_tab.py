import tkinter as tk
from tkinter import ttk, messagebox
import threading
from io import BytesIO
from PIL import Image, ImageTk
import pandas as pd
from efficiency_test import EfficiencyTest
from measure_eff_Tek import eff
from config import *

class EfficiencyTab(tk.Frame):
    def __init__(self, parent, instrument_manager, setting_frame):
        super().__init__(parent)
        self.instrument_manager = instrument_manager
        self.setting_frame = setting_frame
        self.efficiency_test = EfficiencyTest(instrument_manager)
        self.test_running = False
        self.create_widgets()

    def create_widgets(self):
        self.create_control_frame()
        self.create_results_area()

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
        paned_window = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned_window.pack(expand=True, fill=tk.BOTH, pady=10, padx=10)

        self.results_text = tk.Text(paned_window, height=20, width=40)
        paned_window.add(self.results_text)

        self.graph_frame = tk.Frame(paned_window, bg='white')
        self.graph_label = tk.Label(self.graph_frame, bg='white')
        self.graph_label.pack(expand=True, fill=tk.BOTH)
        paned_window.add(self.graph_frame)
        
    def start_efficiency_test(self):
        if self.test_running:
            messagebox.showwarning("Warning", "Test is already running")
            return

        try:
            # Setup instruments
            self.setup_instruments()

            # Get settings from setting_frame
            settings = self.setting_frame.get_all_values()
            

            # Set test running flag and update UI
            self.test_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)


           # self.run_test(settings)
            self.validate_settings(settings)


        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.test_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            
    def run_test(self, settings):
        try:
            validated_settings = validate_setting(settings)
            eff(**validated_settings)
            # self.update_progress(100)
            self.update_results("Test completed successfully!")
        except ValueError as e:
            self.update_results(f"Error in settings: {str(e)}")
        except Exception as e:
            self.update_results(f"Error during test: {str(e)}")
        finally:
            self.test_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            
    def validate_setting(settings):
        expected_types = {
            'Input_V': list,
            'Input_I': float,
            'Max_input_voltage': float,
            'Max_input_current': float,
            'Max_load_current': float,
            'Low_load_start': float,
            'Low_load_step': float,
            'Low_load_stop': float,
            'High_load_stop': float,
            'High_load_step': float,
            'input_shunt_max_voltage': float,
            'input_shunt_max_current': float,
            'output_shunt_max_voltage': float,
            'output_shunt_max_current': float,
            'input_v_ch': str,
            'input_i_ch': str,
            'output_v_ch': str,
            'output_i_ch': str,
            'vcc_ch': str,
            'ldo_ch': str
        }

        validated_settings = {}

        for key, values in settings.items():
            if key in values:
                eff_keys = values[key]
                if isinstance(eff_keys, list):
                    for i, eff_key in enumerate(eff_keys):
                        if not isinstance(values[i], expected_types[eff_key]):
                            raise ValueError(f"Invalid data type for '{eff_key}'. Expected {expected_types[eff_key]}, but got {type(values[i])}")
                        validated_settings[eff_key] = values[i]
                else:
                    if not isinstance(values, expected_types[eff_keys]):
                        raise ValueError(f"Invalid data type for '{eff_keys}'. Expected {expected_types[eff_keys]}, but got {type(values)}")
                    validated_settings[eff_keys] = values
            else:
                raise ValueError(f"Unexpected setting: '{key}'")

        return validated_settings
    

            
    def stop_efficiency_test(self):
        if not self.test_running:
            return
        self.test_running = False
        self.update_results("Test stopped by user.")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def setup_instruments(self):
        # This method should initialize your instruments
        # For now, it's just a placeholder
        pass

    def update_progress(self, value):
        self.progress_var.set(value)

    def update_results(self, message):
        self.results_text.insert(tk.END, message + "\n")
        self.results_text.see(tk.END)

    def lock_frame(self):
        self.start_button.config(state=tk.DISABLED)

    def unlock_frame(self):
        self.start_button.config(state=tk.NORMAL)