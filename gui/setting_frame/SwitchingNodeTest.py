from .TestFrame import TestFrame
import tkinter as tk
from tkinter import ttk, messagebox
from config import *
from .utils import *

class SwitchingNodeTestFrame(TestFrame):
    def __init__(self, parent, instrument_manager, selected_ic):
        super().__init__(parent, instrument_manager, selected_ic)
        self.setting_frame = parent
        self.validated_values = None

    def create_widgets(self):
        print("Creating SwitchingNodeTestFrame widgets...")
        tk.Label(self, text="Switching Node Test Settings", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        self.create_power_supply_frame()
        self.create_scope_frame()
        self.create_load_frame()
        print("All SwitchingNodeTestFrame widgets created.")

    def create_power_supply_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=5, y=30, width=450, height=150)
        
        tk.Label(frame, text="Power Supply", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.get_instrument_model('supply'), font=FONT_NORMAL, bg='white', fg="black").place(x=110, y=5)

        self.vin_frame = tk.Frame(frame, bg='white')
        self.vin_frame.place(x=5, y=35, width=230, height=100)
        
        self.vin = self.create_entry(self.vin_frame, "Vin(V)", 0, width=10, validate_command=validate_vin_entry)
        self.iin = self.create_entry(self.vin_frame, "Iin(A)", 40)
        
        tk.Label(self.vin_frame, text="CH", font=FONT_NORMAL, bg='white', fg="black").place(x=0, y=70)
        self.pw_ch_vin = ttk.Combobox(self.vin_frame, width=5, values=POWER_SUPPLY_CHANNELS)
        self.pw_ch_vin.place(x=30, y=70)

        self.vcc_var = tk.BooleanVar()
        self.vcc_checkbox = tk.Checkbutton(frame, text="VCC", variable=self.vcc_var, 
                                           command=self.toggle_vcc_frame, bg='white')
        self.vcc_checkbox.place(x=190, y=120)

        self.vcc_frame = tk.Frame(frame, bg='white')
        self.vcc_frame.place(x=270, y=35, width=200, height=100)
        
        self.vcc = self.create_entry(self.vcc_frame, "Vcc(V)", 0)
        self.icc = self.create_entry(self.vcc_frame, "Icc(A)", 30)
        tk.Label(self.vcc_frame, text="CH", font=FONT_NORMAL, bg='white', fg="black").place(x=0, y=60)
        self.pw_ch_vcc = ttk.Combobox(self.vcc_frame, width=5, values=POWER_SUPPLY_CHANNELS)
        self.pw_ch_vcc.place(x=30, y=60)

    def create_scope_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=5, y=190, width=450, height=220)
        
        tk.Label(frame, text="Oscilloscope", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.get_instrument_model('o_scope'), font=FONT_NORMAL, bg='white', fg="black").place(x=110, y=5)

        self.scope_channels = []
        for i in range(1, 7):
            tk.Label(frame, text=f"CH{i}", font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=30 + 25*(i-1))
            combo = ttk.Combobox(frame, width=20, values=Scope_OPTIONS)
            combo.place(x=55, y=30 + 25*(i-1))
            self.scope_channels.append(combo)

        tk.Label(frame, text="us/div", font=FONT_NORMAL, bg='white', fg="black").place(x=240, y=30)
        self.scope_us_div = self.create_entry(frame, "", 30, x=290, width=8)

        self.persistence_var = tk.BooleanVar()
        tk.Checkbutton(frame, text="Persistence", variable=self.persistence_var, bg='white').place(x=240, y=60)

    def create_load_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=5, y=420, width=450, height=100)
        
        tk.Label(frame, text="E Load", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.get_instrument_model('load'), font=FONT_NORMAL, bg='white', fg="black").place(x=110, y=5)

        self.load_values = self.create_entry(frame, "Load Values(A)", 40, width=30,validate_command=validate_eload_entry)


    def create_entry(self, parent, label, y, x=None, width=8, validate_command=None):
        if label:
            tk.Label(parent, text=label, font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=y)
        vcmd = (self.register(validate_command or validate_entry), '%P')
        entry = tk.Entry(parent, validate="key", validatecommand=vcmd,
                         font=("times new roman", 12), bd=2, relief=tk.GROOVE, width=width)
        if x is None:
            x = len(label)*8 + 55
        entry.place(x=x, y=y)
        return entry

    def toggle_vcc_frame(self):
        if self.vcc_var.get():
            self.vcc_frame.place(x=240, y=35, width=200, height=100)
            default_settings = IC_DEFAULT_SETTINGS.get(self.selected_ic, DEFAULT_SETTINGS)['Switching Node']
            self.vcc.delete(0, tk.END)
            self.vcc.insert(0, str(default_settings['power_supply']['vcc']))
            self.icc.delete(0, tk.END)
            self.icc.insert(0, str(default_settings['power_supply']['icc']))
            self.pw_ch_vcc.set(default_settings['power_supply']['vcc_channel'])
        else:
            self.vcc_frame.place_forget()
            self.vcc.delete(0, tk.END)
            self.vcc.insert(0, "0")
            self.icc.delete(0, tk.END)
            self.icc.insert(0, "0")
            self.pw_ch_vcc.set("")

    def set_default_values(self, settings):
        # Power Supply
        self.vin.delete(0, tk.END)
        self.vin.insert(0, ", ".join(map(str, settings['power_supply']['vin'])))
        self.iin.delete(0, tk.END)
        self.iin.insert(0, str(settings['power_supply']['iin']))
        self.pw_ch_vin.set(settings['power_supply']['vin_channel'])
        
        # VCC
        self.vcc_var.set(False)
        self.vcc.delete(0, tk.END)
        self.vcc.insert(0, str(settings['power_supply']['vcc']))
        self.icc.delete(0, tk.END)
        self.icc.insert(0, str(settings['power_supply']['icc']))
        self.pw_ch_vcc.set(settings['power_supply']['vcc_channel'])
        self.toggle_vcc_frame()

        # Scope
        for i, combo in enumerate(self.scope_channels, 1):
            combo.set(settings['scope'][f'ch{i}'])
        self.scope_us_div.delete(0, tk.END)
        self.scope_us_div.insert(0, str(settings['scope']['default_us_div']))
        self.persistence_var.set(settings['scope']['default_persistence'])

        # Load
        self.load_values.delete(0, tk.END)
        self.load_values.insert(0, ", ".join(map(str, settings['load']['load_values'])))


    def get_values(self):
        try:
            values = {
                'selected_ic': self.selected_ic,
                'power_supply': {
                    'vin': safe_float_list(self.vin.get(), "Input Voltage (Vin)"),
                    'iin': safe_float(self.iin.get(), "Input Current (Iin)"),
                    'vin_channel': self.pw_ch_vin.get(),
                    'vcc_enabled': self.vcc_var.get(),
                    'vcc': safe_float(self.vcc.get(), "VCC Voltage") if self.vcc_var.get() else 0,
                    'icc': safe_float(self.icc.get(), "VCC Current") if self.vcc_var.get() else 0,
                    'vcc_channel': self.pw_ch_vcc.get() if self.vcc_var.get() else ' 2'
                },
                'scope': {
                    f'ch{i+1}': combo.get() for i, combo in enumerate(self.scope_channels)
                },
                'scope_us_div': safe_float(self.scope_us_div.get(), "Scope us/div"),
                'scope_persistence': self.persistence_var.get(),
                'load': {
                    'load_values': safe_float_list(self.load_values.get(), "Load Values"),

                },
                'protection': self.setting_frame.get_protection_values()
            }

            return values

        except ValueError as e:
            messagebox.showwarning("Validation Error", str(e))
            return None


    def validate_values(self, values):
        try:
            if values['scope_us_div'] <= 0:
                raise ValueError("Scope us/div must be greater than 0")

            # Validate Power Supply settings
            vin_values = values['power_supply']['vin']
            if any(vin > MAX_INPUT_VOLTAGE or vin < MIN_INPUT_VOLTAGE for vin in vin_values):
                raise ValueError(f"Input voltage (Vin) range should be between {MIN_INPUT_VOLTAGE}V~{MAX_INPUT_VOLTAGE}V")

            if values['power_supply']['iin'] > MAX_OUTPUT_CURRENT:
                raise ValueError(f"Input current (Iin) should not exceed {MAX_OUTPUT_CURRENT}A")

            # Validate Load settings
            load_values = values['load']['load_values']
            if len(load_values) < 2:
                raise ValueError("At least two load values must be provided")
            if any(value < 0 or value > MAX_OUTPUT_CURRENT for value in load_values):
                raise ValueError(f"Load values must be between 0A and {MAX_OUTPUT_CURRENT}A")
            if values['load']['load_delay'] <= 0:
                raise ValueError("Load delay must be greater than 0")

            # Validate protection settings
            protection = values['protection']
            if protection['max_vin'] < max(vin_values):
                raise ValueError("Max input voltage protection must be greater than or equal to the highest input voltage")
            if protection['max_iin'] < values['power_supply']['iin']:
                raise ValueError("Max input current protection must be greater than or equal to input current")
            if protection['max_iout'] < max(load_values):
                raise ValueError("Max output current protection must be greater than or equal to the highest load value")

            return True

        except ValueError as e:
            messagebox.showwarning("Validation Error", str(e))
            return False
        except Exception as e:
            messagebox.showwarning("Error", f"An unexpected error occurred: {str(e)}")
            return False