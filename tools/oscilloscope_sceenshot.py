import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from instrument_manager import InstrumentManager

class ScopeScreenshotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Scope Screenshot Tool")
        master.geometry("1200x700")  # Increased size for larger GUI
        
        # Initialize InstrumentManager
        self.instrument_manager = InstrumentManager()
        
        # Create main frame
        main_frame = ttk.Frame(master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        # Left frame for controls
        left_frame = ttk.Frame(main_frame, padding="10")
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Right frame for image preview
        right_frame = ttk.Frame(main_frame, padding="10")
        right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        # File name input
        ttk.Label(left_frame, text="File Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.file_name_entry = ttk.Entry(left_frame, width=30)
        self.file_name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.file_name_entry.insert(0, "scope_screenshot")
        
        # File path input
        ttk.Label(left_frame, text="Save Path:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.file_path_entry = ttk.Entry(left_frame, width=30)
        self.file_path_entry.grid(row=1, column=1, padx=5, pady=5)
        self.file_path_entry.insert(0, os.path.expanduser("~"))
        
        # Browse button
        self.browse_button = ttk.Button(left_frame, text="Browse", command=self.browse_path)
        self.browse_button.grid(row=1, column=2, padx=5, pady=5)
        
        # Save button
        self.save_button = ttk.Button(left_frame, text="Save Screenshot", command=self.save_screenshot)
        self.save_button.grid(row=2, column=1, pady=10)
        
        # Canvas for image preview
        self.canvas = tk.Canvas(right_frame, width=800, height=600, bg="white")
        self.canvas.pack(expand=True, fill=tk.BOTH)
        
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
            # Save the screenshot
            self.scope.saveimage(full_path)
            
            # Display the saved image in the GUI
            self.display_image(full_path)
            
            messagebox.showinfo("Success", f"Screenshot saved to {full_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save screenshot: {str(e)}")

    def display_image(self, image_path):
        try:
            # Open and resize the image
            image = Image.open(image_path)
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            image.thumbnail((canvas_width, canvas_height))  # Resize image to fit canvas
            photo = ImageTk.PhotoImage(image)
            
            # Update canvas
            self.canvas.delete("all")
            self.canvas.create_image(canvas_width//2, canvas_height//2, anchor=tk.CENTER, image=photo)
            self.canvas.image = photo  # Keep a reference to prevent garbage collection
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display image: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScopeScreenshotGUI(root)
    root.mainloop()