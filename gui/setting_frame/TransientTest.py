from .TestFrame import TestFrame
import tkinter as tk
from tkinter import ttk, messagebox
from config import *
from .utils import validate_entry, validate_vin_entry

class TransientTestFrame(TestFrame):
    def __init__(self, parent, instrument_manager, selected_ic):
        print("Initializing TransientTestFrame...")
        super().__init__(parent, instrument_manager, selected_ic)
        self.setting_frame = parent
        self.scope_us_div_entries = []
        self.scope_persistence_vars = []
        self.scope_channels = []
        self.load_entries = []
        self.shunt_entries = []
        self.load_level_var = tk.StringVar()
        print("TransientTestFrame attributes initialized. Creating widgets...")
        self.create_widgets()
        print("TransientTestFrame widgets created.")

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
        tk.Label(frame, text=self.instrument_manager.instruments['supply'], font=FONT_NORMAL, bg='white', fg="black").place(x=100, y=5)

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
        tk.Label(frame, text=self.instrument_manager.instruments['o_scope'], font=FONT_NORMAL, bg='white', fg="black").place(x=100, y=5)

       
        

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
        tk.Label(frame, text=self.instrument_manager.instruments['load'], font=FONT_NORMAL, bg='white', fg="black").place(x=100, y=5)

        labels = [("I low", "Low time"), ("I high", "High time"), ("Raising SR", "Falling SR")]
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





    def create_transient_load_entries(self, parent):
        labels = ["Low Load (A):", "High Load (A):", "Rise Time (µs):", "Fall Time (µs):", "Frequency (Hz):"]
        self.load_entries = []
        
        for i, label in enumerate(labels):
            tk.Label(parent, text=label, font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=40 + i*30)
            entry = self.create_entry(parent, "", 40 + i*30, x=130, width=10)
            self.load_entries.append(entry)

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
        self.vcc_var.set(False)
        self.vcc.delete(0, tk.END)
        self.vcc.insert(0, "0")
        self.icc.delete(0, tk.END)
        self.icc.insert(0, "0")
        self.pw_ch_vcc.set("")
        self.toggle_vcc_frame()

        # Scope
        for i, combo in enumerate(self.scope_channels, 1):
            combo.set(settings['scope'][f'ch{i}'])

        # Load (You may need to adjust this based on your transient test requirements)
        load_params = ['low_load', 'high_load', 'rise_time', 'fall_time', 'frequency']
        for entry, param in zip(self.load_entries, load_params):
            entry.delete(0, tk.END)
            entry.insert(0, str(settings['load'].get(param, '')))

        # Current Shunt
        shunt_values = settings['current_shunt'].values()
        for entry, value in zip(self.shunt_entries, shunt_values):
            entry.delete(0, tk.END)
            entry.insert(0, str(value))
            
        for entry in self.scope_us_div_entries:
            entry.delete(0, tk.END)
            entry.insert(0, settings['scope'].get('default_us_div', '1'))
            
        for var in self.scope_persistence_vars:
            var.set(settings['scope'].get('default_persistence', False))
        self.load_level_var.set(settings['load'].get('default_load_level', 'L'))

    def get_values(self):
        def safe_float(value, field_name):
            try:
                return float(value) if value else 0
            except ValueError:
                raise ValueError(f"Invalid input for {field_name}")

        input_v = safe_float(self.vin.get(), "Input Voltage (Input_V)")
        input_i = safe_float(self.iin.get(), "Input Current (Input_I)")
        power_supply_channel = self.pw_ch_vin.get()
        
        scope_channels = [combo.get() for combo in self.scope_channels]
        
        # Access protection values from SettingFrame
        max_vin = safe_float(self.setting_frame.max_vin.get(), "Protective Maximum Input Voltage (MAX_Vin)")
        max_iin = safe_float(self.setting_frame.max_iin.get(), "Protective Maximum Input Current (MAX_Iin)")
        max_iout = safe_float(self.setting_frame.max_iout.get(), "Protective Maximum Output Current (MAX_Iout)")

        load_params = ['low_load', 'high_load', 'rise_time', 'fall_time', 'frequency']
        load_values = [safe_float(entry.get(), f"{param.replace('_', ' ').title()}") for entry, param in zip(self.load_entries, load_params)]

        input_shunt_max_voltage = safe_float(self.shunt_entries[0].get(), "Input Shunt Max Voltage")
        input_shunt_max_current = safe_float(self.shunt_entries[1].get(), "Input Shunt Max Current")
        output_shunt_max_voltage = safe_float(self.shunt_entries[2].get(), "Output Shunt Max Voltage")
        output_shunt_max_current = safe_float(self.shunt_entries[3].get(), "Output Shunt Max Current")

        values = {
            'selected_ic': self.selected_ic,
            'input_v': input_v,
            'input_i': input_i,
            'power_supply_channel': power_supply_channel,
            'scope_channels': scope_channels,       
            'scope_us_div': [entry.get() for entry in self.scope_us_div_entries],
            'scope_persistence': [var.get() for var in self.scope_persistence_vars],
            'load_level': self.load_level_var.get(),
            'max_vin': max_vin,
            'max_iin': max_iin,
            'max_iout': max_iout,
            'load': dict(zip(load_params, load_values)),
            'shunt_settings': [
                input_shunt_max_voltage,
                input_shunt_max_current,
                output_shunt_max_voltage,
                output_shunt_max_current
            ]
        }

        return values
    
    def validate_values(self, values):
        try:
            input_v = float(values['input_v'])
            input_i = float(values['input_i'])

            if input_v > MAX_INPUT_VOLTAGE or input_v < MIN_INPUT_VOLTAGE:
                raise ValueError(f"Input voltage (Input_V) range should be between {MIN_INPUT_VOLTAGE}V~{MAX_INPUT_VOLTAGE}V")
            
            if input_i > MAX_OUTPUT_CURRENT:
                raise ValueError(f"Input current (Input_I) should not exceed {MAX_OUTPUT_CURRENT}A")

            # Validate load settings
            low_load = float(values['load']['low_load'])
            high_load = float(values['load']['high_load'])
            rise_time = float(values['load']['rise_time'])
            fall_time = float(values['load']['fall_time'])
            frequency = float(values['load']['frequency'])

            if low_load >= high_load:
                raise ValueError("Low load should be less than high load")
            
            if rise_time <= 0 or fall_time <= 0 or frequency <= 0:
                raise ValueError("Rise time, fall time, and frequency should be greater than 0")

            # Validate protection settings
            max_vin = float(values['max_vin'])
            max_iin = float(values['max_iin'])
            max_iout = float(values['max_iout'])

            if max_vin < input_v:
                raise ValueError("Max input voltage protection should be greater than or equal to input voltage")
            
            if max_iin < input_i:
                raise ValueError("Max input current protection should be greater than or equal to input current")
            
            if max_iout < high_load:
                raise ValueError("Max output current protection should be greater than or equal to high load")

            # Validate shunt settings
            input_shunt_max_voltage, input_shunt_max_current, output_shunt_max_voltage, output_shunt_max_current = values['shunt_settings']

            if input_shunt_max_current < input_i:
                raise ValueError("Input shunt max current should be greater than or equal to input current")
            
            if output_shunt_max_current < high_load:
                raise ValueError("Output shunt max current should be greater than or equal to high load")

           # Validate scope channel assignments
            scope_channels = values['scope_channels']
            if len(set(scope_channels)) != len(scope_channels):
                raise ValueError("Scope channels must be unique")
            if len(scope_channels) != 6:
                raise ValueError("All 6 scope channels must be assigned")
            
            for us_div in values['scope_us_div']:
                if not us_div:
                    raise ValueError("All scope us/div fields must be filled")
                float(us_div)  # Check if it's a valid float
            
            if not values['load_level']:
                raise ValueError("Load level must be selected")
            
        except KeyError as e:
            messagebox.showwarning("Warning", f"Missing required field: {str(e)}")
        except ValueError as e:
            messagebox.showwarning("Warning", str(e))
        except Exception as e:
            messagebox.showwarning("Warning", f"An unexpected error occurred: {str(e)}")

        return False

    def update_protection_values(self):
        # This method can be called to update the protection values from the SettingFrame
        protection_values = self.setting_frame.get_protection_values()
        self.max_vin = protection_values['max_vin']
        self.max_iin = protection_values['max_iin']
        self.max_iout = protection_values['max_iout']

    def prepare_for_test(self):
        # This method can be called before starting the test to ensure all settings are up to date
        self.update_protection_values()
        # Add any other pre-test preparations here

    def get_test_parameters(self):
        # This method returns a dictionary of all parameters needed for the transient test
        values = self.get_values()
        test_params = {
            'input_voltage': values['input_v'],
            'input_current': values['input_i'],
            'power_supply_channel': values['power_supply_channel'],
            'scope_channels': values['scope_channels'],
            'load_settings': values['load'],
            'protection': {
                'max_vin': values['max_vin'],
                'max_iin': values['max_iin'],
                'max_iout': values['max_iout']
            },
            'shunt_settings': values['shunt_settings']
        }
        return test_params

    def lock_frame(self):
        # Disable all input fields when the test is running
        for widget in self.winfo_children():
            if isinstance(widget, (tk.Entry, ttk.Combobox)):
                widget.config(state='disabled')

    def unlock_frame(self):
        # Enable all input fields when the test is not running
        for widget in self.winfo_children():
            if isinstance(widget, (tk.Entry, ttk.Combobox)):
                widget.config(state='normal')

    def reset_to_defaults(self):
        # Reset all fields to their default values
        self.set_default_values(IC_DEFAULT_SETTINGS.get(self.selected_ic, DEFAULT_SETTINGS))
