import tkinter as tk
from tkinter import ttk
from efficiency_tab import EfficiencyTab

class TestingFrame(tk.Frame):
    def __init__(self, parent, instrument_manager, setting_frame):
        super().__init__(parent, bd=4, relief=tk.RIDGE, bg='gray')
        self.parent = parent
        self.instrument_manager = instrument_manager
        self.setting_frame = setting_frame
        self.create_widgets()
        self.is_locked = True
        self.lock_frame()

    def create_widgets(self):
        self.create_notebook()

    def create_notebook(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create Efficiency Tab
        self.efficiency_tab = EfficiencyTab(self.notebook, self.instrument_manager, self.setting_frame)
        self.notebook.add(self.efficiency_tab, text="Efficiency")

    def lock_frame(self):
        self.is_locked = True
        # Disable all tabs
        for tab in self.notebook.tabs():
            self.notebook.tab(tab, state='disabled')
        # Disable all widgets in the efficiency tab
        for widget in self.efficiency_tab.winfo_children():
            if isinstance(widget, (tk.Entry, ttk.Combobox, tk.Button)):
                widget.config(state='disabled')

    def unlock_frame(self):
        self.is_locked = False
        # Enable all tabs
        for tab in self.notebook.tabs():
            self.notebook.tab(tab, state='normal')
        # Enable all widgets in the efficiency tab
        for widget in self.efficiency_tab.winfo_children():
            if isinstance(widget, (tk.Entry, ttk.Combobox, tk.Button)):
                widget.config(state='normal')