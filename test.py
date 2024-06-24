from tkinter import ttk
from tkinter import *
import pyvisa as visa
from measure_eff_Tek import eff
def update_combobox(combobox_options, selected_value):
  """
  This function removes the selected value from the provided options list 
  and returns the updated list.

  Args:
      combobox_options (list): The original list of options.
      selected_value (str): The value to be removed.

  Returns:
      list: The updated list of options without the selected value.
  """
  if selected_value in combobox_options:
    combobox_options.remove(selected_value)
  return combobox_options

# Initial options for the comboboxes
DAQ_combobox = ('input V', 'input I', 'output V', 'output I', 'Vcc', 'LDO')

# Create the main window
root = Tk()
root.title("Comboboxes with Shared Options")

# Create a frame to hold the labels and comboboxes
daq_frame = tk.Frame(root)
daq_frame.pack(padx=10, pady=10)

# Create six comboboxes and labels
channel_labels = ("CH1", "CH2", "CH3", "CH4", "CH5", "CH6")
comboboxes = []
for i in enumerate(DAQ_combobox):

  DAQ['values'] = DAQ_combobox.copy()  # Copy the original list to avoid modification
  
  comboboxes.append(combobox)  # Store comboboxes in a list

  # Bind a function to update other comboboxes on selection change
  def update_other_comboboxes(event, combobox=combobox, other_comboboxes=comboboxes.copy()):
    # Remove the selected value from the copy of the original list
    updated_options = update_combobox(DAQ_combobox.copy(), combobox.get())

    # Update the options for all other comboboxes (excluding the current one)
    for other_combobox in other_comboboxes:
      if other_combobox != combobox:
        other_combobox['values'] = updated_options

  combobox.bind("<<ComboboxSelected>>", update_other_comboboxes)

# Start the main event loop
root.mainloop()