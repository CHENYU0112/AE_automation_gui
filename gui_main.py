from tkinter import ttk
from tkinter import *

class MAIN_MENU:
    def __init__(self, top):
        self.top = top
        self.top.title("PoL Automation V1.0.0")
        self.top.geometry("1000x700")  # Set window size

        # Create left and right frames with explicit width (for reference)
        self.Setting_frame = LabelFrame(top, text="Setting")
        self.Tab_frame = LabelFrame(top, text="Tabs")

        # Use expand=True for older Python versions
        self.Setting_frame.pack(padx=10, pady=10, side=LEFT, fill=Y, expand=True)
        # Optionally comment out the weight line below
        # self.Setting_frame.pack(padx=10, pady=10, side=LEFT, fill=Y, weight=2)  # Not supported in older Python versions

        self.Tab_frame.pack(padx=10, pady=10, side=RIGHT, fill=Y)

        # Add labels to Setting_frame using grid
        voltage_label = Label(self.Setting_frame, text="Vin(V)")
        voltage_label.grid(row=0, column=0)

        current_label = Label(self.Setting_frame, text="lin(A)")
        current_label.grid(row=1, column=0)

        # ... (Add more labels and controls as needed)

# Main program execution
def main():
    root = Tk()
    main_menu = MAIN_MENU(root)
    root.mainloop()

if __name__ == "__main__":
    main()