import tkinter as tk
from tkinter import ttk, messagebox
import threading
import queue
import sys
import time
import numpy as np
from io import StringIO
from .test_tab import *
from config import *

class TransientTab(TestTab):
    def __init__(self, parent, instrument_manager, setting_frame):
        super().__init__(parent, instrument_manager, setting_frame, "Transient")

    def create_widgets(self):
        self.create_control_frame()
        self.create_results_area()
        
    def create_control_frame(self):
        control_frame = tk.Frame(self, bd=2, relief=tk.RIDGE)
        control_frame.pack(pady=10, padx=10, fill=tk.X)

        self.start_button = tk.Button(control_frame, text="Start Transient Test", command=print("start"))
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(control_frame, text="Stop Test", command=print("stop"), state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        

    def create_results_area(self):
        results_frame = tk.Frame(self, bd=2, relief=tk.RIDGE)
        results_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Add a title for the results area
        self.results_title = tk.Label(results_frame, text="Transient Test", font=("times new roman", 16, "bold"), bg='black', fg="white")
        self.results_title.pack(fill=tk.X, padx=5, pady=5)

        # Increased height and width for the text widgets
        self.results_text = tk.Text(results_frame, height=30, width=40)
        self.results_text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, pady=10, padx=10)

        self.output_text = tk.Text(results_frame, height=30, width=120)
        self.output_text.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, pady=10, padx=10)
        
        
    def lock_frame(self):
        self.start_button.config(state=tk.DISABLED)

    def unlock_frame(self):
        self.start_button.config(state=tk.NORMAL)

    def start_test(self):
        # Implement transient-specific start test logic here
        pass

    def stop_test(self):
        # Implement transient-specific stop test logic here
        pass