from .TestFrame import TestFrame
import tkinter as tk
from tkinter import ttk, messagebox
from config import *
from .utils import validate_entry

class EfficiencyTestFrame(TestFrame):
    def __init__(self, parent, instrument_manager, selected_ic):
        super().__init__(parent, instrument_manager, selected_ic)

    def create_widgets(self):
        tk.Label(self, text="Efficiency Test Settings", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        self.create_power_supply_frame()
        self.create_daq_frame()
        self.create_load_frame()
        self.create_protection_frame()
        self.create_current_shunt_frame()

    def create_power_supply_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=5, y=30, width=450, height=150)
        
        tk.Label(frame, text="Power_Supply", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.instruments['supply'], font=FONT_BOLD, bg='white', fg="black").place(x=115, y=5)

        self.vin_frame = tk.Frame(frame, bg='white')
        self.vin_frame.place(x=5, y=35, width=200, height=100)
        
        self.vin = self.create_entry(self.vin_frame, "Vin(V)", 0)
        self.iin = self.create_entry(self.vin_frame, "Iin(A)", 30)
        
        tk.Label(self.vin_frame, text="CH", font=FONT_NORMAL, bg='white', fg="black").place(x=0, y=60)
        self.pw_ch_vin = ttk.Combobox(self.vin_frame, width=5, values=POWER_SUPPLY_CHANNELS)
        self.pw_ch_vin.place(x=30, y=60)

        self.vcc_var = tk.BooleanVar()
        self.vcc_checkbox = tk.Checkbutton(frame, text="VCC", variable=self.vcc_var, 
                                           command=self.toggle_vcc_frame, bg='white')
        self.vcc_checkbox.place(x=190, y=35)

        self.vcc_frame = tk.Frame(frame, bg='white')
        self.vcc_frame.place(x=250, y=35, width=200, height=100)
        
        self.vcc = self.create_entry(self.vcc_frame, "Vcc(V)", 0)
        self.icc = self.create_entry(self.vcc_frame, "Icc(A)", 30)
        tk.Label(self.vcc_frame, text="CH", font=FONT_NORMAL, bg='white', fg="black").place(x=0, y=60)
        self.pw_ch_vcc = ttk.Combobox(self.vcc_frame, width=5, values=POWER_SUPPLY_CHANNELS)
        self.pw_ch_vcc.place(x=30, y=60)

    def create_daq_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=5, y=190, width=450, height=220)
        
        tk.Label(frame, text="DAQ", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.instruments['DAQ'], font=FONT_BOLD, bg='white', fg="black").place(x=115, y=5)

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
        tk.Label(frame, text=self.instrument_manager.instruments['load'], font=FONT_BOLD, bg='white', fg="black").place(x=110, y=5)
        tk.Label(frame, text="Low Load", font=FONT_BOLD, bg='white', fg="black").place(x=90, y=30)
        tk.Label(frame, text="High Load", font=FONT_BOLD, bg='white', fg="black").place(x=270, y=30)

        self.low_load_entries, self.low_load_vars = self.create_load_entries(frame, 90, is_low_load=True)
        self.high_load_entries, self.high_load_vars = self.create_load_entries(frame, 270, is_low_load=False)

        self.low_load_stop_var = self.low_load_vars[2]
        self.high_load_start_var = self.high_load_vars[0]
        
        self.low_load_stop_var.trace_add('write', self.update_high_load_start)
        self.high_load_start_var.trace_add('write', self.update_low_load_stop)

    def create_protection_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=5, y=630, width=450, height=140)
        
        tk.Label(frame, text="Protection", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)

        self.max_vin = self.create_entry(frame, "Max Vin(V)", 35)
        self.max_iin = self.create_entry(frame, "Max Iin(A)", 65)
        self.max_iout = self.create_entry(frame, "Max Iout(A)", 95)

    def create_current_shunt_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=5, y=780, width=450, height=130)
        
        tk.Label(frame, text="Current Shunt ", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)

        labels = ["Max Vin(V)", "Max Iin(A)", "Max Vout(V)", "Max Iout(A)"]
        self.shunt_entries = []

        for i, label in enumerate(labels):
            row = i // 2
            col = i % 2
            tk.Label(frame, text=label, font=FONT_NORMAL, bg='white', fg="black").place(x=5 + col*225, y=30 + row*30)
            entry = self.create_entry(frame, "", 30 + row*30, x=130 + col*225, width=8)
            self.shunt_entries.append(entry)

    def create_entry(self, parent, label, y, x=None, width=8):
        if label:
            tk.Label(parent, text=label, font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=y)
        entry = tk.Entry(parent, validate="key", validatecommand=(self.register(validate_entry), "%P"),
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
        self.vcc.insert(0, "0")
        self.icc.delete(0, tk.END)
        self.icc.insert(0, "0")
        self.pw_ch_vcc.set("")
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

        # Protection
        self.max_vin.delete(0, tk.END)
        self.max_vin.insert(0, str(settings['protection']['max_vin']))
        self.max_iin.delete(0, tk.END)
        self.max_iin.insert(0, str(settings['protection']['max_iin']))
        self.max_iout.delete(0, tk.END)
        self.max_iout.insert(0, str(settings['protection']['max_iout']))

        # Current Shunt
        shunt_values = settings['current_shunt'].values()
        for entry, value in zip(self.shunt_entries, shunt_values):
            entry.delete(0, tk.END)
            entry.insert(0, str(value))

    def get_values(self):
        values = {
            'power_supply': {
                'vin': float(self.vin.get()),
                'iin': float(self.iin.get()),
                'vin_channel': self.pw_ch_vin.get(),
                'vcc_enabled': self.vcc_var.get(),
                'vcc': float(self.vcc.get()) if self.vcc_var.get() else 0,
                'icc': float(self.icc.get()) if self.vcc_var.get() else 0,
                'vcc_channel': self.pw_ch_vcc.get() if self.vcc_var.get() else ''
            },
            'daq': {f'ch{i+1}': combo.get() for i, combo in enumerate(self.daq_channels)},
            'load': {
                'low_load': {param: float(entry.get()) for param, entry in zip(['start', 'step', 'stop', 'delay'], self.low_load_entries)},
                'high_load': {param: float(entry.get()) for param, entry in zip(['start', 'step', 'stop', 'delay'], self.high_load_entries)}
            },
            'protection': {
                'max_vin': float(self.max_vin.get()),
                'max_iin': float(self.max_iin.get()),
                'max_iout': float(self.max_iout.get())
            },
            'current_shunt': {
                label: float(entry.get()) for label, entry in zip(["Input Shunt Max Voltage", "Input Shunt Max Current", 
                                                                   "Output Shunt Max Voltage", "Output Shunt Max Current"], 
                                                                  self.shunt_entries)
            }
        }
        return values
    
    def validate_values(self):
        values = self.get_values()
        try:
            # Validate input voltage and current
            input_v = values['power_supply']['vin']
            input_i = values['power_supply']['iin']

            if input_v > MAX_INPUT_VOLTAGE or input_v < MIN_INPUT_VOLTAGE:
                raise ValueError(f"Input voltage (Input_V) range should be between {MIN_INPUT_VOLTAGE}V~{MAX_INPUT_VOLTAGE}V")
            
            if input_i > MAX_OUTPUT_CURRENT:
                raise ValueError(f"Input current (Input_I) should not exceed {MAX_OUTPUT_CURRENT}A")

            # Validate load settings
            low_load = values['load']['low_load']
            high_load = values['load']['high_load']

            if low_load['start'] >= low_load['stop']:
                raise ValueError("Low load start should be less than low load stop")
            
            if low_load['stop'] >= high_load['stop']:
                raise ValueError("Low load stop should be less than high load stop")
            
            if low_load['step'] <= 0 or high_load['step'] <= 0:
                raise ValueError("Load steps should be greater than 0")

            # Validate protection settings
            max_vin = values['protection']['max_vin']
            max_iin = values['protection']['max_iin']
            max_iout = values['protection']['max_iout']

            if max_vin < input_v:
                raise ValueError("Max input voltage protection should be greater than or equal to input voltage")
            
            if max_iin < input_i:
                raise ValueError("Max input current protection should be greater than or equal to input current")
            
            if max_iout < high_load['stop']:
                raise ValueError("Max output current protection should be greater than or equal to high load stop")

            # Validate shunt settings
            shunt = values['current_shunt']
            if shunt["Input Shunt Max Current"] < input_i:
                raise ValueError("Input shunt max current should be greater than or equal to input current")
            
            if shunt["Output Shunt Max Current"] < high_load['stop']:
                raise ValueError("Output shunt max current should be greater than or equal to high load stop")

            # Validate DAQ channel assignments
            daq_channels = list(values['daq'].values())
            if len(set(daq_channels)) != len(daq_channels):
                raise ValueError("DAQ channels must be unique")
            
            # Validate VCC settings if enabled
            if values['power_supply']['vcc_enabled']:
                vcc_voltage = values['power_supply']['vcc']
                vcc_current = values['power_supply']['icc']
                vcc_channel = values['power_supply']['vcc_channel']

                if vcc_voltage <= 0 or vcc_voltage > MAX_INPUT_VOLTAGE:
                    raise ValueError(f"VCC voltage should be between 0 and {MAX_INPUT_VOLTAGE}V")

                if vcc_current <= 0 or vcc_current > MAX_OUTPUT_CURRENT:
                    raise ValueError(f"VCC current should be between 0 and {MAX_OUTPUT_CURRENT}A")

                if not vcc_channel:
                    raise ValueError("VCC channel must be selected")
                
                if values['power_supply']['vin_channel'] == vcc_channel:
                    raise ValueError("Power supply channels must be unique")

            return True

        except ValueError as e:
            messagebox.showwarning("Validation Error", str(e))
            return False