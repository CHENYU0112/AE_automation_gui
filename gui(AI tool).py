import tkinter as tk
from tkinter import ttk, messagebox
from config import *
from instrument_manager import InstrumentManager
from setting_frame import SettingFrame
from testing_frame import TestingFrame
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.instrument_manager = InstrumentManager()
        self.instrument_manager.find_devices()
        self.configure_window()
        self.create_widgets()

    def configure_window(self):
        self.parent.title("PoL Automation V1.0.0")
        self.parent.geometry(WINDOW_SIZE)
        self.parent.resizable(False, False)

    def create_widgets(self):
        self.setting_frame = SettingFrame(self, self.instrument_manager)
        self.setting_frame.place(x=20, y=20, width=500, height=1100)  


        self.testing_frame = TestingFrame(self, self.instrument_manager, self.setting_frame)
        self.testing_frame.place(x=550, y=20, width=1400, height=1100)
        
        # Lock the testing frame immediately after creation
        self.lock_testing_frame()

    def unlock_testing_frame(self):
        self.testing_frame.unlock_frame()

    def lock_testing_frame(self):
        self.testing_frame.lock_frame()

def main():
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    
    root.mainloop()

if __name__ == "__main__":
    main()