import tkinter as tk
from tkinter import ttk, messagebox
from config import *
from instrument_manager import InstrumentManager
from .EfficiencyTest import EfficiencyTestFrame
from .TransientTest import TransientTestFrame
from .SwitchingNodeTest import SwitchingNodeTestFrame
from .TestFrame import TestFrame
from .utils import validate_entry , validate_vin_entry ,validate_eload_entry

class SettingFrame(tk.Frame):
    
    def __init__(self, parent, instrument_manager):
        super().__init__(parent, bd=4, relief=tk.RIDGE, bg='gray')
        self.parent = parent
        self.instrument_manager = instrument_manager
        self.is_locked = False
        self.current_test_frame = None
        self.test_type='none'
        self.create_widgets()
        self.set_default_values()

    def create_widgets(self):
        self.create_title()
        self.create_selection_frame()
        self.create_protection_frame()
        self.create_test_type_frame()
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
        self.create_test_type_frame()
        self.set_default_values(self.ic_combo.get())


    def create_test_type_frame(self):
        if self.current_test_frame:
            self.current_test_frame.destroy()

        test_type = self.test_type_combo.get()
        selected_ic = self.ic_combo.get()

        if test_type == 'Efficiency':
            self.current_test_frame = EfficiencyTestFrame(self, self.instrument_manager, selected_ic)
        elif test_type == 'Transient':
            self.current_test_frame = TransientTestFrame(self, self.instrument_manager, selected_ic)
        elif test_type == 'Switching Node':
            self.current_test_frame = SwitchingNodeTestFrame(self, self.instrument_manager, selected_ic)

        self.current_test_frame.place(x=25, y=240, width=470, height=810)
        
        self.set_default_values(selected_ic)

        
    def create_protection_frame(self):
        frame = tk.Frame(self, bd=2, relief=tk.RIDGE, bg='white')
        frame.place(x=25, y=100, width=470, height=140)
        
        tk.Label(frame, text="Protection", font=FONT_BOLD, bg='white', fg="black").place(x=5, y=5)

        self.max_vin = self.create_entry(frame, "Max Vin(V)", 35)
        self.max_iin = self.create_entry(frame, "Max Iin(A)", 65)
        self.max_iout = self.create_entry(frame, "Max Iout(A)", 95)

    def create_entry(self, parent, label, y, x=None, width=8):
        if label:
            tk.Label(parent, text=label, font=FONT_NORMAL, bg='white', fg="black").place(x=5, y=y)
        entry = tk.Entry(parent, validate="key", validatecommand=(self.register(validate_entry), "%P"),
                         font=("times new roman", 12), bd=2, relief=tk.GROOVE, width=width)
        if x is None:
            x = len(label)*8 + 55
        entry.place(x=x, y=y)
        return entry

    def get_protection_values(self):
        return {
            'max_vin': float(self.max_vin.get()),
            'max_iin': float(self.max_iin.get()),
            'max_iout': float(self.max_iout.get())
        }

    def set_protection_values(self, values):
        self.max_vin.delete(0, tk.END)
        self.max_vin.insert(0, str(values['max_vin']))
        self.max_iin.delete(0, tk.END)
        self.max_iin.insert(0, str(values['max_iin']))
        self.max_iout.delete(0, tk.END)
        self.max_iout.insert(0, str(values['max_iout']))

    def create_button_frame(self):
        frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg='gray', borderwidth=0)
        frame.place(x=25, y=1050, width=470, height=40)

        self.reset_button = tk.Button(frame, text="reset", bg='white', fg="black", padx=20, pady=5,
                  font=BUTTON_FONT, command=self.reset_fields)
        self.reset_button.place(x=30, y=0)
        
        self.set_button = tk.Button(frame, text=" set ", bg='white', fg="black", padx=20, pady=5,
                  font=BUTTON_FONT, command=self.set_values)
        self.set_button.place(x=290, y=0)

    def set_default_values(self, ic='DEFAULT'):
        test_type = self.test_type_combo.get()
        default_settings = IC_DEFAULT_SETTINGS.get(ic, DEFAULT_SETTINGS)[test_type]
        if self.current_test_frame:
            self.current_test_frame.selected_ic = ic
            self.current_test_frame.set_default_values(default_settings)
        
        # Set default protection values
        self.set_protection_values(default_settings['protection'])

    def reset_fields(self):
        selected_ic = self.ic_combo.get()
        test_type = self.test_type_combo.get()
        self.set_default_values(selected_ic)
        self.unlock_frame()
        self.parent.lock_testing_frame()
        if self.current_test_frame:
            self.current_test_frame.set_default_values(IC_DEFAULT_SETTINGS.get(selected_ic, DEFAULT_SETTINGS)[test_type])

    def set_values(self):
        if not self.current_test_frame:
            messagebox.showerror("Error", "No test frame selected")
            return

        if self.current_test_frame.validate_values(self.current_test_frame.get_values()):
            print(self.current_test_frame.get_values())
            # Here you can do something with the values, like saving them or passing them to another part of your application
            messagebox.showinfo("Info", "Values set successfully!")

            # Update the test_type attribute
            self.test_type = self.test_type_combo.get()

            # Create the output tab in the TestingFrame
            self.parent.create_output_tab()

            # Unlock the TestingFrame in the MainApplication
            self.parent.unlock_testing_frame()

            self.lock_frame()
        else:
            messagebox.showerror("Error", "Failed to get validated values")

    def lock_frame(self):
        self.is_locked = True
        for widget in self.winfo_children():
            if isinstance(widget, (tk.Entry, ttk.Combobox, tk.Button)):
                widget.config(state='disabled')
        if self.current_test_frame:
            for widget in self.current_test_frame.winfo_children():
                if isinstance(widget, (tk.Entry, ttk.Combobox, tk.Button)):
                    widget.config(state='disabled')
        # Disable protection frame entries
        self.max_vin.config(state='disabled')
        self.max_iin.config(state='disabled')
        self.max_iout.config(state='disabled')

    def unlock_frame(self):
        self.is_locked = False
        for widget in self.winfo_children():
            if isinstance(widget, (tk.Entry, ttk.Combobox, tk.Button)):
                widget.config(state='normal')
        if self.current_test_frame:
            for widget in self.current_test_frame.winfo_children():
                if isinstance(widget, (tk.Entry, ttk.Combobox, tk.Button)):
                    widget.config(state='normal')
        # Enable protection frame entries
        self.max_vin.config(state='normal')
        self.max_iin.config(state='normal')
        self.max_iout.config(state='normal')


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