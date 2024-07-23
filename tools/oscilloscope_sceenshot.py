import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from instrument_manager import InstrumentManager

class ScopeScreenshotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Scope Screenshot Tool")
        master.geometry("400x200")

        # Initialize InstrumentManager
        self.instrument_manager = InstrumentManager()

        # File name input
        tk.Label(master, text="File Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.file_name_entry = tk.Entry(master, width=30)
        self.file_name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.file_name_entry.insert(0, "scope_screenshot")

        # File path input
        tk.Label(master, text="Save Path:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.file_path_entry = tk.Entry(master, width=30)
        self.file_path_entry.grid(row=1, column=1, padx=5, pady=5)
        self.file_path_entry.insert(0, os.path.expanduser("~"))

        # Browse button
        self.browse_button = tk.Button(master, text="Browse", command=self.browse_path)
        self.browse_button.grid(row=1, column=2, padx=5, pady=5)

        # Save button
        self.save_button = tk.Button(master, text="Save Screenshot", command=self.save_screenshot)
        self.save_button.grid(row=2, column=1, pady=20)

        # Initialize oscilloscope
        self.init_oscilloscope()

    def init_oscilloscope(self):
        try:
            self.instrument_manager.find_devices()
            initialized_instruments = self.instrument_manager.initialize_instruments()
            self.scope = initialized_instruments.get('o_scope')
            if not self.scope:
                raise Exception("Oscilloscope not found or initialized")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize oscilloscope: {str(e)}")
            self.scope = None

    def browse_path(self):
        path = filedialog.askdirectory()
        if path:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(0, path)

    def save_screenshot(self):
        if not self.scope:
            messagebox.showerror("Error", "Oscilloscope not initialized")
            return

        file_name = self.file_name_entry.get()
        file_path = self.file_path_entry.get()
        
        if not file_name or not file_path:
            messagebox.showerror("Error", "Please provide both file name and path")
            return

        full_path = os.path.join(file_path, f"{file_name}.png")

        try:
            self.scope.saveimage(full_path)
            messagebox.showinfo("Success", f"Screenshot saved to {full_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save screenshot: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScopeScreenshotGUI(root)
    root.mainloop()