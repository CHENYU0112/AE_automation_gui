
import tkinter as tk
class TestFrame(tk.Frame):
    def __init__(self, parent, instrument_manager, selected_ic):
        super().__init__(parent, bd=4, relief=tk.RIDGE, bg='white')
        self.instrument_manager = instrument_manager
        self.selected_ic = selected_ic
        self.create_widgets()

    def create_widgets(self):
        raise NotImplementedError("Subclasses must implement create_widgets method")

    def set_default_values(self, settings):
        raise NotImplementedError("Subclasses must implement set_default_values method")

    def get_values(self):
        raise NotImplementedError("Subclasses must implement get_values method")

    def validate_values(self):
        raise NotImplementedError("Subclasses must implement validate_values method")

