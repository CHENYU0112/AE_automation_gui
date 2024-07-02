import tkinter as tk
from tkinter import ttk
from .efficiency_tab import EfficiencyTab
from .transient_tab import TransientTab
from config import *

class TestingFrame(tk.Frame):
    def __init__(self, parent, instrument_manager, setting_frame):
        super().__init__(parent, bd=4, relief=tk.RIDGE, bg='gray')
        self.parent = parent
        self.instrument_manager = instrument_manager
        self.setting_frame = setting_frame
        self.output_tab = None
        self.create_widgets()
        self.is_locked = True

    def create_widgets(self):
        self.create_title()
        self.create_output_tab()

    def create_title(self):
        title = tk.Label(self, text="Testing", font=("times new roman", 20, "bold"), bg='black', fg="white")
        title.pack(fill=tk.X, padx=5, pady=5)

    def create_output_tab(self):
        if self.output_tab:
            self.output_tab.destroy()
        test_type = self.setting_frame.test_type
        if test_type == 'Efficiency':
            self.output_tab = EfficiencyTab(self, self.instrument_manager, self.setting_frame)
        elif test_type == 'Transient':
            self.output_tab = TransientTab(self, self.instrument_manager, self.setting_frame)
        else:
            self.output_tab = None
        if self.output_tab:
            self.output_tab.place(x=0, y=60, width=1400, height=1100)

    def lock_frame(self):
        self.is_locked = True
        if self.output_tab:
            self.output_tab.lock_frame()

    def unlock_frame(self):
        self.is_locked = False
        if self.output_tab:
            self.output_tab.unlock_frame()

    def start_test(self):
        if not self.is_locked and self.output_tab:
            self.output_tab.start_test()

    def stop_test(self):
        if not self.is_locked and self.output_tab:
            self.output_tab.stop_test()

    def update_progress(self, value):
        if not self.is_locked and self.output_tab:
            # Implement progress update if needed
            pass

    def update_results(self, text):
        if not self.is_locked and self.output_tab:
            self.output_tab.results_text.insert(tk.END, text + "\n")
            self.output_tab.results_text.see(tk.END)