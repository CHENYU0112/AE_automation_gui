

import pyvisa as visa

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMessageBox

from measure_eff_Tek import eff

rm = visa.ResourceManager()

o_scope = []

supply = []

load = []

DAQ = []

meter = []

#from table1 import Ui_Form #display table of all equipment


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

class Ui_DCDC_Efficiency(object):

    def openWindow(self): #this method calls the table list of all equipment

        self.Form = QtWidgets.QWidget()

        self.ug = Ui_Form()

        self.ug.setupUi(self.Form)

        self.Form.show()

    def setup_dc_input(self):
    
        self.DC_Input_label_main = QtWidgets.QGroupBox(self.centralwidget)

        self.DC_Input_label_main.setGeometry(QtCore.QRect(310, 0, 291, 81))

        font = QtGui.QFont()

        font.setPointSize(12)

        font.setBold(True)

        font.setWeight(75)

        self.DC_Input_label_main.setFont(font)

        self.DC_Input_label_main.setAutoFillBackground(False)

        self.DC_Input_label_main.setStyleSheet("background-color: rgb(228, 255, 226);")

        self.DC_Input_label_main.setFlat(False)

        self.DC_Input_label_main.setCheckable(False)

        self.DC_Input_label_main.setObjectName("DC_Input_label_main")
    

        self.input_V_label = QtWidgets.QLabel(self.DC_Input_label_main)

        self.input_V_label.setGeometry(QtCore.QRect(10, 20, 61, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.input_V_label.setFont(font)

        self.input_V_label.setMouseTracking(True)

        self.input_V_label.setAutoFillBackground(False)

        self.input_V_label.setTextFormat(QtCore.Qt.AutoText)

        self.input_V_label.setObjectName("input_V_label")
    
    

        self.input_V = QtWidgets.QLineEdit(self.DC_Input_label_main)

        self.input_V.setGeometry(QtCore.QRect(10, 50, 71, 20))

        self.input_V.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.input_V.setObjectName("input_V")

        self.input_V.setText("12")  # set the default input voltage value *******************************
    
    

        self.input_Current_label = QtWidgets.QLabel(self.DC_Input_label_main)

        self.input_Current_label.setGeometry(QtCore.QRect(110, 20, 41, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.input_Current_label.setFont(font)

        self.input_Current_label.setMouseTracking(True)

        self.input_Current_label.setAutoFillBackground(False)

        self.input_Current_label.setTextFormat(QtCore.Qt.AutoText)

        self.input_Current_label.setObjectName("input_Current_label")
    
    

        self.input_Current = QtWidgets.QLineEdit(self.DC_Input_label_main)

        self.input_Current.setGeometry(QtCore.QRect(110, 50, 71, 20))

        self.input_Current.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.input_Current.setObjectName("input_Current")

        self.input_Current.setText("4")  # set the default input current value *******************************  

    def setup_protection(self):
    ## protection_label_main
        self.protection_label_main = QtWidgets.QGroupBox(self.centralwidget)

        self.protection_label_main.setGeometry(QtCore.QRect(310, 90, 291, 81))

        font = QtGui.QFont()

        font.setPointSize(12)

        font.setBold(True)

        font.setWeight(75)

        self.protection_label_main.setFont(font)

        self.protection_label_main.setAutoFillBackground(False)

        self.protection_label_main.setStyleSheet("background-color: rgb(228, 255, 226);")

        self.protection_label_main.setFlat(False)

        self.protection_label_main.setCheckable(False)

        self.protection_label_main.setObjectName("protection_label_main")


        ## input_Max_Voltage_label 
        self.input_Max_Voltage_label = QtWidgets.QLabel(self.protection_label_main)

        self.input_Max_Voltage_label.setGeometry(QtCore.QRect(10, 20, 61, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.input_Max_Voltage_label.setFont(font)

        self.input_Max_Voltage_label.setMouseTracking(True)

        self.input_Max_Voltage_label.setAutoFillBackground(False)

        self.input_Max_Voltage_label.setTextFormat(QtCore.Qt.AutoText)

        self.input_Max_Voltage_label.setObjectName("input_Max_Voltage_label")
        
        
        ## input_Max_Voltage 
        self.input_Max_Voltage = QtWidgets.QLineEdit(self.protection_label_main)

        self.input_Max_Voltage.setGeometry(QtCore.QRect(10, 50, 71, 20))

        self.input_Max_Voltage.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.input_Max_Voltage.setObjectName("input_Max_Voltage")

        self.input_Max_Voltage.setText("60")  # set the default input max voltage value ******************************
        
        
        ## input_Max_Current_label 
        self.input_Max_Current_label = QtWidgets.QLabel(self.protection_label_main)

        self.input_Max_Current_label.setGeometry(QtCore.QRect(110, 20, 61, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.input_Max_Current_label.setFont(font)

        self.input_Max_Current_label.setMouseTracking(True)

        self.input_Max_Current_label.setAutoFillBackground(False)

        self.input_Max_Current_label.setTextFormat(QtCore.Qt.AutoText)

        self.input_Max_Current_label.setObjectName("input_Max_Current_label")
        
        ## input_Max_Current
        self.input_Max_Current = QtWidgets.QLineEdit(self.protection_label_main)

        self.input_Max_Current.setGeometry(QtCore.QRect(110, 50, 71, 20))

        self.input_Max_Current.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.input_Max_Current.setObjectName("input_Max_Current")

        self.input_Max_Current.setText("5")  # set the default input max current value *******************************

        
        ## output_Max_Current_label 
        self.output_Max_Current_label = QtWidgets.QLabel(self.protection_label_main)

        self.output_Max_Current_label.setGeometry(QtCore.QRect(200, 20, 81, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.output_Max_Current_label.setFont(font)

        self.output_Max_Current_label.setMouseTracking(True)

        self.output_Max_Current_label.setAutoFillBackground(False)

        self.output_Max_Current_label.setTextFormat(QtCore.Qt.AutoText)

        self.output_Max_Current_label.setObjectName("output_Max_Current_label")

    ## output_Max_Current
        self.output_Max_Current = QtWidgets.QLineEdit(self.protection_label_main)

        self.output_Max_Current.setGeometry(QtCore.QRect(200, 50, 71, 20))

        self.output_Max_Current.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.output_Max_Current.setObjectName("output_Max_Current")

        self.output_Max_Current.setText("10")  # set the default output max current value *******************************
    
    def setup_load_range(self):
        
        self.Load_Range_Label = QtWidgets.QGroupBox(self.centralwidget)

        self.Load_Range_Label.setGeometry(QtCore.QRect(30, 370, 571, 101))

        font = QtGui.QFont()

        font.setPointSize(12)

        font.setBold(True)

        font.setWeight(75)

        self.Load_Range_Label.setFont(font)

        self.Load_Range_Label.setAutoFillBackground(False)

        self.Load_Range_Label.setStyleSheet("background-color: rgb(228, 255, 226);")

        self.Load_Range_Label.setFlat(False)

        self.Load_Range_Label.setCheckable(False)

        self.Load_Range_Label.setObjectName("Load_Range_Label")

        self.Low_load_start_label = QtWidgets.QLabel(self.Load_Range_Label)

        self.Low_load_start_label.setGeometry(QtCore.QRect(10, 20, 91, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.Low_load_start_label.setFont(font)

        self.Low_load_start_label.setMouseTracking(True)

        self.Low_load_start_label.setAutoFillBackground(False)

        self.Low_load_start_label.setTextFormat(QtCore.Qt.AutoText)

        self.Low_load_start_label.setObjectName("Low_load_start_label")

        self.Low_load_start = QtWidgets.QLineEdit(self.Load_Range_Label)

        self.Low_load_start.setGeometry(QtCore.QRect(10, 50, 71, 20))

        self.Low_load_start.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.Low_load_start.setObjectName("Low_load_start")

        self.Low_load_start.setText("0")  # set the default low load start value *******************************

        self.Low_load_step_label = QtWidgets.QLabel(self.Load_Range_Label)

        self.Low_load_step_label.setGeometry(QtCore.QRect(110, 20, 101, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.Low_load_step_label.setFont(font)

        self.Low_load_step_label.setMouseTracking(True)

        self.Low_load_step_label.setAutoFillBackground(False)

        self.Low_load_step_label.setTextFormat(QtCore.Qt.AutoText)

        self.Low_load_step_label.setObjectName("Low_load_step_label")

        self.Low_load_stop_label = QtWidgets.QLabel(self.Load_Range_Label)

        self.Low_load_stop_label.setGeometry(QtCore.QRect(210, 20, 81, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.Low_load_stop_label.setFont(font)

        self.Low_load_stop_label.setMouseTracking(True)

        self.Low_load_stop_label.setAutoFillBackground(False)

        self.Low_load_stop_label.setTextFormat(QtCore.Qt.AutoText)

        self.Low_load_stop_label.setObjectName("Low_load_stop_label")

        self.High_load_stop_label = QtWidgets.QLabel(self.Load_Range_Label)

        self.High_load_stop_label.setGeometry(QtCore.QRect(310, 20, 91, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.High_load_stop_label.setFont(font)

        self.High_load_stop_label.setMouseTracking(True)

        self.High_load_stop_label.setAutoFillBackground(False)

        self.High_load_stop_label.setTextFormat(QtCore.Qt.AutoText)

        self.High_load_stop_label.setObjectName("High_load_stop_label")

        self.High_load_step_label = QtWidgets.QLabel(self.Load_Range_Label)

        self.High_load_step_label.setGeometry(QtCore.QRect(410, 20, 91, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.High_load_step_label.setFont(font)

        self.High_load_step_label.setMouseTracking(True)

        self.High_load_step_label.setAutoFillBackground(False)

        self.High_load_step_label.setTextFormat(QtCore.Qt.AutoText)

        self.High_load_step_label.setObjectName("High_load_step_label")

        self.Low_load_step = QtWidgets.QLineEdit(self.Load_Range_Label)

        self.Low_load_step.setGeometry(QtCore.QRect(110, 50, 71, 20))

        self.Low_load_step.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.Low_load_step.setObjectName("Low_load_step")

        self.Low_load_step.setText("0.01")  # set the default low load step value *******************************

        self.Low_load_stop = QtWidgets.QLineEdit(self.Load_Range_Label)

        self.Low_load_stop.setGeometry(QtCore.QRect(210, 50, 71, 20))

        self.Low_load_stop.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.Low_load_stop.setObjectName("Low_load_stop")

        self.Low_load_stop.setText("0.1")  # set the default low load stop value *******************************

        self.High_load_stop = QtWidgets.QLineEdit(self.Load_Range_Label)

        self.High_load_stop.setGeometry(QtCore.QRect(310, 50, 71, 20))

        self.High_load_stop.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.High_load_stop.setObjectName("High_load_stop")

        self.High_load_stop.setText("0.5")  # set the default high load stop value *******************************

        self.High_load_step = QtWidgets.QLineEdit(self.Load_Range_Label)

        self.High_load_step.setGeometry(QtCore.QRect(410, 50, 71, 20))

        self.High_load_step.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.High_load_step.setObjectName("High_load_step")

        self.High_load_step.setText("0.05")  # set the default high load step value *******************************

    def setup_output_file(self):
        self.output_file_label_main = QtWidgets.QGroupBox(self.centralwidget)

        self.output_file_label_main.setGeometry(QtCore.QRect(310, 180, 291, 81))

        font = QtGui.QFont()

        font.setPointSize(12)

        font.setBold(True)

        font.setWeight(75)

        self.output_file_label_main.setFont(font)

        self.output_file_label_main.setAutoFillBackground(False)

        self.output_file_label_main.setStyleSheet("background-color: rgb(228, 255, 226);")

        self.output_file_label_main.setFlat(False)

        self.output_file_label_main.setCheckable(False)

        self.output_file_label_main.setObjectName("output_file_label_main")

        self.output_file_label = QtWidgets.QLabel(self.output_file_label_main)

        self.output_file_label.setGeometry(QtCore.QRect(10, 20, 111, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.output_file_label.setFont(font)

        self.output_file_label.setMouseTracking(True)

        self.output_file_label.setAutoFillBackground(False)

        self.output_file_label.setTextFormat(QtCore.Qt.AutoText)

        self.output_file_label.setObjectName("output_file_label")

        self.output_file_name = QtWidgets.QLineEdit(self.output_file_label_main)

        self.output_file_name.setGeometry(QtCore.QRect(10, 50, 231, 20))

        self.output_file_name.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.output_file_name.setObjectName("output_file_name")

        self.output_file_name.setText("change_name _here")  # set the default output file name *************************
    
    def setup_instrument_address(self):
        self.Instr_Add_Label_main = QtWidgets.QGroupBox(self.centralwidget)

        self.Instr_Add_Label_main.setGeometry(QtCore.QRect(30, 0, 251, 361))

        font = QtGui.QFont()

        font.setPointSize(12)

        font.setBold(True)

        font.setWeight(75)

        self.Instr_Add_Label_main.setFont(font)

        self.Instr_Add_Label_main.setAutoFillBackground(False)

        self.Instr_Add_Label_main.setStyleSheet("background-color: rgb(228, 255, 226);")

        self.Instr_Add_Label_main.setFlat(False)

        self.Instr_Add_Label_main.setCheckable(False)

        self.Instr_Add_Label_main.setObjectName("Instr_Add_Label_main") #*********

        #self.DC_sup_add_label = QtWidgets.QGroupBox(self.Instr_Add_Label_main)
        

        self.DC_sup_add_label = QtWidgets.QLabel(self.Instr_Add_Label_main)

        self.DC_sup_add_label.setGeometry(QtCore.QRect(10, 20, 200, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.DC_sup_add_label.setFont(font)

        self.DC_sup_add_label.setMouseTracking(True)

        self.DC_sup_add_label.setAutoFillBackground(False)

        self.DC_sup_add_label.setTextFormat(QtCore.Qt.AutoText)

        self.DC_sup_add_label.setObjectName("DC_sup_add_label")

        #self.DC_sup_add = QtWidgets.QLineEdit(self.Instr_Add_Label_main)



        self.DC_sup_add = QtWidgets.QComboBox(self.Instr_Add_Label_main) #xxxxx add drop down box

        #self.DC_sup_add = QtWidgets.QComboBox(self.DC_sup_add_label)  # xxxxx add drop down box

        self.DC_sup_add.setGeometry(QtCore.QRect(10, 50, 231, 20))

        self.DC_sup_add.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.DC_sup_add.setObjectName("DC_sup_add")

        self.DC_sup_add.addItem("") #xxxxx the amount of these "addItem" lines dictate the amount of drop down

        self.DC_sup_add.addItem("")  # xxxx

        self.DC_sup_add.addItem("")  # xxxx

        self.DC_sup_add.addItem("")  # xxxx

        self.DC_sup_add.addItem("")  # xxxx

        self.DC_sup_add.addItem("")  # xxxx

        self.DC_sup_add.addItem("")  # xxxx

        self.DC_sup_add.addItem("")  # xxxx

        self.DC_sup_add.addItem("")  # xxxx

        self.DC_sup_add.addItem("")  # xxxx

        self.DC_sup_add.addItem("")  # xxxx



        #self.DC_sup_add.setText("01")  # set the default DC supply GPIB address *******************************

        self.data_logger_add_label = QtWidgets.QLabel(self.Instr_Add_Label_main)

        self.data_logger_add_label.setGeometry(QtCore.QRect(10, 80, 200, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.data_logger_add_label.setFont(font)

        self.data_logger_add_label.setMouseTracking(True)

        self.data_logger_add_label.setAutoFillBackground(False)

        self.data_logger_add_label.setTextFormat(QtCore.Qt.AutoText)

        self.data_logger_add_label.setObjectName("data_logger_add_label")

        self.E_load_address_label = QtWidgets.QLabel(self.Instr_Add_Label_main)

        self.E_load_address_label.setGeometry(QtCore.QRect(10, 140, 200, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.E_load_address_label.setFont(font)

        self.E_load_address_label.setMouseTracking(True)

        self.E_load_address_label.setAutoFillBackground(False)

        self.E_load_address_label.setTextFormat(QtCore.Qt.AutoText)

        self.E_load_address_label.setObjectName("E_load_address_label")

        #self.E_load_address = QtWidgets.QLineEdit(self.Instr_Add_Label_main)



        self.E_load_address = QtWidgets.QComboBox(self.Instr_Add_Label_main) #xxxxx add drop down box

        self.E_load_address.setGeometry(QtCore.QRect(10, 170, 231, 20))

        self.E_load_address.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.E_load_address.setObjectName("E_load_address")

        self.E_load_address.addItem("")  # xxxx

        self.E_load_address.addItem("")  # xxxx

        self.E_load_address.addItem("")  # xxxx

        self.E_load_address.addItem("")  # xxxx

        self.E_load_address.addItem("")  # xxxx

        self.E_load_address.addItem("")  # xxxx

        self.E_load_address.addItem("")  # xxxx

        self.E_load_address.addItem("")  # xxxx

        self.E_load_address.addItem("")  # xxxx

        #self.E_load_address.setText("07")  # set the default electronic load GPIB address ******************************





        #self.data_logger_add = QtWidgets.QLineEdit(self.Instr_Add_Label_main)

        self.data_logger_add = QtWidgets.QComboBox(self.Instr_Add_Label_main) #xxxxx add drop down box

        self.data_logger_add.setGeometry(QtCore.QRect(10, 110, 231, 20))

        self.data_logger_add.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.data_logger_add.setObjectName("data_logger_add")

        self.data_logger_add.addItem("")  # xxxx

        self.data_logger_add.addItem("")  # xxxx

        self.data_logger_add.addItem("")  # xxxx

        self.data_logger_add.addItem("")  # xxxx

        self.data_logger_add.addItem("")  # xxxx

        self.data_logger_add.addItem("")  # xxxx

        self.data_logger_add.addItem("")  # xxxx

        #self.data_logger_add.setText("09")  # set the default data logger GPIB address *******************************





        self.Renesas_label = QtWidgets.QLabel(self.Instr_Add_Label_main)

        self.Renesas_label.setGeometry(QtCore.QRect(10, 280, 231, 41))

        self.Renesas_label.setText("")

        #self.Renesas_label.setPixmap(QtGui.QPixmap("../../../../../Renesas_symbol_2.PNG"))

        self.Renesas_label.setPixmap(QtGui.QPixmap("C:/Users/nyakamna/Desktop/Newey/Python/Nprogram/dcdc_eff/Renesas_symbol_2.PNG"))

        self.Renesas_label.setObjectName("Renesas_label")

        self.lecroy_USB_address_label = QtWidgets.QLabel(self.Instr_Add_Label_main)

        self.lecroy_USB_address_label.setGeometry(QtCore.QRect(10, 200, 151, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.lecroy_USB_address_label.setFont(font)

        self.lecroy_USB_address_label.setMouseTracking(True)

        self.lecroy_USB_address_label.setAutoFillBackground(False)

        self.lecroy_USB_address_label.setTextFormat(QtCore.Qt.AutoText)

        self.lecroy_USB_address_label.setObjectName("lecroy_USB_address_label")



        #self.lecroy_USB_address = QtWidgets.QLineEdit(self.Instr_Add_Label_main)

        self.lecroy_USB_address = QtWidgets.QComboBox(self.Instr_Add_Label_main) #xxxxx add drop down box

        self.lecroy_USB_address.setGeometry(QtCore.QRect(10, 230, 231, 20))

        self.lecroy_USB_address.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.lecroy_USB_address.setObjectName("lecroy_USB_address")

        self.lecroy_USB_address.addItem("")  # xxxx

        self.lecroy_USB_address.addItem("")  # xxxx

        self.lecroy_USB_address.addItem("")  # xxxx

        self.lecroy_USB_address.addItem("")  # xxxx

        self.lecroy_USB_address.addItem("")  # xxxx

        self.lecroy_USB_address.addItem("")  # xxxx

        self.lecroy_USB_address.addItem("")  # xxxx

        self.lecroy_USB_address.addItem("")  # xxxx

        self.lecroy_USB_address.addItem("")  # xxxx

        self.lecroy_USB_address.addItem("")  # xxxx

        #self.lecroy_USB_address.setText("0x05FF::0x1023::3566N52362")  # set the default lecroy scope USB address ******
    
    def setup_delay_time(self):
        self.delay_time_label_main = QtWidgets.QGroupBox(self.centralwidget)

        self.delay_time_label_main.setGeometry(QtCore.QRect(310, 270, 291, 91))

        font = QtGui.QFont()

        font.setPointSize(12)

        font.setBold(True)

        font.setWeight(75)

        self.delay_time_label_main.setFont(font)

        self.delay_time_label_main.setAutoFillBackground(False)

        self.delay_time_label_main.setStyleSheet("background-color: rgb(228, 255, 226);")

        self.delay_time_label_main.setFlat(False)

        self.delay_time_label_main.setCheckable(False)

        self.delay_time_label_main.setObjectName("delay_time_label_main")

        self.low_load_delay_time_label = QtWidgets.QLabel(self.delay_time_label_main)

        self.low_load_delay_time_label.setGeometry(QtCore.QRect(10, 20, 121, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.low_load_delay_time_label.setFont(font)

        self.low_load_delay_time_label.setMouseTracking(True)

        self.low_load_delay_time_label.setAutoFillBackground(False)

        self.low_load_delay_time_label.setTextFormat(QtCore.Qt.AutoText)

        self.low_load_delay_time_label.setObjectName("low_load_delay_time_label")

        self.low_load_delay_time = QtWidgets.QLineEdit(self.delay_time_label_main)

        self.low_load_delay_time.setGeometry(QtCore.QRect(10, 50, 121, 20))

        self.low_load_delay_time.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.low_load_delay_time.setObjectName("low_load_delay_time")

        self.low_load_delay_time.setText("3")  # set the default low load setting delay prior to taking measurement*****

        self.high_load_delay_time_label = QtWidgets.QLabel(self.delay_time_label_main)

        self.high_load_delay_time_label.setGeometry(QtCore.QRect(160, 20, 121, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.high_load_delay_time_label.setFont(font)

        self.high_load_delay_time_label.setMouseTracking(True)

        self.high_load_delay_time_label.setAutoFillBackground(False)

        self.high_load_delay_time_label.setTextFormat(QtCore.Qt.AutoText)

        self.high_load_delay_time_label.setObjectName("high_load_delay_time_label")

        self.high_load_delay_time = QtWidgets.QLineEdit(self.delay_time_label_main)

        self.high_load_delay_time.setGeometry(QtCore.QRect(160, 50, 121, 20))

        self.high_load_delay_time.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.high_load_delay_time.setObjectName("high_load_delay_time")

        self.high_load_delay_time.setText("3")  # set the default high load setting delay prior to taking measurement****
    
    def setup_current_shunt(self):
        self.Current_shunt_settings_label_main = QtWidgets.QGroupBox(self.centralwidget)

        self.Current_shunt_settings_label_main.setGeometry(QtCore.QRect(30, 480, 571, 101))

        font = QtGui.QFont()

        font.setPointSize(12)

        font.setBold(True)

        font.setWeight(75)

        self.Current_shunt_settings_label_main.setFont(font)

        self.Current_shunt_settings_label_main.setAutoFillBackground(False)

        self.Current_shunt_settings_label_main.setStyleSheet("background-color: rgb(228, 255, 226);")

        self.Current_shunt_settings_label_main.setFlat(False)

        self.Current_shunt_settings_label_main.setCheckable(False)

        self.Current_shunt_settings_label_main.setObjectName("Current_shunt_settings_label_main")

        self.Input_shunt_max_v_label = QtWidgets.QLabel(self.Current_shunt_settings_label_main)

        self.Input_shunt_max_v_label.setGeometry(QtCore.QRect(10, 20, 111, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.Input_shunt_max_v_label.setFont(font)

        self.Input_shunt_max_v_label.setMouseTracking(True)

        self.Input_shunt_max_v_label.setAutoFillBackground(False)

        self.Input_shunt_max_v_label.setTextFormat(QtCore.Qt.AutoText)

        self.Input_shunt_max_v_label.setObjectName("Input_shunt_max_v_label")

        self.Input_shunt_max_v = QtWidgets.QLineEdit(self.Current_shunt_settings_label_main)

        self.Input_shunt_max_v.setGeometry(QtCore.QRect(10, 50, 91, 20))

        self.Input_shunt_max_v.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.Input_shunt_max_v.setObjectName("Input_shunt_max_v")

        self.Input_shunt_max_v.setText("0.1")  # set the default input shunt resistor max voltage value ****************

        self.Input_shunt_max_i_label = QtWidgets.QLabel(self.Current_shunt_settings_label_main)

        self.Input_shunt_max_i_label.setGeometry(QtCore.QRect(140, 20, 101, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.Input_shunt_max_i_label.setFont(font)

        self.Input_shunt_max_i_label.setMouseTracking(True)

        self.Input_shunt_max_i_label.setAutoFillBackground(False)

        self.Input_shunt_max_i_label.setTextFormat(QtCore.Qt.AutoText)

        self.Input_shunt_max_i_label.setObjectName("Input_shunt_max_i_label")

        self.Output_shunt_max_v_label = QtWidgets.QLabel(self.Current_shunt_settings_label_main)

        self.Output_shunt_max_v_label.setGeometry(QtCore.QRect(280, 20, 121, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.Output_shunt_max_v_label.setFont(font)

        self.Output_shunt_max_v_label.setMouseTracking(True)

        self.Output_shunt_max_v_label.setAutoFillBackground(False)

        self.Output_shunt_max_v_label.setTextFormat(QtCore.Qt.AutoText)

        self.Output_shunt_max_v_label.setObjectName("Output_shunt_max_v_label")

        self.Output_shunt_max_i_label = QtWidgets.QLabel(self.Current_shunt_settings_label_main)

        self.Output_shunt_max_i_label.setGeometry(QtCore.QRect(420, 20, 111, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.Output_shunt_max_i_label.setFont(font)

        self.Output_shunt_max_i_label.setMouseTracking(True)

        self.Output_shunt_max_i_label.setAutoFillBackground(False)

        self.Output_shunt_max_i_label.setTextFormat(QtCore.Qt.AutoText)

        self.Output_shunt_max_i_label.setObjectName("Output_shunt_max_i_label")

        self.Input_shunt_max_i = QtWidgets.QLineEdit(self.Current_shunt_settings_label_main)

        self.Input_shunt_max_i.setGeometry(QtCore.QRect(140, 50, 101, 20))

        self.Input_shunt_max_i.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.Input_shunt_max_i.setObjectName("Input_shunt_max_i")

        self.Input_shunt_max_i.setText("10")  # set the default input shunt resistor max current value ******************

        self.Output_shunt_max_v = QtWidgets.QLineEdit(self.Current_shunt_settings_label_main)

        self.Output_shunt_max_v.setGeometry(QtCore.QRect(280, 50, 101, 20))

        self.Output_shunt_max_v.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.Output_shunt_max_v.setObjectName("Output_shunt_max_v")

        self.Output_shunt_max_v.setText("0.1")  # set the default output shunt resistor max voltage value **************

        self.Output_shunt_max_i = QtWidgets.QLineEdit(self.Current_shunt_settings_label_main)

        self.Output_shunt_max_i.setGeometry(QtCore.QRect(420, 50, 101, 20))

        self.Output_shunt_max_i.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.Output_shunt_max_i.setObjectName("Output_shunt_max_i")

        self.Output_shunt_max_i.setText("20")  # set the default output shunt resistor max current value ***************
    
    def setup_data_logger(self):
        self.Data_logger_ch_label_main = QtWidgets.QGroupBox(self.centralwidget)

        self.Data_logger_ch_label_main.setGeometry(QtCore.QRect(30, 590, 571, 101))

        font = QtGui.QFont()

        font.setPointSize(12)

        font.setBold(True)

        font.setWeight(75)

        self.Data_logger_ch_label_main.setFont(font)

        self.Data_logger_ch_label_main.setAutoFillBackground(False)

        self.Data_logger_ch_label_main.setStyleSheet("background-color: rgb(228, 255, 226);")

        self.Data_logger_ch_label_main.setFlat(False)

        self.Data_logger_ch_label_main.setCheckable(False)

        self.Data_logger_ch_label_main.setObjectName("Data_logger_ch_label_main")

        self.input_v_ch_label = QtWidgets.QLabel(self.Data_logger_ch_label_main)

        self.input_v_ch_label.setGeometry(QtCore.QRect(10, 20, 91, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.input_v_ch_label.setFont(font)

        self.input_v_ch_label.setMouseTracking(True)

        self.input_v_ch_label.setAutoFillBackground(False)

        self.input_v_ch_label.setTextFormat(QtCore.Qt.AutoText)

        self.input_v_ch_label.setObjectName("input_v_ch_label")

        self.input_v_ch_1 = QtWidgets.QLineEdit(self.Data_logger_ch_label_main)

        self.input_v_ch_1.setGeometry(QtCore.QRect(10, 50, 71, 20))

        self.input_v_ch_1.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.input_v_ch_1.setObjectName("input_v_ch_1")

        self.input_v_ch_1.setText("101")  # set the default input voltage channel ***************

        self.input_i_ch_label = QtWidgets.QLabel(self.Data_logger_ch_label_main)

        self.input_i_ch_label.setGeometry(QtCore.QRect(110, 20, 101, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.input_i_ch_label.setFont(font)

        self.input_i_ch_label.setMouseTracking(True)

        self.input_i_ch_label.setAutoFillBackground(False)

        self.input_i_ch_label.setTextFormat(QtCore.Qt.AutoText)

        self.input_i_ch_label.setObjectName("input_i_ch_label")

        self.output_v_ch_label = QtWidgets.QLabel(self.Data_logger_ch_label_main)

        self.output_v_ch_label.setGeometry(QtCore.QRect(210, 20, 91, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.output_v_ch_label.setFont(font)

        self.output_v_ch_label.setMouseTracking(True)

        self.output_v_ch_label.setAutoFillBackground(False)

        self.output_v_ch_label.setTextFormat(QtCore.Qt.AutoText)

        self.output_v_ch_label.setObjectName("output_v_ch_label")

        self.output_i_ch_label = QtWidgets.QLabel(self.Data_logger_ch_label_main)

        self.output_i_ch_label.setGeometry(QtCore.QRect(310, 20, 91, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.output_i_ch_label.setFont(font)

        self.output_i_ch_label.setMouseTracking(True)

        self.output_i_ch_label.setAutoFillBackground(False)

        self.output_i_ch_label.setTextFormat(QtCore.Qt.AutoText)

        self.output_i_ch_label.setObjectName("output_i_ch_label")



        self.ldo_ch_label = QtWidgets.QLabel(self.Data_logger_ch_label_main)

        self.ldo_ch_label.setGeometry(QtCore.QRect(510, 20, 91, 41))

        self.ldo_ch_label.setFont(font)

        self.ldo_ch_label.setMouseTracking(True)

        self.ldo_ch_label.setAutoFillBackground(False)

        self.ldo_ch_label.setTextFormat(QtCore.Qt.AutoText)

        self.ldo_ch_label.setObjectName("LDO_ch_label")



        self.vcc_ch_label = QtWidgets.QLabel(self.Data_logger_ch_label_main)

        self.vcc_ch_label.setGeometry(QtCore.QRect(410, 20, 91, 41))

        font = QtGui.QFont()

        font.setPointSize(8)

        font.setBold(True)

        font.setWeight(75)

        self.vcc_ch_label.setFont(font)

        self.vcc_ch_label.setMouseTracking(True)

        self.vcc_ch_label.setAutoFillBackground(False)

        self.vcc_ch_label.setTextFormat(QtCore.Qt.AutoText)

        self.vcc_ch_label.setObjectName("vcc_ch_label")

        self.input_i_ch_1 = QtWidgets.QLineEdit(self.Data_logger_ch_label_main)

        self.input_i_ch_1.setGeometry(QtCore.QRect(110, 50, 71, 20))

        self.input_i_ch_1.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.input_i_ch_1.setObjectName("input_i_ch_1")

        self.input_i_ch_1.setText("102")  # set the default input current channel ***************

        self.output_v_ch_1 = QtWidgets.QLineEdit(self.Data_logger_ch_label_main)

        self.output_v_ch_1.setGeometry(QtCore.QRect(210, 50, 71, 20))

        self.output_v_ch_1.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.output_v_ch_1.setObjectName("output_v_ch_1")

        self.output_v_ch_1.setText("103")  # set the default output voltage channel ***************

        self.output_i_ch_1 = QtWidgets.QLineEdit(self.Data_logger_ch_label_main)

        self.output_i_ch_1.setGeometry(QtCore.QRect(310, 50, 71, 20))

        self.output_i_ch_1.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.output_i_ch_1.setObjectName("output_i_ch_1")

        self.output_i_ch_1.setText("104")  # set the default output current channel ***************

        self.vcc_ch_1 = QtWidgets.QLineEdit(self.Data_logger_ch_label_main)

        self.vcc_ch_1.setGeometry(QtCore.QRect(410, 50, 71, 20))

        self.vcc_ch_1.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.vcc_ch_1.setObjectName("vcc_ch_1")

        self.vcc_ch_1.setText("105")  # set the default vcc channel ***************



        self.ldo_ch_1 = QtWidgets.QLineEdit(self.Data_logger_ch_label_main)

        self.ldo_ch_1.setGeometry(QtCore.QRect(510, 50, 71, 20))

        self.ldo_ch_1.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.ldo_ch_1.setObjectName("LDO_ch_label")

        self.ldo_ch_1.setText("106")  # set the default ldo channel ***************
    
    def setup_start_button(self):
        self.Start_button = QtWidgets.QPushButton(self.centralwidget) #old code without connecting to radio button

        #self.Start_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.select())

        self.Start_button.setEnabled(True)

        self.Start_button.setGeometry(QtCore.QRect(375, 715, 151, 41))

        font = QtGui.QFont()

        font.setPointSize(12)

        font.setBold(True)

        font.setWeight(75)

        self.Start_button.setFont(font)

        self.Start_button.setStyleSheet("background-color: rgb(85, 85, 255);")

        self.Start_button.setDefault(False)

        self.Start_button.setFlat(False)

        self.Start_button.setObjectName("Start_button")

    def setup_frequency(self):
        
        self.measure_frequency = QtWidgets.QGroupBox(self.centralwidget)# set radio button

        self.measure_frequency.setGeometry(QtCore.QRect(30, 700, 250, 90))

        font = QtGui.QFont()

        font.setPointSize(12)

        font.setBold(True)

        font.setWeight(75)

        self.measure_frequency.setFont(font)

        self.measure_frequency.setAutoFillBackground(False)

        self.measure_frequency.setStyleSheet("background-color: rgb(228, 255, 226);")

        self.measure_frequency.setFlat(False)

        self.measure_frequency.setCheckable(False)

        self.measure_frequency.setObjectName("measure_frequency")

        self.radioButton = QtWidgets.QRadioButton(self.measure_frequency)

        self.radioButton.setGeometry(QtCore.QRect(60, 30, 80, 23))

        self.radioButton.setObjectName("radioButton")
        
    def get_text(self):
        
        self.DC_sup_add.currentText() # notice the word "currentText", this picks the current item from the drop down box

        self.data_logger_add.currentText()

        self.E_load_address.currentText()

        self.lecroy_USB_address.currentText()

        self.input_V.text()

        self.input_Current.text()

        self.input_Max_Voltage.text()

        self.input_Max_Current.text()

        self.output_Max_Current.text()

        self.output_file_name.text()

        self.Low_load_start.text()

        self.Low_load_step.text()

        self.Low_load_stop.text()

        self.High_load_stop.text()

        self.High_load_step.text()

        self.Input_shunt_max_v.text()

        self.Input_shunt_max_i.text()

        self.Output_shunt_max_v.text()

        self.Output_shunt_max_i.text()

        self.low_load_delay_time.text()

        self.high_load_delay_time.text()

        self.input_v_ch_1.text()

        self.input_i_ch_1.text()

        self.output_v_ch_1.text()

        self.output_i_ch_1.text()

        self.vcc_ch_1.text()

        self.ldo_ch_1.text()
    
    def setupUi(self, DCDC_Efficiency):

        rm = visa.ResourceManager()

        DCDC_Efficiency.setObjectName("DCDC_Efficiency")

        DCDC_Efficiency.resize(636, 788)

        DCDC_Efficiency.setAutoFillBackground(False)

        DCDC_Efficiency.setStyleSheet("background-color: rgb(207, 217, 221);")

        self.centralwidget = QtWidgets.QWidget(DCDC_Efficiency)

        self.centralwidget.setObjectName("centralwidget")
        
        self.setup_dc_input()
        
        self.setup_protection()
        
        self.setup_load_range()

        self.setup_output_file()
        
        self.setup_instrument_address()
    
        self.setup_delay_time()

        self.setup_current_shunt()

        self.setup_data_logger()

        self.setup_start_button()

        self.setup_frequency()
    



        # links all PB and lin edit to function parameters ******************************************

        self.DC_sup_add.currentIndexChanged.connect(self.select)

        self.Start_button.clicked.connect(self.pressed)

        self.get_text()




        DCDC_Efficiency.setCentralWidget(self.centralwidget)
        

        # self.menubar = QtWidgets.QMenuBar(DCDC_Efficiency)

        # self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 20))

        # self.menubar.setObjectName("menubar")

        # DCDC_Efficiency.setMenuBar(self.menubar)

        # self.statusbar = QtWidgets.QStatusBar(DCDC_Efficiency)

        # self.statusbar.setObjectName("statusbar")

        # DCDC_Efficiency.setStatusBar(self.statusbar)

        # self.vin_list = QtWidgets.QListWidget()  # make a "list" from widget



        self.retranslateUi(DCDC_Efficiency)

        QtCore.QMetaObject.connectSlotsByName(DCDC_Efficiency)


    def retranslateUi(self, DCDC_Efficiency):

        _translate = QtCore.QCoreApplication.translate

        s = 0

        t = 0

        v = 0

        y = 0

        z = 0

        print("supply is", supply)

        for list_y in supply:

            self.DC_sup_add.setItemText(y, _translate("drop_main", str(list_y))) #place specific itme of list in frop down box

            #print("list y is",list_y)

            """device_name = rm.open_resource(list_y).query('*IDN?')

            if device_name.find('N6705C') > -1:

                print("device name is", device_name)

                self.input_Max_Voltage.setEnabled(False)

                self.input_Max_Current.setEnabled(False)"""

            y = y + 1

        for list_z in load:

            self.E_load_address.setItemText(z, _translate("drop_main", str(list_z)))

            z = z + 1

        for list_v in DAQ:

            self.data_logger_add.setItemText(z, _translate("drop_main", str(list_v)))

            v = v + 1

        for list_s in o_scope:

            self.lecroy_USB_address.setItemText(z, _translate("drop_main", str(list_s)))

            s = s + 1

        """for list_t in meter: #no need for efficiency GUI, not setup in program, only DAQ

            self.data_logger_add.setItemText(z, _translate("drop_main", str(list_t)))

            t = t + 1"""



        DCDC_Efficiency.setWindowTitle(_translate("DCDC_Efficiency", "Infineon PoL Automation v1.0.0"))

        self.protection_label_main.setTitle(_translate("DCDC_Efficiency", "Protection"))

        self.input_Max_Voltage_label.setText(_translate("DCDC_Efficiency", "Max Vin(V)"))

        self.input_Max_Current_label.setText(_translate("DCDC_Efficiency", "Max Iin(A)"))

        self.output_Max_Current_label.setText(_translate("DCDC_Efficiency", "Max Iout(A)"))

        self.DC_Input_label_main.setTitle(_translate("DCDC_Efficiency", "DC Input"))

        self.input_V_label.setText(_translate("DCDC_Efficiency", "Vin(V)"))

        self.input_Current_label.setText(_translate("DCDC_Efficiency", "Iin(A)"))

        self.Load_Range_Label.setTitle(_translate("DCDC_Efficiency", "Load Ranges (A)"))

        self.Low_load_start_label.setText(_translate("DCDC_Efficiency", "Low Load Start"))

        self.Low_load_step_label.setText(_translate("DCDC_Efficiency", "Low Load Step"))

        self.Low_load_stop_label.setText(_translate("DCDC_Efficiency", "Low Load Stop"))

        self.High_load_stop_label.setText(_translate("DCDC_Efficiency", "High Load Stop"))

        self.High_load_step_label.setText(_translate("DCDC_Efficiency", "High Load Step"))

        self.output_file_label_main.setTitle(_translate("DCDC_Efficiency", "Output File"))

        self.output_file_label.setText(_translate("DCDC_Efficiency", "Output File Name"))

        self.Instr_Add_Label_main.setTitle(_translate("DCDC_Efficiency", "Instrument Addresses"))

        self.DC_sup_add_label.setText(_translate("DCDC_Efficiency", "DC Supply"))

        self.data_logger_add_label.setText(_translate("DCDC_Efficiency", "Data Acquisition"))

        self.E_load_address_label.setText(_translate("DCDC_Efficiency", "E-Load"))

        self.lecroy_USB_address_label.setText(_translate("DCDC_Efficiency", "Oscilloscope"))

        self.delay_time_label_main.setTitle(_translate("DCDC_Efficiency", "Delay Time Prior To Measurement"))

        self.low_load_delay_time_label.setText(_translate("DCDC_Efficiency", "Low Load Delay Time"))

        self.high_load_delay_time_label.setText(_translate("DCDC_Efficiency", "High Load Delay Time"))

        self.Start_button.setText(_translate("DCDC_Efficiency", "START"))

        self.Current_shunt_settings_label_main.setTitle(_translate("DCDC_Efficiency", "Current Shunt Settings"))

        self.Input_shunt_max_v_label.setText(_translate("DCDC_Efficiency", "Input Shunt Max V"))

        self.Input_shunt_max_i_label.setText(_translate("DCDC_Efficiency", "Input Shunt Max I"))

        self.Output_shunt_max_v_label.setText(_translate("DCDC_Efficiency", "Output Shunt Max V"))

        self.Output_shunt_max_i_label.setText(_translate("DCDC_Efficiency", "Output Shunt max I"))

        self.Data_logger_ch_label_main.setTitle(_translate("DCDC_Efficiency", "Data_Logger_Channels"))

        self.input_v_ch_label.setText(_translate("DCDC_Efficiency", "input_v_ch"))

        self.input_i_ch_label.setText(_translate("DCDC_Efficiency", "input_i_ch"))

        self.output_v_ch_label.setText(_translate("DCDC_Efficiency", "output_v_ch"))

        self.output_i_ch_label.setText(_translate("DCDC_Efficiency", "output_i_ch"))

        self.vcc_ch_label.setText(_translate("DCDC_Efficiency", "vcc_ch"))

        self.ldo_ch_label.setText(_translate("DCDC_Efficiency", "LDO_ch"))

        self.measure_frequency.setTitle(_translate("DCDC_Efficiency", "Measure FREQ and On-time"))

        self.radioButton.setText(_translate("DCDC_Efficiency", "ON/OFF"))



    def select(self):

        device_name = rm.open_resource(self.DC_sup_add.currentText()).query('*IDN?')



        if device_name.find('N6705C') > -1:

            print("device name is", device_name)

            self.input_Max_Voltage.setEnabled(False)

            self.input_Max_Current.setEnabled(False)



    def pressed(self):

        print("drop down item is ")

        power_supply_GPIB_address = self.DC_sup_add.currentText() #set drop down to particular address

        print("supply is", self.DC_sup_add.currentText())



        """device_name = rm.open_resource(self.DC_sup_add.currentText()).query('*IDN?')



        if device_name.find('N6705C') > -1:

            print("device name is", device_name)

            self.input_Max_Voltage.setEnabled(False)

            self.input_Max_Current.setEnabled(False)"""



        print("I'm herererererererer 666 ", power_supply_GPIB_address)

        data_logger_GPIB_address = self.data_logger_add.currentText() #set drop down to particular address

        electronic_load_GPIB_address = self.E_load_address.currentText() #set drop down to particular address

        lecory_usb_address = self.lecroy_USB_address.currentText() #set drop down to particular address

        #Input_V = float(self.input_V.text())

        Input_I = float(self.input_Current.text())

        Max_input_voltage = float(self.input_Max_Voltage.text())

        Max_input_current = float(self.input_Max_Current.text())

        Max_load_current = float(self.output_Max_Current.text())

        output_file = self.output_file_name.text()

        Low_load_start = float(self.Low_load_start.text())

        Low_load_step = float(self.Low_load_step.text())

        Low_load_stop = float(self.Low_load_stop.text())

        High_load_stop = float(self.High_load_stop.text())

        High_load_step = float(self.High_load_step.text())

        input_shunt_max_voltage = float(self.Input_shunt_max_v.text())

        input_shunt_max_current = float(self.Input_shunt_max_i.text())

        output_shunt_max_voltage = float(self.Output_shunt_max_v.text())

        output_shunt_max_current = float(self.Output_shunt_max_i.text())

        low_load_timing = float(self.low_load_delay_time.text())

        high_load_timing = float(self.high_load_delay_time.text())

        input_v_ch = str(self.input_v_ch_1.text())

        input_i_ch = str(self.input_i_ch_1.text())

        output_v_ch = str(self.output_v_ch_1.text())

        output_i_ch = str(self.output_i_ch_1.text())

        vcc_ch = str(self.vcc_ch_1.text())

        ldo_ch = str(self.ldo_ch_1.text())



        if self.input_V.text():

            Input_V = [float(val) for val in self.input_V.text().split(",")]  # allows floating values, space, commas

            self.vin_list.addItems([str(val) for val in Input_V])  # add values to list

            print(Input_V)





        if self.radioButton.isChecked(): # for measuring frequency and on-time

            FRE = int(1) #set FRE state if radioButton is checked

            msg = QMessageBox()  # pop-up box to remind user to connect probe to phase node

            msg.setWindowTitle("Measuring Frequency and On-time")

            msg.setText("Please be sure to hook CH1 probe up to phase node")

            x = msg.exec_()  # display message

        else:

            FRE = int(0)



        # calls function

        eff(input_shunt_max_voltage, input_shunt_max_current, output_shunt_max_voltage, output_shunt_max_current,

            power_supply_GPIB_address, data_logger_GPIB_address, electronic_load_GPIB_address, lecory_usb_address,

            input_v_ch, input_i_ch, output_v_ch, output_i_ch, vcc_ch, ldo_ch, Max_input_voltage, Max_input_current,

            Max_load_current, output_file, Input_V, Input_I, Low_load_start, Low_load_step, Low_load_stop,

            High_load_stop, High_load_step, low_load_timing, high_load_timing, FRE)





if __name__ == "__main__":

    import sys

find_dev()

app = QtWidgets.QApplication(sys.argv)

DCDC_Efficiency = QtWidgets.QMainWindow()

ui = Ui_DCDC_Efficiency()

#ui.openWindow()  # calls the method to open table with list of all equipment

ui.setupUi(DCDC_Efficiency)

DCDC_Efficiency.show()

sys.exit(app.exec_())

