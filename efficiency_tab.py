import tkinter as tk
from tkinter import ttk, messagebox
from config import *
from power_supply import power_supplies
from measure_eff_Tek import eff
import threading
from io import BytesIO
from PIL import Image, ImageTk
import pandas as pd

class EfficiencyTab(tk.Frame):
    def __init__(self, parent, instrument_manager, setting_frame):
        super().__init__(parent)
        self.instrument_manager = instrument_manager
        self.setting_frame = setting_frame
        self.test_running = False
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for controls
        control_frame = tk.Frame(self, bd=2, relief=tk.RIDGE)
        control_frame.pack(pady=10, padx=10, fill=tk.X)

        # Start button
        self.start_button = tk.Button(control_frame, text="Start Efficiency Test", command=self.start_efficiency_test)
        self.start_button.pack(side=tk.LEFT, padx=5)

        # Stop button (initially disabled)
        self.stop_button = tk.Button(control_frame, text="Stop Test", command=self.stop_efficiency_test, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(control_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        # Create a paned window for results and graph
        paned_window = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned_window.pack(expand=True, fill=tk.BOTH, pady=10, padx=10)

        # Results text area
        self.results_text = tk.Text(paned_window, height=20, width=40)
        paned_window.add(self.results_text)

        # Graph area
        self.graph_frame = tk.Frame(paned_window, bg='white')
        self.graph_label = tk.Label(self.graph_frame, bg='white')
        self.graph_label.pack(expand=True, fill=tk.BOTH)
        paned_window.add(self.graph_frame)

    def start_efficiency_test(self):
        if self.test_running:
            messagebox.showwarning("Test in Progress", "A test is already running.")
            return

        # Get values from setting frame
        try:
            settings = self.setting_frame.get_all_values()
            if not self.setting_frame.validate_values(settings):
                return
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
            return

        # Disable start button and enable stop button
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Clear previous results
        self.results_text.delete(1.0, tk.END)
        self.graph_label.config(image='')

        # Run the efficiency test in a separate thread
        self.test_running = True
        threading.Thread(target=self.run_efficiency_test, args=(settings,), daemon=True).start()

    def run_efficiency_test(self, settings):
        try:
            excel_buffer = eff(settings, self.instrument_manager, 
                               progress_callback=self.update_progress,
                               result_callback=self.update_results,
                               graph_callback=self.display_graph)
            self.display_excel(excel_buffer)
        except Exception as e:
            self.update_results(f"Error during test: {str(e)}")
        finally:
            self.test_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def stop_efficiency_test(self):
        if self.test_running:
            self.test_running = False
            self.update_results("Test stopped by user.")
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.progress_var.set(0)

    def update_progress(self, value):
        self.progress_var.set(value)
        self.update_idletasks()

    def update_results(self, message):
        self.results_text.insert(tk.END, message + "\n")
        self.results_text.see(tk.END)
        self.update_idletasks()

    def display_graph(self, plot_buffer):
        # Convert the plot buffer to a Tkinter-compatible image
        image = Image.open(plot_buffer)
        photo = ImageTk.PhotoImage(image)
        
        # Update the graph label with the new image
        self.graph_label.config(image=photo)
        self.graph_label.image = photo  # keep a reference!

    def display_excel(self, excel_buffer):
        # Save the Excel file
        with open("efficiency_results.xlsx", "wb") as f:
            f.write(excel_buffer.getvalue())
        self.update_results("Excel file saved as 'efficiency_results.xlsx'")

        # Display a summary of the results
        df = pd.read_excel(excel_buffer)
        summary = df.groupby('input_voltage_setpoint').agg({
            'efficiency': ['min', 'max', 'mean'],
            'v_output_voltage': ['min', 'max', 'mean'],
            'i_output_current': ['min', 'max']
        }).reset_index()

        summary_text = "Summary of Results:\n\n"
        for _, row in summary.iterrows():
            summary_text += f"Input Voltage: {row['input_voltage_setpoint']:.2f}V\n"
            summary_text += f"  Efficiency: {row['efficiency']['min']:.2f}% - {row['efficiency']['max']:.2f}% (Avg: {row['efficiency']['mean']:.2f}%)\n"
            summary_text += f"  Output Voltage: {row['v_output_voltage']['min']:.3f}V - {row['v_output_voltage']['max']:.3f}V (Avg: {row['v_output_voltage']['mean']:.3f}V)\n"
            summary_text += f"  Output Current: {row['i_output_current']['min']:.3f}A - {row['i_output_current']['max']:.3f}A\n\n"

        self.update_results(summary_text)