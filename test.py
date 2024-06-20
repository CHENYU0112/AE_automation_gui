import tkinter as tk 
import tkinter.ttk as ttk 
  
# initialize the tkinter window 
root = tk.Tk()  
  
# provide some width and height 
root.geometry("300x300")  
  
# created a label frame with title "Group" 
labelframe = ttk.LabelFrame(root, text = "GFG") 
  
# provide padding  
labelframe.pack(padx=30, pady=30)  
  
# created the text label inside the the labelframe 
left = tk.Label(labelframe, text="Geeks for Geeks")  
left.pack() 
  
root.mainloop()