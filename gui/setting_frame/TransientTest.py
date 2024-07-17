from .TestFrame import TestFrame
import tkinter as tk
from tkinter import ttk, messagebox
from config import *
from .utils import validate_entry, validate_vin_entry

class TransientTestFrame(TestFrame):
    def __init__(self, parent, instrument_manager, selected_ic):
        super().__init__(parent, instrument_manager, selected_ic)
        self.setting_frame = parent
        self.validated_values = None
        
        
    def create_widgets(self):
        print("Creating TransientTestFrame widgets...")
        tk.Label(self, text="Transient Test Settings", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        
        # Power Supply Frame
        self.create_power_supply_frame()
        
        # Oscilloscope and Scope Measurement Frames (side by side)
        self.create_scope_and_measurement_frames()
        
        # E Load Frame
        self.create_load_frame()
        

        
        print("All TransientTestFrame widgets created.")



    def create_power_supply_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=5, y=50, width=460, height=140)
        
        tk.Label(frame, text="Power Supply", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.get_instrument_model('supply'), font=FONT_NORMAL, bg='white', fg="black").place(x=110, y=5)

        tk.Label(frame, text="Vin(V)", font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=35)
        self.vin = self.create_entry(frame, "", 35, x=60, width=10)
        
        tk.Label(frame, text="Iin(A)", font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=65)
        self.iin = self.create_entry(frame, "", 65, x=60, width=10)
        
        tk.Label(frame, text="CH", font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=95)
        self.pw_ch_vin = ttk.Combobox(frame, width=5, values=POWER_SUPPLY_CHANNELS)
        self.pw_ch_vin.place(x=60, y=95)

        self.vcc_var = tk.BooleanVar()
        self.vcc_checkbox = tk.Checkbutton(frame, text="VCC", variable=self.vcc_var, 
                                           command=self.toggle_vcc_frame, bg='white')
        self.vcc_checkbox.place(x=140, y=95)

        self.vcc_frame = tk.Frame(frame, bg='white')
        self.vcc_frame.place(x=270, y=30, width=200, height=90)
        
        self.vcc = self.create_entry(self.vcc_frame, "Vcc(V)", 0)
        self.icc = self.create_entry(self.vcc_frame, "Icc(A)", 30)
        tk.Label(self.vcc_frame, text="CH", font=FONT_NORMAL, bg='white', fg="black").place(x=0, y=60)
        self.pw_ch_vcc = ttk.Combobox(self.vcc_frame, width=5, values=POWER_SUPPLY_CHANNELS)
        self.pw_ch_vcc.place(x=30, y=60)
        
    def create_scope_and_measurement_frames(self):
        scope_frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        scope_frame.place(x=5, y=200, width=460, height=220)
        
        measurement_frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        measurement_frame.place(x=5, y=430, width=460, height=120)
        
        self.create_scope_frame(scope_frame)
        self.create_scope_measurement_frame(measurement_frame)

    def create_scope_frame(self, frame):
        tk.Label(frame, text="Oscilloscope", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.get_instrument_model('o_scope'), font=FONT_NORMAL, bg='white', fg="black").place(x=110, y=5)

       
        

        self.scope_channels = []
        self.scope_us_div_entries = []
        self.scope_persistence_vars = []
        us_div_entry = self.create_entry(frame, "",  30, x=200, width=5)
        tk.Label(frame, text="us/div", font=FONT_NORMAL, bg='white', fg="black").place(x=255, y= 30)
        self.scope_us_div_entries.append(us_div_entry)
        tk.Label(frame, text="Persistence", font=FONT_NORMAL, bg='white', fg="black").place(x=320, y= 30)
        persistence_var = tk.BooleanVar()
        persistence_checkbox = tk.Checkbutton(frame, variable=persistence_var, bg='white')
        persistence_checkbox.place(x=410, y=30)
        self.scope_persistence_vars.append(persistence_var)

        
        for i in range(1, 7):
            tk.Label(frame, text=f"CH{i}", font=FONT_NORMAL, bg='white', fg="black").place(x=5,  y=25 + 30*(i-1))
            combo = ttk.Combobox(frame, width=20, values=Scope_OPTIONS)
            combo.place(x=40, y=25 + 30*(i-1))
            self.scope_channels.append(combo)


    def create_scope_measurement_frame(self, frame):
        tk.Label(frame, text="Scope Measurement", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)
        tk.Label(frame, text="Vout: Peak, valley", font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=30)
        tk.Label(frame, text="SW: Frequency", font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=55)
        tk.Label(frame, text="Iout: raising SR, falling SR", font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=80)


    def create_load_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=5, y=560, width=460, height=160)
        
        tk.Label(frame, text="E Load", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.get_instrument_model('load'), font=FONT_NORMAL, bg='white', fg="black").place(x=110, y=5)

        labels = [("I low(A)", "Low time(uS)"), ("I high(A)", "High time(uS)"), ("R SR(A/us)", "F SR(A/us)")]
        self.load_entries = []
        for i, (label1, label2) in enumerate(labels):
            tk.Label(frame, text=label1, font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=35 + i*30)
            entry1 = self.create_entry(frame, "", 35 + i*30, x=100, width=10)
            self.load_entries.append(entry1)
            
            tk.Label(frame, text=label2, font=FONT_NORMAL, bg='white', fg="black").place(x=220, y=35 + i*30)
            entry2 = self.create_entry(frame, "", 35 + i*30, x=320, width=10)
            self.load_entries.append(entry2)

        tk.Label(frame, text="Load Level:", font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=120)
        self.load_level_var = tk.StringVar()
        tk.Radiobutton(frame, text="L", variable=self.load_level_var, value="L", bg='white').place(x=100, y=120)
        tk.Radiobutton(frame, text="M", variable=self.load_level_var, value="M", bg='white').place(x=150, y=120)
        tk.Radiobutton(frame, text="H", variable=self.load_level_var, value="H", bg='white').place(x=200, y=120)





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
            # Set default values for VCC when selected
            default_settings = IC_DEFAULT_SETTINGS.get(self.selected_ic, DEFAULT_SETTINGS)
            self.vcc.delete(0, tk.END)
            self.vcc.insert(0, str(default_settings['power_supply']['vcc']))
            self.icc.delete(0, tk.END)
            self.icc.insert(0, str(default_settings['power_supply']['icc']))
            self.pw_ch_vcc.set(default_settings['power_supply']['vcc_channel'])
        else:
            self.vcc_frame.place_forget()
            # Reset VCC values when deselected
            self.vcc.delete(0, tk.END)
            self.vcc.insert(0, "0")
            self.icc.delete(0, tk.END)
            self.icc.insert(0, "0")
            self.pw_ch_vcc.set("")

    def set_default_values(self, settings):
        # Power Supply
        self.vin.delete(0, tk.END)
        self.vin.insert(0, str(settings['power_supply']['vin']))
        self.iin.delete(0, tk.END)
        self.iin.insert(0, str(settings['power_supply']['iin']))
        self.pw_ch_vin.set(settings['power_supply']['vin_channel'])
        
        # VCC
        self.vcc_var.set(settings['power_supply'].get('vcc_enabled', False))
        self.vcc.delete(0, tk.END)
        self.vcc.insert(0, str(settings['power_supply'].get('vcc', 0)))
        self.icc.delete(0, tk.END)
        self.icc.insert(0, str(settings['power_supply'].get('icc', 0)))
        self.pw_ch_vcc.set(settings['power_supply']['vcc_channel'])
        self.toggle_vcc_frame()

        # Scope
        for i, combo in enumerate(self.scope_channels, 1):
            combo.set(settings['scope'][f'ch{i}'])
        
        self.scope_us_div_entries[0].delete(0, tk.END)
        self.scope_us_div_entries[0].insert(0, str(settings['scope']['default_us_div']))
        
        self.scope_persistence_vars[0].set(settings['scope']['default_persistence'])

        # Load
        load_params = ['i_low', 'low_time', 'i_high', 'high_time', 'rising_sr', 'falling_sr']
        for entry, param in zip(self.load_entries, load_params):
            entry.delete(0, tk.END)
            entry.insert(0, str(settings['load'][param]))
        
        self.load_level_var.set(settings['load']['default_load_level'])

        # Current Shunt (if applicable)
        if 'current_shunt' in settings:
            shunt_values = settings['current_shunt'].values()
            for entry, value in zip(self.shunt_entries, shunt_values):
                entry.delete(0, tk.END)
                entry.insert(0, str(value))

    def get_values(self):
        def safe_float(value, field_name):
            try:
                return float(value) if value else 0
            except ValueError:
                raise ValueError(f"Invalid input for {field_name}")

        values = {
            'selected_ic': self.selected_ic,
            'power_supply': {
                'vin': safe_float(self.vin.get(), "Input Voltage (Vin)"),
                'iin': safe_float(self.iin.get(), "Input Current (Iin)"),
                'vin_channel': self.pw_ch_vin.get(),
                'vcc_enabled': self.vcc_var.get(),
                'vcc': safe_float(self.vcc.get(), "VCC Voltage") if self.vcc_var.get() else 0,
                'icc': safe_float(self.icc.get(), "VCC Current") if self.vcc_var.get() else 0,
                'vcc_channel': self.pw_ch_vcc.get() if self.vcc_var.get() else '2'
            },
            'scope': {
                f'ch{i+1}': combo.get() for i, combo in enumerate(self.scope_channels)
            },
            'scope_us_div': safe_float(self.scope_us_div_entries[0].get(), "Scope us/div"),
            'scope_persistence': self.scope_persistence_vars[0].get(),
            'load_settings': {
                'i_low': safe_float(self.load_entries[0].get(), "I low"),
                'low_time': safe_float(self.load_entries[1].get(), "Low time"),
                'i_high': safe_float(self.load_entries[2].get(), "I high"),
                'high_time': safe_float(self.load_entries[3].get(), "High time"),
                'rising_sr': safe_float(self.load_entries[4].get(), "Rising Slew Rate"),
                'falling_sr': safe_float(self.load_entries[5].get(), "Falling Slew Rate"),
                'load_level': self.load_level_var.get()
            },
            'protection': self.setting_frame.get_protection_values()
        }

        return values

    def validate_values(self, values):
        try:
            # Validate Power Supply settings
            if values['power_supply']['vin'] > MAX_INPUT_VOLTAGE or values['power_supply']['vin'] < MIN_INPUT_VOLTAGE:
                raise ValueError(f"Input voltage (Vin) range should be between {MIN_INPUT_VOLTAGE}V~{MAX_INPUT_VOLTAGE}V")
            
            if values['power_supply']['iin'] > MAX_OUTPUT_CURRENT:
                raise ValueError(f"Input current (Iin) should not exceed {MAX_OUTPUT_CURRENT}A")

            if values['power_supply']['vcc_enabled']:
                if values['power_supply']['vcc'] > MAX_INPUT_VOLTAGE or values['power_supply']['vcc'] < 0:
                    raise ValueError(f"VCC voltage range should be between 0V~{MAX_INPUT_VOLTAGE}V")
                if values['power_supply']['icc'] > MAX_OUTPUT_CURRENT or values['power_supply']['icc'] < 0:
                    raise ValueError(f"VCC current should be between 0A~{MAX_OUTPUT_CURRENT}A")

            # Validate Scope settings
            scope_channels = list(values['scope'].values())
            if len(set(scope_channels)) != len(scope_channels):
                raise ValueError("Scope channels must be unique")
            if len(scope_channels) != 6:
                raise ValueError("All 6 scope channels must be assigned")

            if values['scope_us_div'] <= 0:
                raise ValueError("Scope us/div must be greater than 0")

            # Validate Load settings
            load = values['load_settings']
            if load['i_low'] >= load['i_high']:
                raise ValueError("Low load current must be less than high load current")
            if load['low_time'] <= 0 or load['high_time'] <= 0:
                raise ValueError("Low time and high time must be greater than 0")
            if load['rising_sr'] <= 0 or load['falling_sr'] <= 0:
                raise ValueError("Rising and falling slew rates must be greater than 0")
            if not load['load_level']:
                raise ValueError("Load level must be selected")

            # Validate protection settings
            protection = values['protection']
            if protection['max_vin'] < values['power_supply']['vin']:
                raise ValueError("Max input voltage protection must be greater than or equal to input voltage")
            if protection['max_iin'] < values['power_supply']['iin']:
                raise ValueError("Max input current protection must be greater than or equal to input current")
            if protection['max_iout'] < load['i_high']:
                raise ValueError("Max output current protection must be greater than or equal to high load current")

            return True

        except ValueError as e:
            messagebox.showwarning("Validation Error", str(e))
            return False
        except Exception as e:
            messagebox.showwarning("Error", f"An unexpected error occurred: {str(e)}")
            return False