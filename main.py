import tkinter as tk
from tkinter import ttk, messagebox
import os
from instrument_manager import InstrumentManager
from gui.setting_frame.setting_frame import SettingFrame
from gui.testing_frame.testing_frame import TestingFrame
from config import WINDOW_SIZE, FONT_TITLE
import warnings
from openpyxl.chart import ScatterChart, Reference, Series
from openpyxl.chart.marker import Marker
warnings.filterwarnings("ignore", category=FutureWarning)
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.instrument_manager = InstrumentManager()
        self.setup_instruments()
        self.configure_window()
        self.create_widgets()

    def setup_instruments(self):
        self.instrument_manager.find_devices()
        self.instrument_manager.connect_instruments()
        try:
            self.instrument_manager.verify_connections()
            print("connection success")
        except ConnectionError as e:
            messagebox.showerror("Instrument Connection Error", str(e))
            self.parent.quit()

    def configure_window(self):
        self.parent.title("PoL Automation V1.0.0")
        self.parent.geometry(WINDOW_SIZE)
        self.parent.resizable(False, False)

    def create_widgets(self):
        self.create_title()
        self.create_status_bar()  # Create status bar before frames
        self.create_frames()

    def create_title(self):
        title = tk.Label(self, text="PoL Automation Test", font=FONT_TITLE, bg='black', fg="white")
        title.pack(fill=tk.X, padx=5, pady=5)

    def create_status_bar(self):
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(self, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_frames(self):
        self.setting_frame = SettingFrame(self, self.instrument_manager)
        self.setting_frame.place(x=20, y=60, width=520, height=1100)  

        self.testing_frame = TestingFrame(self, self.instrument_manager, self.setting_frame)
        self.testing_frame.place(x=550, y=60, width=1400, height=1100)
        
        # Lock the testing frame immediately after creation
        self.lock_testing_frame()
        
    def create_output_tab(self):
        self.testing_frame.create_output_tab()
        
    def unlock_testing_frame(self):
        self.testing_frame.unlock_frame()
        self.status_var.set("Testing frame unlocked")

    def lock_testing_frame(self):
        self.testing_frame.lock_frame()
        self.status_var.set("Testing frame locked")

    def update_status(self, message):
        self.status_var.set(message)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            
            try:
                self.instrument_manager.disconnect_all()
            except Exception as e:
                print(f"Error during disconnect: {e}")  # Debug print
            self.parent.quit()
            self.parent.destroy()
            print("Closing application...")  # Debug print
            os._exit(0)

def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.pack(side="top", fill="both", expand=True)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()