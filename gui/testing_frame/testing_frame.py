import tkinter as tk
from tkinter import ttk
from .efficiency_tab import EfficiencyTab
from .transient_tab import TransientTab
from .switchingnode_tab import SwitchingNodeTab
from config import *

class TestingFrame(tk.Frame):
    def __init__(self, parent, instrument_manager, setting_frame):
        super().__init__(parent, bd=4, relief=tk.RIDGE, bg='gray')
        self.parent = parent
        self.instrument_manager = instrument_manager
        self.setting_frame = setting_frame
        self.output_tab = None
        self.is_locked = True
        self.create_widgets()

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
        tab_class = self.get_tab_class(test_type)

        if tab_class:
            self.output_tab = tab_class(self, self.instrument_manager, self.setting_frame)
            self.output_tab.place(x=0, y=60, width=1400, height=1000)
        else:
            self.output_tab = None

    def get_tab_class(self, test_type):
        tab_classes = {
            'Efficiency': EfficiencyTab,
            'Transient': TransientTab,
            'Switching Node': SwitchingNodeTab,
            # Add more test types here as needed
        }
        return tab_classes.get(test_type)

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
            self.output_tab.update_progress(value)

    def update_results(self, text):
        if not self.is_locked and self.output_tab:
            self.output_tab.update_results(text)
