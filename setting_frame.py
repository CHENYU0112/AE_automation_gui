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
        self.create_power_supply_frame()
        self.create_daq_frame()
        self.create_load_frame()
        self.create_protection_frame()
        self.create_current_shunt_frame()
        self.create_button_frame()

    def create_title(self):
        title = tk.Label(self, text="Setting", font=("times new roman", 20, "bold"), bg='black', fg="white")
        title.pack(fill=tk.X, padx=5, pady=5)

    def create_power_supply_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=60, width=450, height=150)
        
        tk.Label(frame, text="Power_Supply", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.instruments['supply'], font=FONT_BOLD, bg='white', fg="black").place(x=115, y=5)

        self.vin = self.create_entry(frame, "Vin(V)", 35)
        self.iin = self.create_entry(frame, "Iin(A)", 65)
        
        tk.Label(frame, text="CH", font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=95)
        self.pw_ch = ttk.Combobox(frame, width=5, values=POWER_SUPPLY_CHANNELS)
        self.pw_ch.place(x=35, y=95)

    def create_daq_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=220, width=450, height=220)
        
        tk.Label(frame, text="DAQ", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.instruments['DAQ'], font=FONT_BOLD, bg='white', fg="black").place(x=115, y=5)
        # Check if 'DAQ' key exists in instruments dictionary
        # daq_info = self.instrument_manager.instruments.get('DAQ', 'Not detected')
        # tk.Label(frame, text=daq_info, font=FONT_BOLD, bg='white', fg="black").place(x=110, y=5)

        self.daq_channels = []
        for i in range(1, 7):
            label = tk.Label(frame, text=f"CH{i}", font=FONT_NORMAL, bg='white', fg="black")
            label.place(x=5, y=30 + 25*(i-1))
            combo = ttk.Combobox(frame, width=20, values=DAQ_OPTIONS)
            combo.place(x=55, y=30 + 25*(i-1))
            self.daq_channels.append(combo)

    def create_load_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=450, width=450, height=150)
        
        tk.Label(frame, text="E Load", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)
        tk.Label(frame, text=self.instrument_manager.instruments['load'], font=FONT_BOLD, bg='white', fg="black").place(x=110, y=5)

        tk.Label(frame, text="Low Load", font=FONT_BOLD, bg='white', fg="black").place(x=90, y=30)
        tk.Label(frame, text="High Load", font=FONT_BOLD, bg='white', fg="black").place(x=270, y=30)

        self.low_load_entries = self.create_load_entries(frame, 90)
        self.high_load_entries = self.create_load_entries(frame, 270)

    def create_load_entries(self, parent, x):
        entries = []
        for i, label in enumerate(["Start :", "Step :", "Stop :"]):
            tk.Label(parent, text=label, font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=55 + i*25)
            entry = self.create_entry(parent, "", 55 + i*25, x=x)
            entries.append(entry)
        return entries

    def create_protection_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=610, width=450, height=150)
        
        tk.Label(frame, text="Protection", font=FONT_BOLD, bg='yellow', fg="black").place(x=5, y=5)

        self.max_vin = self.create_entry(frame, "Max Vin(V)", 35)
        self.max_iin = self.create_entry(frame, "Max Iin(A)", 65)
        self.max_iout = self.create_entry(frame, "Max Iout(A)", 95)

    def create_current_shunt_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=770, width=450, height=150)
        
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
        frame.place(x=25, y=920, width=450, height=60)

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

    def set_default_values(self):
        # Power Supply
        self.vin.insert(0, str(DEFAULT_SETTINGS['power_supply']['vin']))
        self.iin.insert(0, str(DEFAULT_SETTINGS['power_supply']['iin']))
        self.pw_ch.set(DEFAULT_SETTINGS['power_supply']['channel'])

        # DAQ
        for i, combo in enumerate(self.daq_channels, 1):
            combo.set(DEFAULT_SETTINGS['daq'][f'ch{i}'])

        # Load
        for i, entry in enumerate(self.low_load_entries):
            key = ['start', 'step', 'stop'][i]
            entry.insert(0, str(DEFAULT_SETTINGS['load']['low_load'][key]))
        for i, entry in enumerate(self.high_load_entries):
            key = ['start', 'step', 'stop'][i]
            entry.insert(0, str(DEFAULT_SETTINGS['load']['high_load'][key]))

        # Protection
        self.max_vin.insert(0, str(DEFAULT_SETTINGS['protection']['max_vin']))
        self.max_iin.insert(0, str(DEFAULT_SETTINGS['protection']['max_iin']))
        self.max_iout.insert(0, str(DEFAULT_SETTINGS['protection']['max_iout']))

        # Current Shunt Settings
        shunt_values = DEFAULT_SETTINGS['current_shunt'].values()
        for entry, value in zip(self.shunt_entries, shunt_values):
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

        clear_widget(self)
        self.set_default_values()
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

        values = {
            'input_v': safe_float(self.vin.get(), "Input Voltage (Input_V)"),
            'input_i': safe_float(self.iin.get(), "Input Current (Input_I)"),
            'max_vin': safe_float(self.max_vin.get(), "Protective Maximum Input Voltage (MAX_Vin)"),
            'max_iin': safe_float(self.max_iin.get(), "Protective Maximum Input Current (MAX_Iin)"),
            'max_iout': safe_float(self.max_iout.get(), "Protective Maximum Output Current (MAX_Iout)"),
            'low_load': [
                safe_float(self.low_load_start.get(), "Low Load Start"),
                safe_float(self.low_load_step.get(), "Low Load Step"),
                safe_float(self.low_load_stop.get(), "Low Load Stop")
            ],
            'high_load': [
                safe_float(self.high_load_step.get(), "High Load Step"),
                safe_float(self.high_load_stop.get(), "High Load Stop")
            ],
            'shunt_settings': [
                safe_float(self.input_shunt_max_voltage.get(), "Input Shunt Max Voltage"),
                safe_float(self.input_shunt_max_current.get(), "Input Shunt Max Current"),
                safe_float(self.output_shunt_max_voltage.get(), "Output Shunt Max Voltage"),
                safe_float(self.output_shunt_max_current.get(), "Output Shunt Max Current")
            ],
            'daq': [
                self.input_v_ch.get(),
                self.input_i_ch.get(),
                self.output_v_ch.get(),
                self.output_i_ch.get(),
                self.vcc_ch.get(),
                self.ldo_ch.get()
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
            input_v = float(values['input_v'])
            max_vin = float(values['max_vin'])
            input_i = float(values['input_i'])
            max_iin = float(values['max_iin'])
            low_load_start = float(values['low_load'][0])
            low_load_step = float(values['low_load'][1])
            low_load_stop = float(values['low_load'][2])
            high_load_start = float(values['high_load'][0])
            high_load_step = float(values['high_load'][1])
            high_load_stop = float(values['high_load'][2])
            max_iout = float(values['max_iout'])

            if input_v > max_vin:
                raise ValueError("Protective maximum input voltage (MAX_Vin) must be at least the Input voltage (Input_V)")
            elif input_i > max_iin:
                raise ValueError("Protective maximum input current (MAX_Iin) must be at least the Input current (Input_I)")
            elif input_v > MAX_INPUT_VOLTAGE or input_v < MIN_INPUT_VOLTAGE:
                raise ValueError(f"Input voltage (Input_V) range should be between {MIN_INPUT_VOLTAGE}V~{MAX_INPUT_VOLTAGE}V")
            elif high_load_start < low_load_stop:
                raise ValueError("High Load Start Current should not be lower than the Low Load Stop")
            elif any(load > MAX_OUTPUT_CURRENT for load in [low_load_stop, high_load_stop, max_iout]):
                raise ValueError(f"Output current should < {MAX_OUTPUT_CURRENT}A")
            elif low_load_step > (low_load_stop - low_load_start):
                raise ValueError("Invalid low load step")
            elif high_load_step > (high_load_stop - high_load_start):
                raise ValueError("Invalid high load step")
            else:
                return True
        except ValueError as e:
            messagebox.showwarning("Warning", str(e))

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