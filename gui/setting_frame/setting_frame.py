import tkinter as tk
from tkinter import ttk, messagebox
from config import *
from instrument_manager import InstrumentManager
from .EfficiencyTest import EfficiencyTestFrame
from .TestFrame import TestFrame
from .utils import validate_entry

class SettingFrame(tk.Frame):
    def __init__(self, parent, instrument_manager):
        super().__init__(parent, bd=4, relief=tk.RIDGE, bg='gray')
        self.parent = parent
        self.instrument_manager = instrument_manager
        self.is_locked = False
        self.current_test_frame = None
        self.create_widgets()
        self.set_default_values()

    def create_widgets(self):
        self.create_title()
        self.create_selection_frame()
        self.create_test_frame()
        self.create_button_frame()

    def create_title(self):
        title = tk.Label(self, text="Setting", font=("times new roman", 20, "bold"), bg='black', fg="white")
        title.pack(fill=tk.X, padx=5, pady=5)
        
    def create_selection_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=50, width=470, height=40)
        
        tk.Label(frame, text="IC", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)
        self.ic_combo = ttk.Combobox(frame, width=15, values=IC_OPTIONS)
        self.ic_combo.place(x=30, y=5)
        self.ic_combo.set('DEFAULT')
        self.ic_combo.bind("<<ComboboxSelected>>", self.on_ic_selected)

        tk.Label(frame, text="Test Type", font=FONT_BOLD, bg='white', fg="black").place(x=200, y=5)
        self.test_type_combo = ttk.Combobox(frame, width=15, values=TEST_TYPES)
        self.test_type_combo.place(x=280, y=5)
        self.test_type_combo.set('Efficiency')
        self.test_type_combo.bind("<<ComboboxSelected>>", self.on_test_type_selected)
        
    def on_ic_selected(self, event):
        selected_ic = self.ic_combo.get()
        self.set_default_values(selected_ic)
        
    def on_test_type_selected(self, event):
        self.create_test_frame()

    def create_test_frame(self):
        if self.current_test_frame:
            self.current_test_frame.destroy()

        test_type = self.test_type_combo.get()
        selected_ic = self.ic_combo.get()

        if test_type == 'Efficiency':
            self.current_test_frame = EfficiencyTestFrame(self, self.instrument_manager, selected_ic)
        # Add more elif statements here for future test types
        else:
            raise ValueError(f"Unknown test type: {test_type}")

        self.current_test_frame.place(x=25, y=100, width=470, height=920)
        self.set_default_values()

    def create_button_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='gray', borderwidth=0)
        frame.place(x=25, y=1030, width=450, height=60)

        self.reset_button = tk.Button(frame, text="reset", bg='white', fg="black", padx=20, pady=5,
                  font=BUTTON_FONT, command=self.reset_fields)
        self.reset_button.place(x=30, y=10)
        
        self.set_button = tk.Button(frame, text=" set ", bg='white', fg="black", padx=20, pady=5,
                  font=BUTTON_FONT, command=self.set_values)
        self.set_button.place(x=270, y=10)

    def set_default_values(self, ic='DEFAULT'):
        default_settings = IC_DEFAULT_SETTINGS.get(ic, DEFAULT_SETTINGS)
        if self.current_test_frame:
            self.current_test_frame.selected_ic = ic  # Update the selected_ic in the test frame
            self.current_test_frame.set_default_values(default_settings)

    def reset_fields(self):
        selected_ic = self.ic_combo.get()
        self.set_default_values(selected_ic)
        self.unlock_frame()
        self.parent.lock_testing_frame()

    def set_values(self):
        if not self.current_test_frame:
            messagebox.showerror("Error", "No test frame selected")
            return

        if self.current_test_frame.validate_values():
            values = self.current_test_frame.get_values()
            # Here you can do something with the values, like saving them or passing them to another part of your application
            messagebox.showinfo("Info", "Values set successfully!")
            self.lock_frame()
            self.parent.unlock_testing_frame()

    def lock_frame(self):
        self.is_locked = True
        for widget in self.winfo_children():
            if widget != self.reset_button and isinstance(widget, (tk.Entry, ttk.Combobox, tk.Button)):
                widget.config(state='disabled')
        if self.current_test_frame:
            for widget in self.current_test_frame.winfo_children():
                if isinstance(widget, (tk.Entry, ttk.Combobox, tk.Button)):
                    widget.config(state='disabled')

    def unlock_frame(self):
        self.is_locked = False
        for widget in self.winfo_children():
            if isinstance(widget, (tk.Entry, ttk.Combobox, tk.Button)):
                widget.config(state='normal')
        if self.current_test_frame:
            for widget in self.current_test_frame.winfo_children():
                if isinstance(widget, (tk.Entry, ttk.Combobox, tk.Button)):
                    widget.config(state='normal')

    def get_instrument_manager(self):
        return self.instrument_manager

    def update_instrument_info(self):
        # Update instrument information labels
        supply_info = self.instrument_manager.instruments.get('supply', 'Not detected')
        daq_info = self.instrument_manager.instruments.get('DAQ', 'Not detected')
        load_info = self.instrument_manager.instruments.get('load', 'Not detected')

        # Assuming you have labels for each instrument, update them here
        # For example:
        # self.supply_label.config(text=supply_info)
        # self.daq_label.config(text=daq_info)
        # self.load_label.config(text=load_info)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.instrument_manager.disconnect_all()
            self.parent.destroy()