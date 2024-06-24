from tkinter import ttk
from tkinter import *
from tkinter import messagebox 
import re
import pyvisa as visa
from measure_eff_Tek import eff

rm = visa.ResourceManager()

o_scope = []

supply = []

load = []

DAQ = []

meter = []


#from table1 import Ui_Form #display table of all equipment
def update_combobox(combobox_options):
            """
            This function updates the available options in a combobox, 
            removing any duplicates from the provided list. (Inside class)

            Args:
                combobox_options (list): A list of options to set for the combobox.
        
            Returns:
                list: A list of unique options without duplicates.
            """
            # Same logic as the outside function (convert to set, remove duplicates, convert back to list)
            return list(set(combobox_options))
def validate_entry(P):
    """Validates user input in an Entry widget to allow numbers, a single decimal point,
    and leading decimal points.

    Args:
        P (str): The character or string being entered into the Entry widget.

    Returns:
        str: An empty string if the input is valid, or `False` to prevent invalid input.
    """

    if P.isdigit() or (P == '.' and P not in P.get()):
        # Allow digits, a single decimal point (if not already present),
        # and leading decimal points
        return ''
    else:
        return False  # Prevent invalid characters
def find_dev(): # categorize equipment and put them in proper list

    for dev3 in rm.list_resources():



        if dev3.find('USB0') > -1 or dev3.find('GPIB0') > -1: #this is here to not include ASRL3::INSTR

            device_name = rm.open_resource(dev3).query('*IDN?')

        # this is where you add all the look up device

            if device_name.find('E3649A') > -1:

                supply.append(dev3)

            if device_name.find('62012') > -1:

                supply.append(dev3)

            if device_name.find('62006P') > -1:

                supply.append(dev3)

            if device_name.find('N6705C') > -1:

                supply.append(dev3)
                

            if device_name.find('HDO6104A') > -1:

                o_scope.append(dev3)

            if device_name.find('MSO56') > -1:

                o_scope.append(dev3)
                

            if device_name.find('MSO54') > -1:

                o_scope.append(dev3)

            if device_name.find('63600') > -1:

                load.append(dev3)
                

            if device_name.find('34970') > -1:

                DAQ.append(dev3)
                

            if device_name.find('DAQ973') > -1:

                DAQ.append(dev3)
                

            if device_name.find('34461') > -1:

                meter.append(dev3)
class MAIN_MENU:
   

    def __init__(self, root):
        
        self.root = root
        self.root.title("PoL Automation V1.0.0")
        self.root.geometry("2000x1200")  # Set window size
        self.root.resizable(False, False)
        
        self.setting_frame()
        self.testing_frame()
   

    def setting_frame(self):   
        #=============================================Setting FRAME==============================================================
        Setting_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = 'gray')
        Setting_Frame.place(x = 20,y = 20, width = 500,height = 1100)

        Setting__title = Label(Setting_Frame,text = "Setting", font = ("times new roman",25,"bold"), bg = 'black', fg = "white")
        Setting__title.place(relx=0.5, y=40, anchor="center")  
        
        # Instrument_Address_Frame=Frame(Setting_Frame, bd = 4, relief = RIDGE, bg = 'white')
        # Instrument_Address_Frame.place(x = 25,y = 80, width = 450,height = 200)
        # Instrument_Address_Frame__title = Label(Instrument_Address_Frame,text = "Instrument_Address", font = ("times new roman",12,"bold"), bg = 'yellow', fg = "black")
        # Instrument_Address_Frame__title.place(x=5, y=5)  
        
        # Power_Supply__l = Label(Instrument_Address_Frame,text = "Power Supply", font = ("times new roman",12), bg ='white', fg = "black")
        # Power_Supply__l.place(x=5, y=35)  
        
        # DAQ__l = Label(Instrument_Address_Frame,text = "DAQ", font = ("times new roman",12), bg ='white', fg = "black")
        # DAQ__l.place(x=5, y=75)  
        
        # E_load__l = Label(Instrument_Address_Frame,text = "E_load", font = ("times new roman",12), bg ='white', fg = "black")
        # E_load__l.place(x=5, y=115)  
        
        # Oscil__l = Label(Instrument_Address_Frame,text = "Oscilloscope", font = ("times new roman",12), bg ='white', fg = "black")
        # Oscil__l.place(x=5, y=155)  
        
        
        
        Power_Supply_Frame=Frame(Setting_Frame, bd = 4, relief = RIDGE, bg = 'white')
        Power_Supply_Frame.place(x = 25,y = 80, width = 450,height = 200)
        Power_Supply_Frame__title = Label(Power_Supply_Frame,text = "Power_Supply", font = ("times new roman",12,"bold"), bg = 'yellow', fg = "black")
        Power_Supply_Frame__title.place(x=5, y=5)
        Power_Supply_Address = Label(Power_Supply_Frame,text = supply, font = ("times new roman",12,"bold"), bg = 'white', fg = "black")
        Power_Supply_Address.place(x=110, y=5)  
        
        Vin__l = Label(Power_Supply_Frame,text = "Vin(V)", font = ("times new roman",12), bg ='white', fg = "black")
        Vin__l.place(x=5, y=55)  
        Vin = Entry(Power_Supply_Frame, validate="key", validatecommand=(self.root.register(validate_entry), "%P") , font = ("times new roman",15,"bold"), bd = 5,relief=GROOVE)
        Vin.place(x= Vin__l.winfo_width()  + 55, y=55)  
        
        Iin__l = Label(Power_Supply_Frame,text = "Iin(A)", font = ("times new roman",12), bg ='white', fg = "black")
        Iin__l.place(x=5, y=105)
        Iin = Entry(Power_Supply_Frame, validate="key", validatecommand=(self.root.register(validate_entry), "%P") , font = ("times new roman",15,"bold"), bd = 5,relief=GROOVE)
        Iin.place(x= Iin__l.winfo_width()  + 55, y=105)    
        
        PW_CH__l = Label(Power_Supply_Frame,text = "CH", font = ("times new roman",12), bg ='white', fg = "black")
        PW_CH__l.place(x=5, y=155)
        PW_CH = ttk.Combobox(Power_Supply_Frame, width = 10) 
        PW_CH.place(x= Iin__l.winfo_width()  + 55, y=155) 
        # Adding combobox drop down list 
        PW_CH['values'] = (' 1', ' 2',' 3',' 4')  
        
        
        
        
        DAQ_Frame=Frame(Setting_Frame, bd = 4, relief = RIDGE, bg = 'white')
        DAQ_Frame.place(x = 25,y = 300, width = 450,height = 230)
        DAQ_Frame__title = Label(DAQ_Frame,text = "DAQ", font = ("times new roman",12,"bold"), bg = 'yellow', fg = "black")
        DAQ_Frame__title.place(x=5, y=5) 
        DAQ_Address = Label(DAQ_Frame,text = DAQ, font = ("times new roman",12,"bold"), bg = 'white', fg = "black")
        DAQ_Address.place(x=110, y=5)   
        
        
        DAQ_combobox=('input V', 'input I','output V','output I','Vcc','LDO')
        DAQ_options=update_combobox(DAQ_combobox) 
        
        DAQ_CH1__l = Label(DAQ_Frame,text = "CH1", font = ("times new roman",12), bg ='white', fg = "black")
        DAQ_CH1__l.place(x=5, y=35)
        DAQ_CH1 = ttk.Combobox(DAQ_Frame, width = 25) 
        DAQ_CH1.place( x=55, y=35)  
        DAQ_CH1['values'] =   DAQ_combobox 
        
        DAQ_CH2__l = Label(DAQ_Frame,text = "CH2", font = ("times new roman",12), bg ='white', fg = "black")
        DAQ_CH2__l.place(x=5, y=65)
        DAQ_CH2 = ttk.Combobox(DAQ_Frame, width = 25) 
        DAQ_CH2.place( x=55, y=65)  
        DAQ_CH2['values'] = DAQ_combobox   
        
        DAQ_CH3__l = Label(DAQ_Frame,text = "CH3", font = ("times new roman",12), bg ='white', fg = "black")
        DAQ_CH3__l.place(x=5, y=95)
        DAQ_CH3 = ttk.Combobox(DAQ_Frame, width = 25) 
        DAQ_CH3.place( x=55, y=95)  
        DAQ_CH3['values'] = DAQ_combobox 
        
        DAQ_CH4__l = Label(DAQ_Frame,text = "CH4", font = ("times new roman",12), bg ='white', fg = "black")
        DAQ_CH4__l.place(x=5, y=125)
        DAQ_CH4 = ttk.Combobox(DAQ_Frame, width = 25) 
        DAQ_CH4.place( x=55, y=125)  
        DAQ_CH4['values'] = DAQ_combobox   
        
        DAQ_CH5__l = Label(DAQ_Frame,text = "CH5", font = ("times new roman",12), bg ='white', fg = "black")
        DAQ_CH5__l.place(x=5, y=155)
        DAQ_CH5 = ttk.Combobox(DAQ_Frame, width = 25) 
        DAQ_CH5.place( x=55, y=155)  
        DAQ_CH5['values'] = DAQ_combobox  
        
        DAQ_CH6__l = Label(DAQ_Frame,text = "CH6", font = ("times new roman",12), bg ='white', fg = "black")
        DAQ_CH6__l.place(x=5, y=185)
        DAQ_CH6 = ttk.Combobox(DAQ_Frame, width = 25) 
        DAQ_CH6.place( x=55, y=185)   
        DAQ_CH6['values'] = DAQ_combobox   
 
        
        Load_Frame=Frame(Setting_Frame, bd = 4, relief = RIDGE, bg = 'white')
        Load_Frame.place(x = 25,y = 550, width = 450,height = 200)
        Load_Frame__title = Label(Load_Frame,text = "E Load", font = ("times new roman",12,"bold"), bg = 'yellow', fg = "black")
        Load_Frame__title.place(x=5, y=5)       
        Load_Address = Label(Load_Frame,text = load, font = ("times new roman",12,"bold"), bg = 'white', fg = "black")
        Load_Address.place(x=110, y=5) 
        Low_Load__l = Label(Load_Frame,text = "Low Load", font = ("times new roman",12,"bold"), bg ='white', fg = "black")
        Low_Load__l.place(x=90, y=30)
        High_Load__l = Label(Load_Frame,text = "High Load", font = ("times new roman",12,"bold"), bg ='white', fg = "black")
        High_Load__l.place(x=270, y=30)
        Load_Start__l = Label(Load_Frame,text = "Start :", font = ("times new roman",12), bg ='white', fg = "black")
        Load_Start__l.place(x=5, y=60)      
        Load_Step__l = Label(Load_Frame,text = "Step :", font = ("times new roman",12), bg ='white', fg = "black")
        Load_Step__l.place(x=5, y=100)      
        Load_Stop__l = Label(Load_Frame,text = "Stop :", font = ("times new roman",12), bg ='white', fg = "black")
        Load_Stop__l.place(x=5, y=140) 
        
        Low_Load_Start = Entry(Load_Frame, validate="key", validatecommand=(self.root.register(validate_entry), "%P") , font = ("times new roman",12,"bold"), bd = 5,relief=GROOVE,width=10)
        Low_Load_Start.place(x= 90, y=60)  
        Low_Load_Step = Entry(Load_Frame, validate="key", validatecommand=(self.root.register(validate_entry), "%P") , font = ("times new roman",12,"bold"), bd = 5,relief=GROOVE,width=10)
        Low_Load_Step.place(x= 90, y=100)  
        Low_Load_Stop = Entry(Load_Frame, validate="key", validatecommand=(self.root.register(validate_entry), "%P") , font = ("times new roman",12,"bold"), bd = 5,relief=GROOVE,width=10)
        Low_Load_Stop.place(x= 90, y=140)
        High_Load_Start = Entry(Load_Frame, validate="key", validatecommand=(self.root.register(validate_entry), "%P") , font = ("times new roman",12,"bold"), bd = 5,relief=GROOVE,width=10)
        High_Load_Start.place(x= 270, y=60)  
        High_Load_Step = Entry(Load_Frame, validate="key", validatecommand=(self.root.register(validate_entry), "%P") , font = ("times new roman",11,"bold"), bd = 5,relief=GROOVE,width=10)
        High_Load_Step.place(x= 270  , y=100)  
        High_Load_Stop = Entry(Load_Frame, validate="key", validatecommand=(self.root.register(validate_entry), "%P") , font = ("times new roman",12,"bold"), bd = 5,relief=GROOVE,width=10)
        High_Load_Stop.place(x= 270 , y=140)    

        

        Protection_Frame=Frame(Setting_Frame, bd = 4, relief = RIDGE, bg = 'white')
        Protection_Frame.place(x = 25,y = 770, width = 450,height = 200)
        Protection_Frame__title = Label(Protection_Frame,text = "Protection", font = ("times new roman",12,"bold"), bg = 'yellow', fg = "black")
        Protection_Frame__title.place(x=5, y=5)
           
        
        MAX_Vin__l = Label(Protection_Frame,text = "Max Vin(V)", font = ("times new roman",12), bg ='white', fg = "black")
        MAX_Vin__l.place(x=5, y=55)
        MAX_Vin = Entry(Protection_Frame, validate="key", validatecommand=(self.root.register(validate_entry), "%P") , font = ("times new roman",15,"bold"), bd = 5,relief=GROOVE)
        MAX_Vin.place(x= MAX_Vin__l.winfo_width()  + 85, y=55)   
        
        MAX_Iin__l = Label(Protection_Frame,text = "Max Iin(A)", font = ("times new roman",12), bg ='white', fg = "black")
        MAX_Iin__l.place(x=5, y=105)
        MAX_Iin = Entry(Protection_Frame, validate="key", validatecommand=(self.root.register(validate_entry), "%P") , font = ("times new roman",15,"bold"), bd = 5,relief=GROOVE)
        MAX_Iin.place(x= MAX_Iin__l.winfo_width()  + 85, y=105)  

        
        MAX_Iout__l = Label(Protection_Frame,text = "Max Iout(A)", font = ("times new roman",12), bg ='white', fg = "black")
        MAX_Iout__l.place(x=5, y=155)
        
        MAX_Iout = Entry(Protection_Frame, validate="key", validatecommand=(self.root.register(validate_entry), "%P") , font = ("times new roman",15,"bold"), bd = 5,relief=GROOVE)   
        MAX_Iout.place(x= MAX_Iout__l.winfo_width()  + 85, y=155)  
        


        setting_btn_Frame=Frame(Setting_Frame, bd = 4, relief = RIDGE, bg = 'gray',borderwidth=0)
        setting_btn_Frame.place(x = 25,y = 990, width = 450,height = 100)
        
        
        reset_btn = Button(setting_btn_Frame, text="reset", bg='white', fg="black", padx=20, pady=20,
                            font=("Courier New", 12, "bold"), 
                            command=lambda: [Vin.delete(0, END), Iin.delete(0, END),PW_CH.set(""),
                                            DAQ_CH1.set(""),DAQ_CH2.set(""),DAQ_CH3.set(""),DAQ_CH4.set(""),DAQ_CH5.set(""),DAQ_CH6.set(""),
                                            Low_Load_Start.delete(0, END),Low_Load_Step.delete(0, END),Low_Load_Stop.delete(0, END),High_Load_Start.delete(0, END),High_Load_Step.delete(0, END),High_Load_Stop.delete(0, END),
                                            MAX_Vin.delete(0, END), MAX_Iin.delete(0, END),MAX_Iout.delete(0, END)])
        reset_btn.place(x=30,y=15)  
        
        set_btn = Button(setting_btn_Frame, text=" set ",bg='white',fg="black",padx=20,pady=20,font=("Courier New", 12,"bold") ,command=lambda: press_set_btn())
        set_btn.place(x=270,y=15)  # Center relative to frame
        
        def get_entry_value(entry_widget):

                try:
                    value = entry_widget.get()
                    return float(value) if value else 0.0  # Return 0.0 for empty input
                except ValueError:
                # Handle potential conversion errors (e.g., non-numeric input)
                    print(f"Error: Invalid input in '{entry_widget.name}'")
                return 0.0  # Return 0.0 on conversion errors    
            
        def press_set_btn():
            
            Input_v = get_entry_value(Vin)
            Input_I = get_entry_value(Iin)
            Max_input_voltage = get_entry_value(MAX_Vin)  

            Max_input_current = get_entry_value(MAX_Iin)
            Max_load_current =get_entry_value(MAX_Iout)

            Low_load_start = get_entry_value(Low_Load_Start) 
            Low_load_step = get_entry_value(Low_Load_Step) 
            Low_load_stop =get_entry_value(Low_Load_Stop) 

            High_load_start =get_entry_value(High_Load_Start) 
            High_load_step = get_entry_value(High_Load_Step) 
            High_load_stop =get_entry_value(High_Load_Stop) 
            
            if Input_v > Max_input_voltage:
                messagebox.showwarning(title="warning", message="protective maximum input voltage(MAX_Vin) must be at least the Input voltage (Input_V)")
            elif Input_I > Max_input_current:
                messagebox.showwarning(title="warning", message="protective maximum input current(MAX_Iin) must be at least the Input current (Input_I)")
            elif Input_v > 16 or Input_v < 4:
                messagebox.showwarning(title="warning", message="Input voltage (Input_V) range should between 4V~16V")
            elif High_load_start < (Low_load_start or Low_load_stop):
                messagebox.showwarning(title="warning", message="High Load Start Current should not be lower than the Low Load Stop")
            elif Low_load_stop > 20 or High_load_stop>20 or Max_load_current>20:
                messagebox.showwarning(title="warning", message="output current should < 20A")
            elif Low_load_step > (Low_load_stop-Low_load_start):
                messagebox.showwarning(title="warning", message="invalid low load step")
            elif High_load_step > (High_load_stop-High_load_start):
                messagebox.showwarning(title="warning", message="invalid high load step")
            else : 
                messagebox.showinfo("info", "successfully setting!") 
            
           


            

    
    def testing_frame(self):
        #=============================================Test FRAME==============================================================
        Test_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = 'gray')
        Test_Frame.place(x = 550,y = 20, width = 1400, height = 1100)  
          
 

def main():
    find_dev()
    root = Tk()
    main_menu = MAIN_MENU(root)
    root.mainloop()

if __name__ == "__main__":
    main()