import tkinter as tk
from tkinter import ttk, messagebox
import pyvisa as visa
from typing import List, Dict
from config import *

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

class SettingFrame(tk.Frame):
    def __init__(self, parent, instrument_manager):
        super().__init__(parent, bd=4, relief=tk.RIDGE, bg='gray')
        self.instrument_manager = instrument_manager
        self.create_widgets()

    def create_widgets(self):
        self.create_title()
        self.create_power_supply_frame()
        self.create_daq_frame()
        self.create_load_frame()
        self.create_protection_frame()
        self.create_button_frame()

    def create_title(self):
        title = tk.Label(self, text="Setting", font=FONT_TITLE, bg='black', fg="white")
        title.place(relx=0.5, y=40, anchor="center")

    def create_power_supply_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=80, width=450, height=200)
        
        tk.Label(frame, text="Power_Supply", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.instruments['supply'], font=FONT_BOLD, bg='white', fg="black").place(x=110, y=5)

        self.vin = self.create_entry(frame, "Vin(V)", 55)
        self.iin = self.create_entry(frame, "Iin(A)", 105)
        
        tk.Label(frame, text="CH", font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=155)
        self.pw_ch = ttk.Combobox(frame, width=10, values=POWER_SUPPLY_CHANNELS)
        self.pw_ch.place(x=self.iin.winfo_width() + 55, y=155)

    def create_daq_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=300, width=450, height=230)
        
        tk.Label(frame, text="DAQ", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.instruments['DAQ'], font=FONT_BOLD, bg='white', fg="black").place(x=110, y=5)

        self.daq_channels = []
        for i in range(1, 7):
            label = tk.Label(frame, text=f"CH{i}", font=FONT_NORMAL, bg='white', fg="black")
            label.place(x=5, y=35 + 30*(i-1))
            combo = ttk.Combobox(frame, width=25, values=DAQ_OPTIONS)
            combo.place(x=55, y=35 + 30*(i-1))
            self.daq_channels.append(combo)

    def create_load_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=550, width=450, height=200)
        
        tk.Label(frame, text="E Load", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.instruments['load'], font=FONT_BOLD, bg='white', fg="black").place(x=110, y=5)

        tk.Label(frame, text="Low Load", font=FONT_BOLD, bg='white', fg="black").place(x=90, y=30)
        tk.Label(frame, text="High Load", font=FONT_BOLD, bg='white', fg="black").place(x=270, y=30)

        self.low_load_entries = self.create_load_entries(frame, 90)
        self.high_load_entries = self.create_load_entries(frame, 270)

    def create_load_entries(self, parent, x):
        entries = []
        for i, label in enumerate(["Start :", "Step :", "Stop :"]):
            tk.Label(parent, text=label, font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=60 + i*40)
            entry = tk.Entry(parent, validate="key", validatecommand=(self.register(self.validate_entry), "%P"),
                             font=FONT_BOLD, bd=5, relief=tk.GROOVE, width=10)
            entry.place(x=x, y=60 + i*40)
            entries.append(entry)
        return entries

    def create_protection_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=770, width=450, height=200)
        
        tk.Label(frame, text="Protection", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)

        self.max_vin = self.create_entry(frame, "Max Vin(V)", 55)
        self.max_iin = self.create_entry(frame, "Max Iin(A)", 105)
        self.max_iout = self.create_entry(frame, "Max Iout(A)", 155)

    def create_button_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='gray', borderwidth=0)
        frame.place(x=25, y=990, width=450, height=100)

        tk.Button(frame, text="reset", bg='white', fg="black", padx=20, pady=20,
                  font=BUTTON_FONT, command=self.reset_fields).place(x=30, y=15)
        
        tk.Button(frame, text=" set ", bg='white', fg="black", padx=20, pady=20,
                  font=BUTTON_FONT, command=self.set_values).place(x=270, y=15)

    def create_entry(self, parent, label, y):
        tk.Label(parent, text=label, font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=y)
        entry = tk.Entry(parent, validate="key", validatecommand=(self.register(self.validate_entry), "%P"),
                         font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        entry.place(x=len(label)*8 + 55, y=y)
        return entry

    @staticmethod
    def validate_entry(P):
        return P == "" or P == "." or (P.count('.') <= 1 and P.replace('.', '').isdigit())

    def reset_fields(self):
        for widget in self.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)
            elif isinstance(widget, ttk.Combobox):
                widget.set('')

    def set_values(self):
        try:
            values = self.get_all_values()
            if self.validate_values(values):
                messagebox.showinfo("Info", "Successfully set!")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        
    def get_all_values(self):
        def safe_float(value, field_name):
            try:
                return float(value) if value else 0
            except ValueError:
                raise ValueError(f"Invalid input for {field_name}")

        return {
            'input_v': safe_float(self.vin.get(), "Vin"),
            'input_i': safe_float(self.iin.get(), "Iin"),
            'max_vin': safe_float(self.max_vin.get(), "Max Vin"),
            'max_iin': safe_float(self.max_iin.get(), "Max Iin"),
            'max_iout': safe_float(self.max_iout.get(), "Max Iout"),
            'low_load': [safe_float(entry.get(), f"Low Load {i}") for i, entry in enumerate(self.low_load_entries, 1)],
            'high_load': [safe_float(entry.get(), f"High Load {i}") for i, entry in enumerate(self.high_load_entries, 1)]
        }

    def validate_values(self, values):
        if values['input_v'] > values['max_vin']:
            messagebox.showwarning("Warning", "Protective maximum input voltage (MAX_Vin) must be at least the Input voltage (Input_V)")
        elif values['input_i'] > values['max_iin']:
            messagebox.showwarning("Warning", "Protective maximum input current (MAX_Iin) must be at least the Input current (Input_I)")
        elif values['input_v'] > MAX_INPUT_VOLTAGE or values['input_v'] < MIN_INPUT_VOLTAGE:
            messagebox.showwarning("Warning", f"Input voltage (Input_V) range should be between {MIN_INPUT_VOLTAGE}V~{MAX_INPUT_VOLTAGE}V")
        elif values['high_load'][0] < values['low_load'][2]:
            messagebox.showwarning("Warning", "High Load Start Current should not be lower than the Low Load Stop")
        elif any(load > MAX_OUTPUT_CURRENT for load in [values['low_load'][2], values['high_load'][2], values['max_iout']]):
            messagebox.showwarning("Warning", f"Output current should < {MAX_OUTPUT_CURRENT}A")
        elif values['low_load'][1] > (values['low_load'][2] - values['low_load'][0]):
            messagebox.showwarning("Warning", "Invalid low load step")
        elif values['high_load'][1] > (values['high_load'][2] - values['high_load'][0]):
            messagebox.showwarning("Warning", "Invalid high load step")
        else:
            return True
        return False

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.instrument_manager = InstrumentManager()
        self.instrument_manager.find_devices()
        self.configure_window()
        self.create_widgets()

    def configure_window(self):
        self.parent.title("PoL Automation V1.0.0")
        self.parent.geometry(WINDOW_SIZE)
        self.parent.resizable(False, False)

    def create_widgets(self):
        self.setting_frame = SettingFrame(self, self.instrument_manager)
        self.setting_frame.place(x=20, y=20, width=500, height=1100)

        self.test_frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='gray')
        self.test_frame.place(x=550, y=20, width=1400, height=1100)

def main():
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()