import tkinter as tk
from tkinter import ttk, messagebox
import threading
import queue
import sys
from io import StringIO
from ..setting_frame.TransientTest import TransientTestFrame
from config import *
from .test_tab import TestTab
import datetime
from PIL import Image, ImageTk
from .measure_transient import transient  # Make sure this import is correct


class TransientTab(TestTab):
    def __init__(self, parent, instrument_manager, setting_frame):
        super().__init__(parent, instrument_manager, setting_frame, "Transient")
        self.results = []
        self.scope_image = None

    def create_widgets(self):
        self.create_control_frame()
        self.create_results_area()

    def create_control_frame(self):
        control_frame = tk.Frame(self, bd=2, relief=tk.RIDGE)
        control_frame.pack(pady=10, padx=10, fill=tk.X)

        self.start_button = tk.Button(control_frame, text="Start Transient Test", command=self.start_transient_test)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(control_frame, text="Stop Test", command=self.stop_transient_test, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

    def create_results_area(self):
        results_frame = tk.Frame(self, bd=2, relief=tk.RIDGE)
        results_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.results_title = tk.Label(results_frame, text="Transient Test ", font=("times new roman", 16, "bold"), bg='black', fg="white")
        self.results_title.pack(fill=tk.X, padx=5, pady=5)

        self.notebook = ttk.Notebook(results_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

        # Log tab
        log_frame = tk.Frame(self.notebook)
        self.results_text = tk.Text(log_frame, height=30, width=40)
        scrollbar = tk.Scrollbar(log_frame, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.notebook.add(log_frame, text="Log")

        # Image tab
        self.image_frame = tk.Frame(self.notebook)
        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack(fill=tk.BOTH, expand=True)
        self.notebook.add(self.image_frame, text="Scope Image")

    def start_transient_test(self):
        if self.test_running:
            messagebox.showwarning("Warning", "Test is already running")
            return

        try:
            validated_settings = self.setting_frame.current_test_frame.get_values()
            if not validated_settings:
                messagebox.showerror("Error", "No validated settings available. Please set values in the Setting Frame.")
                return
            
            self.test_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

            self.redirect_output()
            self.test_thread = threading.Thread(target=self.run_test_thread, args=(validated_settings,))
            self.test_thread.start()
            reset_stop_flag()
            self.after(100, self.check_test_thread)
            self.after(100, self.update_output)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.test_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def run_test_thread(self, validated_settings):
        print("Debug: run_test_thread started")
        try:
            self.print_validated_settings(validated_settings)
            print("Debug: About to call transient function")
            
            # Unpack the validated_settings dictionary
            selected_ic = validated_settings['selected_ic']
            power_supply = validated_settings['power_supply']
            scope = validated_settings['scope']
            scope_us_div = validated_settings['scope_us_div']
            scope_persistence = validated_settings['scope_persistence']
            load_settings = validated_settings['load_settings']
            protection = validated_settings['protection']

            self.results = transient(
                selected_ic=selected_ic,
                power_supply_settings=power_supply,
                scope_settings=scope,
                scope_us_div=scope_us_div,
                scope_persistence=scope_persistence,
                load_settings=load_settings,
                protection=protection,
                instrument_manager=self.instrument_manager
            )
            
            self.capture_scope_image()

            if get_stop_flag():
                self.update_results("Test stopped!")
            else:
                self.update_results(f"Test completed successfully!\n")
                self.update_results(f"Results: {self.results}")

        except Exception as e:
            error_message = f"Error during test: {str(e)}\n"
            error_message += "Traceback:\n"
            import traceback
            error_message += traceback.format_exc()
            self.update_results(error_message)
        finally:
            self.test_running = False
            self.restore_output()




    def stop_transient_test(self):
        if not self.test_running:
            return
        
        self.test_running = False
        self.update_results("Test stopped by user.")
        set_stop_flag()
        
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def redirect_output(self):
        self.output_buffer = StringIO()
        self.old_stdout = sys.stdout
        sys.stdout = self.output_buffer

    def restore_output(self):
        sys.stdout = self.old_stdout
        output = self.output_buffer.getvalue()
        self.output_buffer.close()
        self.update_results(output)

    def update_output(self):
        if self.test_running:
            try:
                output = self.output_buffer.getvalue()
                if output:
                    self.results_text.insert(tk.END, output)
                    self.results_text.see(tk.END)
                    self.output_buffer.truncate(0)
                    self.output_buffer.seek(0)
            except Exception as e:
                self.update_results(f"Error updating output: {str(e)}")
            finally:
                self.after(100, self.update_output)

    def check_test_thread(self):
        if self.test_thread.is_alive():
            self.after(100, self.check_test_thread)
        else:
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def update_results(self, message):
        self.after(0, lambda: self.results_text.insert(tk.END, message + "\n"))
        self.after(0, lambda: self.results_text.see(tk.END))
        self.after(0, lambda: self.results_text.update_idletasks())

    def print_validated_settings(self, validated_settings):
        print_string = f"""
        Validated Settings:
        Power Supply:
            Vin: {validated_settings['power_supply']['vin']} V
            Iin: {validated_settings['power_supply']['iin']} A
            Channel: {validated_settings['power_supply']['vin_channel']}
        VCC Enabled: {validated_settings['power_supply']['vcc_enabled']}
        scope:
            us/div: {validated_settings['scope_us_div']}
            Persistence: {validated_settings['scope_persistence']}
            Channel Assignments:
                CH1: {validated_settings['scope']['ch1']}
                CH2: {validated_settings['scope']['ch2']}
                CH3: {validated_settings['scope']['ch3']}
                CH4: {validated_settings['scope']['ch4']}
                CH5: {validated_settings['scope']['ch5']}
                CH6: {validated_settings['scope']['ch6']}
            
        Load Settings:
            I Low: {validated_settings['load_settings']['i_low']} A
            I High: {validated_settings['load_settings']['i_high']} A
            Low Time: {validated_settings['load_settings']['low_time']} µs
            High Time: {validated_settings['load_settings']['high_time']} µs
            Rising SR: {validated_settings['load_settings']['rising_sr']} A/µs
            Falling SR: {validated_settings['load_settings']['falling_sr']} A/µs
            Load Level: {validated_settings['load_settings']['load_level']}
        Protection:
            Max Vin: {validated_settings['protection']['max_vin']} V
            Max Iin: {validated_settings['protection']['max_iin']} A
            Max Iout: {validated_settings['protection']['max_iout']} A
        """
        self.update_results(print_string)

    def capture_scope_image(self):
        # This is a placeholder. Replace with actual scope image capture later.
        # For now, we'll just create a blank image
        img = Image.new('RGB', (400, 300), color = (73, 109, 137))
        self.scope_image = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.scope_image)
        self.image_label.image = self.scope_image  # Keep a reference

    def lock_frame(self):
        self.start_button.config(state=tk.DISABLED)

    def unlock_frame(self):
        self.start_button.config(state=tk.NORMAL)