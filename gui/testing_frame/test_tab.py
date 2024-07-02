import tkinter as tk
from tkinter import ttk, messagebox
import threading
import queue
import sys
import time
import numpy as np
from io import StringIO
from config import *

class TestTab(tk.Frame):
    def __init__(self, parent, instrument_manager, setting_frame, test_name):
        super().__init__(parent)
        self.instrument_manager = instrument_manager
        self.setting_frame = setting_frame
        self.test_name = test_name
        self.test_running = False
        self.output_queue = queue.Queue()
        self.create_widgets()

    def create_widgets(self):
        self.create_control_frame()
        self.create_results_area()

    def create_control_frame(self):
        control_frame = tk.Frame(self, bd=2, relief=tk.RIDGE)
        control_frame.pack(pady=10, padx=10, fill=tk.X)

        self.start_button = tk.Button(control_frame, text=f"Start {self.test_name} Test", command=self.start_test)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(control_frame, text="Stop Test", command=self.stop_test, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

    def create_results_area(self):
        results_frame = tk.Frame(self, bd=2, relief=tk.RIDGE)
        results_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.results_title = tk.Label(results_frame, text=f"{self.test_name} Test", font=("times new roman", 16, "bold"), bg='black', fg="white")
        self.results_title.pack(fill=tk.X, padx=5, pady=5)

        self.results_text = tk.Text(results_frame, height=30, width=40)
        self.results_text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, pady=10, padx=10)

        self.output_text = tk.Text(results_frame, height=30, width=120)
        self.output_text.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, pady=10, padx=10)

    def start_test(self):
        # To be implemented in child classes
        pass

    def stop_test(self):
        # To be implemented in child classes
        pass

    def lock_frame(self):
        self.start_button.config(state=tk.DISABLED)

    def unlock_frame(self):
        self.start_button.config(state=tk.NORMAL)