import tkinter as tk
from tkinter import ttk
from .efficiency_tab import EfficiencyTab
from config import *

class TestingFrame(tk.Frame):
    def __init__(self, parent, instrument_manager, setting_frame):
        super().__init__(parent, bd=4, relief=tk.RIDGE, bg='gray')
        self.parent = parent
        self.instrument_manager = instrument_manager
        self.setting_frame = setting_frame
        self.create_widgets()
        self.is_locked = True

    def create_widgets(self):
        self.create_title()
        self.create_notebook()

    def create_title(self):
        title = tk.Label(self, text="Testing", font=("times new roman", 20, "bold"), bg='black', fg="white")
        title.pack(fill=tk.X, padx=5, pady=5)

    def create_notebook(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create Efficiency Tab
        self.efficiency_tab = EfficiencyTab(self.notebook, self.instrument_manager, self.setting_frame)
        self.notebook.add(self.efficiency_tab, text="Efficiency")

        # Placeholder for future tabs
        # self.create_other_tabs()

    def create_other_tabs(self):
        # Placeholder method for adding other testing tabs in the future
        # For example:
        # self.regulation_tab = RegulationTab(self.notebook, self.instrument_manager, self.setting_frame)
        # self.notebook.add(self.regulation_tab, text="Regulation")
        pass

    def lock_frame(self):
        self.is_locked = True
        # Disable all tabs
        for tab in self.notebook.tabs():
            self.notebook.tab(tab, state='disabled')
        # Disable all widgets in the efficiency tab
        self.efficiency_tab.lock_frame()

    def unlock_frame(self):
        self.is_locked = False
        # Enable all tabs
        for tab in self.notebook.tabs():
            self.notebook.tab(tab, state='normal')
        # Enable all widgets in the efficiency tab
        self.efficiency_tab.unlock_frame()

    def start_efficiency_test(self):
        if not self.is_locked:
            self.efficiency_tab.start_efficiency_test()

    def stop_efficiency_test(self):
        if not self.is_locked:
            self.efficiency_tab.stop_efficiency_test()

    def update_progress(self, value):
        if not self.is_locked:
            self.efficiency_tab.update_progress(value)

    def update_results(self, text):
        if not self.is_locked:
            self.efficiency_tab.update_results(text)