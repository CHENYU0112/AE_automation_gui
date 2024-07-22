from .TestFrame import TestFrame
import tkinter as tk
from tkinter import ttk, messagebox
from config import *
from .utils import *
class EfficiencyTestFrame(TestFrame):
    def __init__(self, parent, instrument_manager, selected_ic):
        super().__init__(parent, instrument_manager, selected_ic)
        self.setting_frame = parent
        self.validated_values = None

    def create_widgets(self):
        print("Creating EfficiencyTestFrame widgets...")
        tk.Label(self, text="Efficiency Test Settings", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        self.create_power_supply_frame()
        self.create_daq_frame()
        self.create_load_frame()
        self.create_current_shunt_frame()
        print("All EfficiencyTestFrame widgets created.")
    def create_power_supply_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=5, y=30, width=450, height=150)
        
        tk.Label(frame, text="Power_Supply", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)
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

    def create_daq_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=5, y=190, width=450, height=220)
        
        tk.Label(frame, text="DAQ", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.get_instrument_model('DAQ'), font=FONT_NORMAL, bg='white', fg="black").place(x=110, y=5)

        self.daq_channels = []
        for i in range(1, 7):
            label = tk.Label(frame, text=f"CH{i}", font=FONT_NORMAL, bg='white', fg="black")
            label.place(x=5, y=30 + 25*(i-1))
            combo = ttk.Combobox(frame, width=20, values=DAQ_OPTIONS)
            combo.place(x=55, y=30 + 25*(i-1))
            self.daq_channels.append(combo)

    def create_load_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=5, y=420, width=450, height=200)
        
        tk.Label(frame, text="E Load", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.get_instrument_model('load'), font=FONT_NORMAL, bg='white', fg="black").place(x=110, y=5)
        tk.Label(frame, text="Low Load", font=FONT_BOLD, bg='white', fg="black").place(x=90, y=30)
        tk.Label(frame, text="High Load", font=FONT_BOLD, bg='white', fg="black").place(x=270, y=30)

        self.low_load_entries, self.low_load_vars = self.create_load_entries(frame, 90, is_low_load=True)
        self.high_load_entries, self.high_load_vars = self.create_load_entries(frame, 270, is_low_load=False)

        self.low_load_stop_var = self.low_load_vars[2]
        self.high_load_start_var = self.high_load_vars[0]
        
        self.low_load_stop_var.trace_add('write', self.update_high_load_start)
        self.high_load_start_var.trace_add('write', self.update_low_load_stop)

    def create_current_shunt_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=5, y=630, width=450, height=130)
        
        tk.Label(frame, text="Current Shunt ", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)

        labels = ["Max Vin(V)", "Max Iin(A)", "Max Vout(V)", "Max Iout(A)"]
        self.shunt_entries = []

        for i, label in enumerate(labels):
            row = i // 2
            col = i % 2
            tk.Label(frame, text=label, font=FONT_NORMAL, bg='white', fg="black").place(x=5 + col*225, y=30 + row*30)
            entry = self.create_entry(frame, "", 30 + row*30, x=130 + col*225, width=8)
            self.shunt_entries.append(entry)

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

    

    def create_load_entries(self, parent, x, is_low_load):
        entries = []
        vars = []
        labels = ["Start :", "Step :", "Stop :", "Delay(s):"]
        for i, label in enumerate(labels):
            tk.Label(parent, text=label, font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=55 + i*25)
            var = tk.StringVar()
            entry = tk.Entry(parent, textvariable=var, validate="key", 
                             validatecommand=(self.register(validate_entry), "%P"),
                             font=("times new roman", 12), bd=2, relief=tk.GROOVE, width=8)
            entry.place(x=x, y=55 + i*25)
            entries.append(entry)
            vars.append(var)
        return entries, vars

    def update_high_load_start(self, *args):
        if self.low_load_stop_var.get() != self.high_load_start_var.get():
            self.high_load_start_var.set(self.low_load_stop_var.get())

    def update_low_load_stop(self, *args):
        if self.high_load_start_var.get() != self.low_load_stop_var.get():
            self.low_load_stop_var.set(self.high_load_start_var.get())

    
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
        self.vcc.insert(0, str(settings['power_supply']['vcc']))
        self.icc.delete(0, tk.END)
        self.icc.insert(0, str(settings['power_supply']['icc']))
        self.pw_ch_vcc.set(settings['power_supply']['vcc_channel'])
        self.toggle_vcc_frame()

        # DAQ
        for i, combo in enumerate(self.daq_channels, 1):
            combo.set(settings['daq'][f'ch{i}'])

        # Load
        load_params = ['start', 'step', 'stop', 'delay']
        for i, entry in enumerate(self.low_load_entries):
            key = load_params[i]
            value = settings['load']['low_load'].get(key, 1)
            entry.delete(0, tk.END)
            entry.insert(0, str(value))
        for i, entry in enumerate(self.high_load_entries):
            key = load_params[i]
            value = settings['load']['high_load'].get(key, 1)
            entry.delete(0, tk.END)
            entry.insert(0, str(value))

        # Current Shunt
        shunt_values = settings['current_shunt'].values()
        for entry, value in zip(self.shunt_entries, shunt_values):
            entry.delete(0, tk.END)
            entry.insert(0, str(value))

    def get_values(self):
        try:

            # Collect and validate values
            input_v = safe_float_list(self.vin.get(), "Input Voltage (Input_V)")
            input_i = safe_float(self.iin.get(), "Input Current (Input_I)")
            power_supply_channel = self.pw_ch_vin.get()
            
            daq_channels = [combo.get() for combo in self.daq_channels]
            
            max_vin = safe_float(self.setting_frame.max_vin.get(), "Protective Maximum Input Voltage (MAX_Vin)")
            max_iin = safe_float(self.setting_frame.max_iin.get(), "Protective Maximum Input Current (MAX_Iin)")
            max_iout = safe_float(self.setting_frame.max_iout.get(), "Protective Maximum Output Current (MAX_Iout)")

            load_params = ['start', 'step', 'stop', 'delay']
            low_load_values = [safe_float(entry.get(), f"Low Load {param.capitalize()}") for entry, param in zip(self.low_load_entries, load_params)]
            high_load_values = [safe_float(entry.get(), f"High Load {param.capitalize()}") for entry, param in zip(self.high_load_entries, load_params)]

            shunt_settings = [safe_float(entry.get(), label) for entry, label in zip(self.shunt_entries, 
                ["Input Shunt Max Voltage", "Input Shunt Max Current", "Output Shunt Max Voltage", "Output Shunt Max Current"])]

            # Create channel assignments
            channel_mapping = {
                'input V': '101', 'input I': '102', 'output V': '103',
                'output I': '104', 'Vcc': '105', 'LDO': '106'
            }
            channel_assignments = {
                f"{channel.lower().replace(' ', '_')}_ch": str(100 + i)
                for i, channel in enumerate(daq_channels, start=1)
                if channel in channel_mapping
            }

            # Ensure all required channels are assigned
            required_channels = ['input_v_ch', 'input_i_ch', 'output_v_ch', 'output_i_ch', 'vcc_ch', 'ldo_ch']
            if not all(channel in channel_assignments for channel in required_channels):
                raise ValueError("Not all required channels are assigned")

            # Prepare the final validated values
            eff_params = {
                'input_shunt_max_voltage': shunt_settings[0],
                'input_shunt_max_current': shunt_settings[1],
                'output_shunt_max_voltage': shunt_settings[2],
                'output_shunt_max_current': shunt_settings[3],
                'Max_input_voltage': max_vin,
                'Max_input_current': max_iin,
                'Max_load_current': max_iout,
                'Input_V': input_v,
                'Input_I': input_i,
                'power_supply_channel': power_supply_channel,
                'Low_load_start': low_load_values[0],
                'Low_load_step': low_load_values[1],
                'Low_load_stop': low_load_values[2],
                'High_load_start': high_load_values[0],
                'High_load_stop': high_load_values[2],
                'High_load_step': high_load_values[1],
                'low_load_timing': low_load_values[3],
                'high_load_timing': high_load_values[3],
                'FRE': 1  # Set FRE to 1 as it's not in the original settings
            }

            # Update eff_params with the channel assignments
            eff_params.update(channel_assignments)

            # Validate data types
            for key, value in eff_params.items():
                if key == 'FRE':
                    if not isinstance(value, int):
                        raise ValueError(f"{key} must be an integer")

            return eff_params

        except ValueError as e:
            messagebox.showwarning("Validation Error", str(e))
            return None
        except Exception as e:
            messagebox.showwarning("Error", f"An unexpected error occurred: {str(e)}")
            return None

    
    def validate_values(self, values):
        try:
            # Validate Input Voltage
            input_v_list = values['Input_V']
            for i, input_v in enumerate(input_v_list):
                if input_v > MAX_INPUT_VOLTAGE or input_v < MIN_INPUT_VOLTAGE:
                    raise ValueError(f"Input voltage {i+1} (Input_V) range should be between {MIN_INPUT_VOLTAGE}V~{MAX_INPUT_VOLTAGE}V")
            
            # Validate Input Current
            input_i = float(values['Input_I'])
            if input_i > MAX_OUTPUT_CURRENT:
                raise ValueError(f"Input current (Input_I) should not exceed {MAX_OUTPUT_CURRENT}A")

            # Validate Load Settings
            low_load_start = float(values['Low_load_start'])
            low_load_step = float(values['Low_load_step'])
            low_load_stop = float(values['Low_load_stop'])
            high_load_start = float(values['High_load_start'])
            high_load_step = float(values['High_load_step'])
            high_load_stop = float(values['High_load_stop'])

            if low_load_start >= low_load_stop:
                raise ValueError("Low load start should be less than low load stop")
            
            if low_load_stop != high_load_start:
                raise ValueError("Low load stop should equal high load start")
            
            if high_load_start >= high_load_stop:
                raise ValueError("High load start should be less than high load stop")
            
            if low_load_step <= 0 or high_load_step <= 0:
                raise ValueError("Load steps should be greater than 0")

            # Validate Protection Settings
            max_vin = float(values['Max_input_voltage'])
            max_iin = float(values['Max_input_current'])
            max_iout = float(values['Max_load_current'])

            if max_vin < max(input_v_list):
                raise ValueError("Max input voltage protection should be greater than or equal to the highest input voltage")
            
            if max_iin < input_i:
                raise ValueError("Max input current protection should be greater than or equal to input current")
            
            if max_iout < high_load_stop:
                raise ValueError("Max output current protection should be greater than or equal to high load stop")

            # Validate Shunt Settings
            input_shunt_max_voltage = float(values['input_shunt_max_voltage'])
            input_shunt_max_current = float(values['input_shunt_max_current'])
            output_shunt_max_voltage = float(values['output_shunt_max_voltage'])
            output_shunt_max_current = float(values['output_shunt_max_current'])

            if input_shunt_max_current < input_i:
                raise ValueError("Input shunt max current should be greater than or equal to input current")
            
            if output_shunt_max_current < high_load_stop:
                raise ValueError("Output shunt max current should be greater than or equal to high load stop")

            # Validate DAQ Channel Assignments
            required_channels = ['input_v_ch', 'input_i_ch', 'output_v_ch', 'output_i_ch', 'vcc_ch', 'ldo_ch']
            assigned_channels = [values[channel] for channel in required_channels]
            if len(set(assigned_channels)) != len(required_channels):
                raise ValueError("DAQ channels must be unique and all required channels must be assigned")

            return True

        except KeyError as e:
            messagebox.showwarning("Warning", f"Missing required field: {str(e)}")
        except ValueError as e:
            messagebox.showwarning("Warning", str(e))
        except Exception as e:
            messagebox.showwarning("Warning", f"An unexpected error occurred: {str(e)}")

        return False