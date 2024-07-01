import tkinter as tk
from tkinter import ttk, messagebox
from config import *
from instrument_manager import InstrumentManager

class SettingFrame(tk.Frame):
    def __init__(self, parent, instrument_manager):
        super().__init__(parent, bd=4, relief=tk.RIDGE, bg='gray')
        self.parent = parent
        self.instrument_manager = instrument_manager
        self.create_widgets()
        self.set_default_values()
        self.is_locked = False

    def create_widgets(self):
        self.create_title()
        self.create_ic_selection_frame()  # New method to create IC selectio
        self.create_power_supply_frame()
        self.create_daq_frame()
        self.create_load_frame()
        self.create_protection_frame()
        self.create_current_shunt_frame()
        self.create_button_frame()

    def create_title(self):
        title = tk.Label(self, text="Setting", font=("times new roman", 20, "bold"), bg='black', fg="white")
        title.pack(fill=tk.X, padx=5, pady=5)
        
    def create_ic_selection_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=50, width=450, height=40)
        
        tk.Label(frame, text="IC", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        self.ic_combo = ttk.Combobox(frame, width=20, values=IC_OPTIONS)
        self.ic_combo.place(x=100, y=5)
        self.ic_combo.set('DEFAULT')  # Set default value
        self.ic_combo.bind("<<ComboboxSelected>>", self.on_ic_selected)
        
        
    def on_ic_selected(self, event):
        selected_ic = self.ic_combo.get()
        self.set_default_values(selected_ic)
        
    def create_power_supply_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=100, width=450, height=150)
        
        tk.Label(frame, text="Power_Supply", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.instruments['supply'], font=FONT_BOLD, bg='white', fg="black").place(x=115, y=5)

        self.vin = self.create_entry(frame, "Vin(V)", 35)
        self.iin = self.create_entry(frame, "Iin(A)", 65)
        
        tk.Label(frame, text="CH", font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=95)
        self.pw_ch = ttk.Combobox(frame, width=5, values=POWER_SUPPLY_CHANNELS)
        self.pw_ch.place(x=35, y=95)

    def create_daq_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=260, width=450, height=220)
        
        tk.Label(frame, text="DAQ", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.instruments['DAQ'], font=FONT_BOLD, bg='white', fg="black").place(x=115, y=5)

        self.daq_channels = []
        for i in range(1, 7):
            label = tk.Label(frame, text=f"CH{i}", font=FONT_NORMAL, bg='white', fg="black")
            label.place(x=5, y=30 + 25*(i-1))
            combo = ttk.Combobox(frame, width=20, values=DAQ_OPTIONS)
            combo.place(x=55, y=30 + 25*(i-1))
            self.daq_channels.append(combo)

    def create_load_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=490, width=450, height=200)  # Increased height to accommodate new entries
        
        tk.Label(frame, text="E Load", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.instruments['load'], font=FONT_BOLD, bg='white', fg="black").place(x=110, y=5)

        tk.Label(frame, text="Low Load", font=FONT_BOLD, bg='white', fg="black").place(x=90, y=30)
        tk.Label(frame, text="High Load", font=FONT_BOLD, bg='white', fg="black").place(x=270, y=30)

        self.low_load_entries = self.create_load_entries(frame, 90)
        self.high_load_entries = self.create_load_entries(frame, 270)

    def create_load_entries(self, parent, x):
        entries = []
        labels = ["Start :", "Step :", "Stop :", "Delay(s):"]
        for i, label in enumerate(labels):
            tk.Label(parent, text=label, font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=55 + i*25)
            entry = self.create_entry(parent, "", 55 + i*25, x=x)
            entries.append(entry)
        return entries

    def create_protection_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=700, width=450, height=150)
        
        tk.Label(frame, text="Protection", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)

        self.max_vin = self.create_entry(frame, "Max Vin(V)", 35)
        self.max_iin = self.create_entry(frame, "Max Iin(A)", 65)
        self.max_iout = self.create_entry(frame, "Max Iout(A)", 95)

    def create_current_shunt_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=860, width=450, height=150)
        
        tk.Label(frame, text="Current Shunt ", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)

        labels = ["Max Vin(V)", "Max Iin(A)", "Max Vout(V)", "Max Iout(A)"]
        self.shunt_entries = []

        for i, label in enumerate(labels):
            row = i // 2
            col = i % 2
            tk.Label(frame, text=label, font=FONT_NORMAL, bg='white', fg="black").place(x=5 + col*225, y=30 + row*30)
            entry = self.create_entry(frame, "", 30 + row*30, x=130 + col*225, width=8)
            self.shunt_entries.append(entry)

    def create_button_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='gray', borderwidth=0)
        frame.place(x=25, y=1020, width=450, height=60)

        self.reset_button = tk.Button(frame, text="reset", bg='white', fg="black", padx=20, pady=5,
                  font=BUTTON_FONT, command=self.reset_fields)
        self.reset_button.place(x=30, y=10)
        
        self.set_button = tk.Button(frame, text=" set ", bg='white', fg="black", padx=20, pady=5,
                  font=BUTTON_FONT, command=self.set_values)
        self.set_button.place(x=270, y=10)

    def create_entry(self, parent, label, y, x=None, width=8):
        if label:
            tk.Label(parent, text=label, font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=y)
        entry = tk.Entry(parent, validate="key", validatecommand=(self.register(self.validate_entry), "%P"),
                         font=("times new roman", 12), bd=2, relief=tk.GROOVE, width=width)
        if x is None:
            x = len(label)*8 + 55
        entry.place(x=x, y=y)
        return entry

    @staticmethod
    def validate_entry(P):
        return P == "" or P == "." or (P.count('.') <= 1 and P.replace('.', '').isdigit())

    def set_default_values(self, ic='DEFAULT'):
        default_settings = IC_DEFAULT_SETTINGS.get(ic, DEFAULT_SETTINGS)
        
        # Power Supply
        self.vin.delete(0, tk.END)
        self.vin.insert(0, str(default_settings['power_supply']['vin']))
        self.iin.delete(0, tk.END)
        self.iin.insert(0, str(default_settings['power_supply']['iin']))
        self.pw_ch.set(default_settings['power_supply']['channel'])

        # DAQ
        for i, combo in enumerate(self.daq_channels, 1):
            combo.set(default_settings['daq'][f'ch{i}'])

        # Load
        load_params = ['start', 'step', 'stop', 'delay']
        for i, entry in enumerate(self.low_load_entries):
            key = load_params[i]
            value = default_settings['load']['low_load'].get(key, 1)
            entry.delete(0, tk.END)
            entry.insert(0, str(value))
        for i, entry in enumerate(self.high_load_entries):
            key = load_params[i]
            value = default_settings['load']['high_load'].get(key, 1)
            entry.delete(0, tk.END)
            entry.insert(0, str(value))

        # Protection
        self.max_vin.delete(0, tk.END)
        self.max_vin.insert(0, str(default_settings['protection']['max_vin']))
        self.max_iin.delete(0, tk.END)
        self.max_iin.insert(0, str(default_settings['protection']['max_iin']))
        self.max_iout.delete(0, tk.END)
        self.max_iout.insert(0, str(default_settings['protection']['max_iout']))

        # Current Shunt Settings
        shunt_values = default_settings['current_shunt'].values()
        for entry, value in zip(self.shunt_entries, shunt_values):
            entry.delete(0, tk.END)
            entry.insert(0, str(value))

    def reset_fields(self):
        
        def clear_widget(widget):
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)
            elif isinstance(widget, ttk.Combobox):
                widget.set('')
            elif isinstance(widget, tk.Text):
                widget.delete(1.0, tk.END)
            
            for child in widget.winfo_children():
                clear_widget(child)
        selected_ic =self.ic_combo.get()
      
        clear_widget(self)
        self.ic_combo.set(selected_ic)
        self.set_default_values(selected_ic)
        self.unlock_frame()
        self.parent.lock_testing_frame()

    def set_values(self):
        try:
            values = self.get_all_values()
            daq_error = self.check_daq_duplicates()
            if daq_error:
                messagebox.showwarning("Warning", daq_error)
                return
            if self.validate_values(values):
                messagebox.showinfo("Info", "Successfully set!")
                self.lock_frame()
                self.parent.unlock_testing_frame()
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

        input_v = safe_float(self.vin.get(), "Input Voltage (Input_V)")
        input_i = safe_float(self.iin.get(), "Input Current (Input_I)")
        power_supply_channel = self.pw_ch.get()
        daq_channels = [combo.get() for combo in self.daq_channels]
        max_vin = safe_float(self.max_vin.get(), "Protective Maximum Input Voltage (MAX_Vin)")
        max_iin = safe_float(self.max_iin.get(), "Protective Maximum Input Current (MAX_Iin)")
        max_iout = safe_float(self.max_iout.get(), "Protective Maximum Output Current (MAX_Iout)")

        load_params = ['start', 'step', 'stop', 'delay']
        low_load_values = [safe_float(entry.get(), f"Low Load {param.capitalize()}") for entry, param in zip(self.low_load_entries, load_params)]
        high_load_values = [safe_float(entry.get(), f"High Load {param.capitalize()}") for entry, param in zip(self.high_load_entries, load_params)]

        input_shunt_max_voltage = safe_float(self.shunt_entries[0].get(), "Input Shunt Max Voltage")
        input_shunt_max_current = safe_float(self.shunt_entries[1].get(), "Input Shunt Max Current")
        output_shunt_max_voltage = safe_float(self.shunt_entries[2].get(), "Output Shunt Max Voltage")
        output_shunt_max_current = safe_float(self.shunt_entries[3].get(), "Output Shunt Max Current")

        values = {
            'selected_ic' : self.ic_combo.get(),
            'input_v': input_v,
            'input_i': input_i,
            'power_supply_channel': power_supply_channel,
            'daq_channels': daq_channels,
            'max_vin': max_vin,
            'max_iin': max_iin,
            'max_iout': max_iout,
            'low_load': dict(zip(load_params, low_load_values)),
            'high_load': dict(zip(load_params, high_load_values)),
            'shunt_settings': [
                input_shunt_max_voltage,
                input_shunt_max_current,
                output_shunt_max_voltage,
                output_shunt_max_current
            ]
        }

        return values

    def check_daq_duplicates(self):
        selections = [combo.get() for combo in self.daq_channels if combo.get()]
        duplicates = set([x for x in selections if selections.count(x) > 1])
        if duplicates:
            return f"Duplicate DAQ selections found: {', '.join(duplicates)}"
        return None

    def validate_values(self, values):
        try:
            # Validate input voltage and current
            input_v = float(values['input_v'])
            input_i = float(values['input_i'])

            if input_v > MAX_INPUT_VOLTAGE or input_v < MIN_INPUT_VOLTAGE:
                raise ValueError(f"Input voltage (Input_V) range should be between {MIN_INPUT_VOLTAGE}V~{MAX_INPUT_VOLTAGE}V")
            
            if input_i > MAX_OUTPUT_CURRENT:
                raise ValueError(f"Input current (Input_I) should not exceed {MAX_OUTPUT_CURRENT}A")

            # Validate load settings
            low_load_start = float(values['low_load']['start'])
            low_load_step = float(values['low_load']['step'])
            low_load_stop = float(values['low_load']['stop'])
            high_load_step = float(values['high_load']['step'])
            high_load_stop = float(values['high_load']['stop'])

            if low_load_start >= low_load_stop:
                raise ValueError("Low load start should be less than low load stop")
            
            if low_load_stop >= high_load_stop:
                raise ValueError("Low load stop should be less than high load stop")
            
            if low_load_step <= 0 or high_load_step <= 0:
                raise ValueError("Load steps should be greater than 0")

            # Validate protection settings
            max_vin = float(values['max_vin'])
            max_iin = float(values['max_iin'])
            max_iout = float(values['max_iout'])

            if max_vin < input_v:
                raise ValueError("Max input voltage protection should be greater than or equal to input voltage")
            
            if max_iin < input_i:
                raise ValueError("Max input current protection should be greater than or equal to input current")
            
            if max_iout < high_load_stop:
                raise ValueError("Max output current protection should be greater than or equal to high load stop")

            # Validate shunt settings
            input_shunt_max_voltage, input_shunt_max_current, output_shunt_max_voltage, output_shunt_max_current = values['shunt_settings']

            if input_shunt_max_current < input_i:
                raise ValueError("Input shunt max current should be greater than or equal to input current")
            
            if output_shunt_max_current < high_load_stop:
                raise ValueError("Output shunt max current should be greater than or equal to high load stop")

            # Validate DAQ channel assignments
            daq_channels = values['daq_channels']
            if len(set(daq_channels)) != len(daq_channels):
                raise ValueError("DAQ channels must be unique")

            return True

        except KeyError as e:
            messagebox.showwarning("Warning", f"Missing required field: {str(e)}")
        except ValueError as e:
            messagebox.showwarning("Warning", str(e))
        except Exception as e:
            messagebox.showwarning("Warning", f"An unexpected error occurred: {str(e)}")

        return False

    def lock_frame(self):
        self.is_locked = True
        for widget in self.winfo_children():
            if widget != self.reset_button and isinstance(widget, (tk.Entry, ttk.Combobox, tk.Button)):
                widget.config(state='disabled')
    def unlock_frame(self):
            self.is_locked = False
            for widget in self.winfo_children():
                if isinstance(widget, (tk.Entry, ttk.Combobox, tk.Button)):
                    widget.config(state='normal')

    def get_instrument_manager(self):
        return self.instrument_manager

    def update_instrument_info(self):
        self.power_supply_label.config(text=self.instrument_manager.instruments['supply'])
        self.daq_label.config(text=self.instrument_manager.instruments['DAQ'])
        self.load_label.config(text=self.instrument_manager.instruments['load'])

        # Assuming you have labels for each instrument, update them here
        # For example:
        # self.supply_label.config(text=supply_info)
        # self.daq_label.config(text=daq_info)
        # self.load_label.config(text=load_info)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.instrument_manager.disconnect_all()
            self.parent.destroy()