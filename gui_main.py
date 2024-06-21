from tkinter import ttk
from tkinter import *




class MAIN_MENU:
    def __init__(self, root):
        self.root = root
        self.root.title("PoL Automation V1.0.0")
        self.root.geometry("1500x1200")  # Set window size
        self.root.resizable(False, False)
        


        
        #=============================================Setting FRAME==============================================================
        Setting_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = 'gray')
        Setting_Frame.place(x = 20,y = 20, width = 500,height = 1100)

        Setting__title = Label(Setting_Frame,text = "Setting", font = ("times new roman",25,"bold"), bg = 'black', fg = "white")
        Setting__title.place(relx=0.5, y=40, anchor="center")  # Centered horizontally and slightly below the top
        
        Instrument_Address_Frame=Frame(Setting_Frame, bd = 4, relief = RIDGE, bg = 'white')
        Instrument_Address_Frame.place(x = 25,y = 80, width = 450,height = 200)
        Instrument_Address_Frame__title = Label(Instrument_Address_Frame,text = "Instrument_Address", font = ("times new roman",12), bg = 'yellow', fg = "black")
        Instrument_Address_Frame__title.place(x=5, y=5)  # Centered horizontally and slightly below the top

        Power_Supply_Frame=Frame(Setting_Frame, bd = 4, relief = RIDGE, bg = 'white')
        Power_Supply_Frame.place(x = 25,y = 300, width = 450,height = 200)
        Power_Supply_Frame__title = Label(Power_Supply_Frame,text = "Power_Supply", font = ("times new roman",12), bg = 'yellow', fg = "black")
        Power_Supply_Frame__title.place(x=5, y=5)  # Centered horizontally and slightly below the top
        
        DAQ_Frame=Frame(Setting_Frame, bd = 4, relief = RIDGE, bg = 'white')
        DAQ_Frame.place(x = 25,y = 520, width = 450,height = 200)
        DAQ_Frame__title = Label(DAQ_Frame,text = "DAQ", font = ("times new roman",12), bg = 'yellow', fg = "black")
        DAQ_Frame__title.place(x=5, y=5)   # Centered horizontally and slightly below the top 

        Protection_Frame=Frame(Setting_Frame, bd = 4, relief = RIDGE, bg = 'white')
        Protection_Frame.place(x = 25,y = 740, width = 450,height = 200)
        Protection_Frame__title = Label(Protection_Frame,text = "Protection", font = ("times new roman",12), bg = 'yellow', fg = "black")
        Protection_Frame__title.place(x=5, y=5)   # Centered horizontally and slightly below the top    

    
        #=============================================Test FRAME==============================================================
        Test_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = 'gray')
        Test_Frame.place(x = 550,y = 20, width = 900,height = 1100)    


        # ... (Add more labels and controls as needed)

# Main program execution
def main():
    root = Tk()
    main_menu = MAIN_MENU(root)
    root.mainloop()

if __name__ == "__main__":
    main()