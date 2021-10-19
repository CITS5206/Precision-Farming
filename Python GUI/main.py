# The University of Western Australia : 2021
# CITS5206 Professional Computing
# Group: Precision Farming

# Source Code


# Author: Arjun Panicker
# Co-Author: Deepakraj Sugumaran
# Date Created: 
# Last Modified: 
# Version:  2.0
# State :  Beta

# References:

# [1] - https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python (Oct,2021)


from posix import listdir
import re
import threading
import subprocess
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from typing import Collection
from tkinter import messagebox
import serial
import sys
import glob
import serial.tools.list_ports
import os
import datetime
import time
import webbrowser




class GUI():
    """ EMI Toolkit GUI Class
        :parameters:
            None
        :methods:
            confirm_selection(),
            scanPorts(),
            saveProject(),
            readSensor(),
            stop_sensor_process(),
        
        :returns:
            None
                    
    """

    def __init__(self):
        """ Initialize a GUI Window
            :returns:
                        None
                    
        """
        #SET RASPBERRY PI DISPLAY ENVIRONMENT VARIABLE
        if os.environ.get('DISPLAY','') == '':
                #print('no display found. Using :0.0')
                os.environ.__setitem__('DISPLAY', ':0.0')
        self.GUIWindow()
        self.GUIFrame()
        self.GUIVariables()
        self.GUISetupOptions()
        self.GUIFileOptions()
        self.GUIControlOPtions()
        self.GUIVisualOptions()
        self.GUIProgramStatus()
        self.GUISoftwareVersion()
        self.GUIMasterGrid()
        
    def GUIMainloop(self):
        self.WINDOW.mainloop()    

    def GUIWindow(self):

            #INITIALIZE GUI WINDOW
            self.WINDOW = Tk()
            self.WINDOW.title("E.M.I Toolkit")
            self.WINDOW.geometry('640x460')
            self.WINDOW.minsize(width=640,height=460)
            self.WINDOW.maxsize(width=640,height=460)
        
    def GUIFrame(self):
            self.MAINFRAME = Frame(self.WINDOW)
            self.MAINFRAME.grid(pady=10,padx=5)

    def GUIVariables(self):

            # GUI VARIABLES
            
            self.button_width = 19
            self.button_padding_x = 2
            self.button_padding_y = 2
            self.combo_box_width = 20
            self.sep_padding_y = 10
            self.sep_padding_x = 0
            self.text_padding_x = 0
            self.text_padding_y = 2
            self.label_font = 'Helvetica 16 bold'
            self.button_font = 'Helvetica 12'
            self.software_version_font = 'Courier 8 italic'
            self.software_version = 'SW Version 1.0'

            
            # PROGRAM VARIABLES
            self.DUALEM_PORT,self.DUALEM_BAUD,self.DUALEM_FREQ = StringVar() ,StringVar(), StringVar()
            self.GPS_PORT, self.GPS_BAUD,self.GPS_FREQ = StringVar(), StringVar() , StringVar()
            self.PROGRAM_STATUS = StringVar()
            
            # self.LEGAL_OPTIONS= ['/dev/tty.usbserial-AL02V3VW','/dev/ttyUSB-AL02V3VW','/dev/tty.usbserial-1110']
            self.LEGAL_BAUD_RATES = ['BAUD RATE','4800', '9600', '14400', '19200', '38400', '57600', '115200', '128000' , '256000']
            self.LEGAL_FREQ_RATES = ['FREQUENCY (M.P.S)','1/10', '1/5', '1/2', '1', '2', '5', '10']

            self.PROGRAM_STATUS_OP = False

    def GUISetupOptions(self):

            # START : SETUP OPTIONS
            self.SETUP_LABEL = ttk.Label(self.MAINFRAME, text="SETUP OPTIONS",justify=tkinter.CENTER,font=self.label_font)
        
            # SETUP OPTIONS --> SCAN AND VERIY 
            self.SCAN_BTN = Button(self.MAINFRAME, text="SCAN PORTS", command=self.scanPorts,width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y)
            self.CONFIRM_BTN = Button(self.MAINFRAME, text="CONFIRM SELECTION", command=self.GUISanityCheck,state="disabled",width=19,pady=2,padx=2, bg="#c90231")
        
            # SETUP OPTIONS --> SCAN DUALEM PORT
            #self.PORT_LABEL = ttk.Label(self.MAINFRAME, text="PORT NAME",justify=tkinter.LEFT, width=10)
            self.DUALEM_PORT_OPTION_BTN = ttk.Combobox(self.MAINFRAME,textvariable=self.DUALEM_PORT, state='disabled',width=self.combo_box_width)
            self.DUALEM_PORT_OPTION_BTN.set("SENSOR PORT")

            self.DUALEM_PORT_BAUD_BTN = ttk.Combobox(self.MAINFRAME,textvariable=self.DUALEM_BAUD,values=self.LEGAL_BAUD_RATES, state='disabled',width=self.combo_box_width)
            self.DUALEM_PORT_BAUD_BTN.set(self.LEGAL_BAUD_RATES[0])

            self.DUALEM_PORT_FREQ_BTN = ttk.Combobox(self.MAINFRAME,textvariable=self.DUALEM_FREQ,values=self.LEGAL_FREQ_RATES, state='disabled',width=self.combo_box_width)
            self.DUALEM_PORT_FREQ_BTN.set(self.LEGAL_FREQ_RATES[0])

            # SETUP OPTIONS --> SCAN GPS PORT
            self.GPS_PORT_OPTION_BTN = ttk.Combobox(self.MAINFRAME,textvariable=self.GPS_PORT, state='disabled',width=self.combo_box_width)
            self.GPS_PORT_OPTION_BTN.set("GPS PORT")
            
            self.GPS_PORT_BAUD_BTN = ttk.Combobox(self.MAINFRAME,textvariable=self.GPS_BAUD,values=self.LEGAL_BAUD_RATES, state='disabled',width=self.combo_box_width)
            self.GPS_PORT_BAUD_BTN.set(self.LEGAL_BAUD_RATES[0])

            self.GPS_PORT_FREQ_BTN = ttk.Combobox(self.MAINFRAME,textvariable=self.GPS_FREQ,values=self.LEGAL_FREQ_RATES, state='disabled',width=self.combo_box_width)
            self.GPS_PORT_FREQ_BTN.set(self.LEGAL_FREQ_RATES[0])
            # END : SETUP OPTIONS

    def GUIFileOptions(self):

            # START : FILE OPTIONS
            self.FILE_LABEL = ttk.Label(self.MAINFRAME, text="FILE OPTIONS",justify=tkinter.CENTER,font=self.label_font)
            self.SAVE_PROJECT_BTN = Button(self.MAINFRAME, text="SAVE PROJECT", command=self.saveProject,width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y,state='disabled')
            self.EXISTING_FOLDER_BTN = Button(self.MAINFRAME, text="OUTPUT FOLDER", command=self.saveProject,width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y, state="disabled")
            self.PREV_PROJECTS_BTN = Button(self.MAINFRAME, text="EXPLORE PREVIOUS PROJECTS", command=self.prevProjects,width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y, state="normal")

            # END : FILE OPTIONS
   
    def GUIControlOPtions(self):

            # START : CONTROL OPTIONS
            self.CONTROL_LABEL = ttk.Label(self.MAINFRAME, text='CONTROL PANEL',justify=tkinter.CENTER,font=self.label_font)
            self.START_SENSOR_BTN = Button(self.MAINFRAME,text="START SENSOR READING",command=self.readSensor, state="disabled",width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y)
            self.STOP_SENSOR_BTN = Button(self.MAINFRAME,text="STOP SENSOR READING", command=self.stop_sensor_process, state="disabled",width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y)
            self.READ_OP_DATA = Button(self.MAINFRAME,text="ENABLE LIVE OUTPUT", command=self.open_op_window, state="normal",width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y)

            # END : CONTROL OPTIONS

    def GUIVisualOptions(self):
            
            # START: VISUALIZATION
            self.VISUAL_LABEL = ttk.Label(self.MAINFRAME, text='VISUALIZATION',justify=tkinter.CENTER,font=self.label_font)
            self.START_WEBSEVER_BTN = Button(self.MAINFRAME,text="START WEBSERVER",command=self.readSensor, state="disabled",width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y)
            self.STOP_WEBSEVER_BTN = Button(self.MAINFRAME,text="STOP WEBSERVER",command=self.readSensor, state="disabled",width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y)
            self.OPEN_WEBSEVER_BTN = Button(self.MAINFRAME,text="OPEN WEB BROWSER",command=self.openbrowser, state="normal",width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y)

            # END: VISUALIZATION

    def GUIProgramStatus(self):
            
            # START: STATUS INDICATOR
            self.STATUS_INDICATOR_LABEL = ttk.Label(self.MAINFRAME, text="PROGRAM STATUS",justify=tkinter.CENTER, font=self.label_font)
            self.STATUS_INDICATOR = ttk.Label(self.MAINFRAME,textvariable=self.PROGRAM_STATUS,relief=tkinter.SUNKEN,width=55,justify=tkinter.LEFT)
            self.PROGRAM_STATUS.set("Press SCAN PORTS to run the program.")
            # END: STATUS INDICATOR

    def GUISoftwareVersion(self):
            # START
            self.SOFTWARE_VERSION_LABEL=  ttk.Label(self.MAINFRAME,justify=tkinter.CENTER,font=self.software_version_font)
            self.SOFTWARE_VERSION_LABEL.grid(row=25,columnspan=3)
            self.SOFTWARE_VERSION_LABEL.config(text=self.software_version)
            # END
   
    def GUIMasterGrid(self):
            
            # MASTER GRID LAYOUT
            ttk.Separator(self.MAINFRAME, orient=tkinter.HORIZONTAL).grid(row=1, columnspan=3,pady=10,sticky='ew')

            self.SETUP_LABEL.grid(row=0,columnspan=3,pady=self.text_padding_y)
            self.SCAN_BTN.grid(row=0,column=0)
            self.CONFIRM_BTN.grid(row=0,column=2)
            
            self.DUALEM_PORT_OPTION_BTN.grid(row=3,column=0,pady=self.text_padding_y)
            self.DUALEM_PORT_BAUD_BTN.grid(row=3,column=1,pady=self.text_padding_y)
            self.DUALEM_PORT_FREQ_BTN.grid(row=3, column=2,pady=self.text_padding_y)
            
            self.GPS_PORT_OPTION_BTN.grid(row=4,column=0,pady=self.text_padding_y)
            self.GPS_PORT_BAUD_BTN.grid(row=4,column=1,pady=self.text_padding_y)
            self.GPS_PORT_FREQ_BTN.grid(row=4, column=2,pady=self.text_padding_y)


            
            ttk.Separator(self.MAINFRAME, orient=tkinter.HORIZONTAL).grid(row=5,columnspan=3,sticky='ew',pady=self.sep_padding_y)
            self.FILE_LABEL.grid(row=6,columnspan=3,pady=self.text_padding_y)
            self.SAVE_PROJECT_BTN.grid(row=7,column=0)
            self.EXISTING_FOLDER_BTN.grid(row=7,column=1)
            self.PREV_PROJECTS_BTN.grid(row=7,column=2)


            ttk.Separator(self.MAINFRAME, orient=tkinter.HORIZONTAL).grid(row=8,columnspan=3,sticky='ew',pady=self.sep_padding_y)
            self.CONTROL_LABEL.grid(row=9,columnspan=3,pady=self.text_padding_y)
            self.START_SENSOR_BTN.grid(row=10,column=0)
            self.STOP_SENSOR_BTN.grid(row=10,column=1)
            self.READ_OP_DATA.grid(row=10,column=2)
            
        
        
            ttk.Separator(self.MAINFRAME, orient=tkinter.HORIZONTAL).grid(row=11,columnspan=3,sticky='ew',pady=self.sep_padding_y)
            self.VISUAL_LABEL.grid(row=12,columnspan=3,pady=self.text_padding_y)
            self.START_WEBSEVER_BTN.grid(row=13,column=0)
            self.STOP_WEBSEVER_BTN.grid(row=13,column=1)
            self.OPEN_WEBSEVER_BTN.grid(row=13,column=2)

            ttk.Separator(self.MAINFRAME, orient=tkinter.HORIZONTAL).grid(row=20,columnspan=3,sticky='ew',pady=self.sep_padding_y)
            self.STATUS_INDICATOR_LABEL.grid(row=21,columnspan=3,pady=self.text_padding_y)
            self.STATUS_INDICATOR.grid(row=22,columnspan=3,pady=self.text_padding_y)

    def GUISanityCheck(self):
        VALID = False
        if self.DUALEM_PORT.get() == "SENSOR PORT" or  self.GPS_PORT.get() == "GPS PORT":
            self.PROGRAM_STATUS.set("Command: Scan Ports\nStatus: Port Selection Error")
            self.MAINFRAME.update()
            messagebox.showwarning(title="WARNING",message= "PORT SELECTION ERROR")

        if self.DUALEM_BAUD.get() == 'BAUD RATE' or self.GPS_BAUD.get()== 'BAUD RATE':
            self.PROGRAM_STATUS.set("Command: Confirm Selection\nStatus: Baud Rate Not Set")
            self.MAINFRAME.update()
            messagebox.showwarning(title="WARNING",message= "BAUD RATE NOT SELECTED")

        elif self.DUALEM_FREQ.get()=='FREQUENCY (M.P.S)' or self.GPS_FREQ.get() == 'FREQUENCY (M.P.S)':
            self.PROGRAM_STATUS.set("Command: Confirm Selection\nStatus: Frequency Rate Not Set")
            self.MAINFRAME.update()
            messagebox.showwarning(title="WARNING",message= "Frequency Not Set")

        else:
            self.PROGRAM_STATUS.set("Command: Confirm Selection\nStatus: OK")
            print(f"Verifying Settings: {not VALID}")
            self.GUISelectionToggle()

        try:
            print(self.DUALEM_BAUD.get())
            print(self.GPS_BAUD.get())
            # if isinstance(self.DUALEM_BAUD,int):print(f"{self.DUALEM_BAUD}")
            # if isinstance(self.GPS_BAUD,int):print(f"{self.GPS_BAUD}")
        except Exception as e:
            print(e)
        
    def GUISelectionToggle(self):
        FLAG = ["WAIT FOR SCAN","USB NOT DETECTED" ]
        if self.CONFIRM_BTN.cget('text') != "MODIFY SELECTION":
            if not self.DUALEM_PORT.get() in FLAG  and not self.GPS_PORT.get() in FLAG :
                self.SCAN_BTN['state'] = tkinter.DISABLED
                self.SAVE_PROJECT_BTN['state'] = tkinter.NORMAL
                self.DUALEM_PORT_OPTION_BTN.state(['disabled'])
                self.DUALEM_PORT_BAUD_BTN.state(['disabled'])
                self.DUALEM_PORT_FREQ_BTN.state(['disabled'])
                self.GPS_PORT_OPTION_BTN.state(["disabled"])
                self.GPS_PORT_FREQ_BTN.state(['disabled'])
                self.GPS_PORT_BAUD_BTN.state(['disabled'])
                self.CONFIRM_BTN.config(text="MODIFY SELECTION")
                self.PROGRAM_STATUS.set("Command: CONFIRM SELECTION\nSTATUS: OK")

        elif self.CONFIRM_BTN.cget('text') == "MODIFY SELECTION":
                self.SCAN_BTN['state'] = tkinter.NORMAL
                self.SAVE_PROJECT_BTN['state'] = tkinter.DISABLED
                self.DUALEM_PORT_OPTION_BTN.state(['!disabled'])
                self.DUALEM_PORT_BAUD_BTN.state(['!disabled'])
                self.DUALEM_PORT_FREQ_BTN.state(['!disabled'])
                self.GPS_PORT_OPTION_BTN.state(['!disabled'])
                self.GPS_PORT_FREQ_BTN.state(['!disabled'])
                self.GPS_PORT_BAUD_BTN.state(['!disabled'])
                self.CONFIRM_BTN.config(text="CONFIRM SELECTION")
                self.PROGRAM_STATUS.set("Command: MODIFY SELECTION\nSTATUS: OK")

                #self.MAINFRAME.update()

    def scanPorts(self):
        ''' Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
        '''
        # Reference [1] - Modified by Arjun Panicker (Sept, 2021)

        if sys.platform.startswith('win'):
            ports = serial.tools.list_ports.comports()
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = ['Debug'] # Remove this in production software
        
        for eachPort in ports:
            print(eachPort.lower())
            if 'usb' in eachPort.lower():
                try:
                    serial.Serial(eachPort).close()
                    result.append(eachPort)
                except (OSError, serial.SerialException):
                    pass
        if result:
            s = ["SENSOR PORT"] + result
            g = ["GPS PORT"] + result
            self.DUALEM_PORT_OPTION_BTN.state(['!disabled'])
            self.DUALEM_PORT_BAUD_BTN.state(['!disabled'])
            self.DUALEM_PORT_FREQ_BTN.state(['!disabled'])
            self.DUALEM_PORT_OPTION_BTN.state(['readonly'])
            self.DUALEM_PORT_BAUD_BTN.state(['readonly'])
            self.DUALEM_PORT_FREQ_BTN.state(['readonly'])
            self.DUALEM_PORT_OPTION_BTN['values'] = s
            self.DUALEM_PORT_OPTION_BTN.set(s[1])
            self.DUALEM_PORT_BAUD_BTN.set(self.LEGAL_BAUD_RATES[2])
            self.DUALEM_PORT_FREQ_BTN.set(self.LEGAL_FREQ_RATES[4])
            
            
            self.GPS_PORT_OPTION_BTN.state(["!disabled"])
            self.GPS_PORT_BAUD_BTN.state(["!disabled"])
            self.GPS_PORT_FREQ_BTN.state(["!disabled"])
            self.GPS_PORT_OPTION_BTN.state(["readonly"])
            self.GPS_PORT_BAUD_BTN.state(["readonly"])
            self.GPS_PORT_FREQ_BTN.state(["readonly"])
            self.GPS_PORT_OPTION_BTN['values'] = g
            self.GPS_PORT_OPTION_BTN.set(g[1])
            self.GPS_PORT_BAUD_BTN.set(self.LEGAL_BAUD_RATES[5])
            self.GPS_PORT_FREQ_BTN.set(self.LEGAL_FREQ_RATES[4])

            self.CONFIRM_BTN['state'] = tkinter.NORMAL
            self.PROGRAM_STATUS.set("Command: SCAN PORTS\nSTATUS: OK ")
        else:
            self.GPS_PORT_OPTION_BTN.state(["disabled"])
            self.GPS_PORT_OPTION_BTN.set("GPS NOT DETECTED")
            self.DUALEM_PORT_OPTION_BTN.state(['disabled'])
            self.DUALEM_PORT_OPTION_BTN.set("SENSOR NOT DETECTED")
            self.CONFIRM_BTN['state'] = tkinter.DISABLED
            self.PROGRAM_STATUS.set("Command: SCAN PORTS\nSTATUS: CHECK CONNECTION ")
    
    def saveProject(self):
        '''
        Function to set project output directory
        returns:
            None
        '''
        
        try:
            # Create a default output folder
            # Make the default dir if it doesn't exist already
            opath = os.path.join(os.path.expanduser('~'),'Documents','EMI-Toolkit')
            if not os.path.exists(opath):
                    os.mkdir(opath)
            filename = datetime.datetime.now().strftime("data-%d-%m-%Y")
        
            self.pwd = filedialog.askdirectory(initialdir=opath)
            self.project_path = os.path.join(self.pwd,'{}.csv'.format(filename))

            if not listdir(self.pwd):
                self.START_SENSOR_BTN['state'] = tkinter.NORMAL
                self.PROGRAM_STATUS.set("Command: SAVE PROJECT \nPATH: {}".format(self.project_path))
                self.SAVE_PROJECT_BTN.config(text="FOLDER SELECTED")
            else:
                self.PROGRAM_STATUS.set("Command: SAVE PROJECT \nSTATUS: WARNING - FOUND EXISTING FILES")
                self.MAINFRAME.update()
                messagebox.showwarning(title="WARNING",message= "Directory not empty")
                if messagebox.askyesno("Confirm Action", "Overwrite files in this directory?"):
                        self.START_SENSOR_BTN['state'] = tkinter.NORMAL 
                        self.PROGRAM_STATUS.set("Command: SAVE PROJECT \nPATH: {}".format(self.project_path))
                        self.SAVE_PROJECT_BTN.config(text="FOLDER SELECTED")
                else:
                        self.PROGRAM_STATUS.set("Command: SAVE PROJECT \nSTATUS: RESELECT PROJECT FOLDER")
                        self.MAINFRAME.update()
        except Exception as e:
            print(e)

    def readSensor(self):
        self.threadFlag = True
        def readserial(self,port=self.DUALEM_PORT.get(),path=self.project_path):
            while self.threadFlag:
                if self.PROGRAM_STATUS_OP:
                    self.PROGRAM_STATUS.set(f"{datetime.datetime.now().strftime('%H:%M:%S')}")
                time.sleep(0.01)
            if not self.threadFlag:
                print(f"Termindated {threading.current_thread().name}")

        def readserial_debug(self,port='Debug',baudrate=9600,timeout=1,path=self.project_path):
            while self.threadFlag:
                self.PROGRAM_STATUS.set(f"{port} : {baudrate} : {timeout}")
                time.sleep(int(timeout))
            if not self.threadFlag:
                print(f"Terminated {threading.current_thread().name}")

        if self.DUALEM_PORT.get()=='Debug' or self.GPS_PORT.get() == 'Debug':
            self.worker1 = threading.Thread(target=readserial_debug,name="DebugSerialRead", args=(self,'Dualem',self.DUALEM_BAUD.get(), self.DUALEM_FREQ.get(), self.project_path), daemon=True)
            self.worker2 = threading.Thread(target=readserial_debug,name="DebugSerialRead", args=(self,'GPS',self.GPS_BAUD.get(), self.GPS_FREQ.get(), self.project_path),daemon=True)
            self.worker1.start()
            self.worker2.start()
        self.STOP_SENSOR_BTN['state'] = tkinter.NORMAL
        self.START_SENSOR_BTN['state'] = tkinter.DISABLED
            #self.proc = subprocess.Popen(['python3','main_read.py', self.DUALEM_PORT.get(),self.project_path]) 
             # Run other script - doesn't wait for it to finish.
        #print(self.proc.pid)
        # if self.proc.pid:
        #        self.STOP_SENSOR_BTN['state'] = tkinter.NORMAL
        #        self.START_SENSOR_BTN['state'] = tkinter.DISABLED
        self.MAINFRAME.update() 
    
    def stop_sensor_process(self):
        try:
            if self.worker1.is_alive() or self.worker2.is_alive():
                self.threadFlag = False

            # if self.proc:
                # self.proc.terminate()
                
                #print("PROCESS: {} TERMINATED".format(self.proc.pid))
                self.START_SENSOR_BTN['state'] = tkinter.NORMAL
                self.STOP_SENSOR_BTN['state'] = tkinter.DISABLED
                #self.task.join()
                return True
                
            return False

        except Exception as e:
            print("NO PROCESS TO TERMINATE")
            return False
        
    def prevProjects(self):
        opath = os.path.join(os.path.expanduser('~'),'Documents','EMI-Toolkit')
        if not os.path.exists(opath):
                    os.mkdir(opath)
        try:
            proc = subprocess.Popen(['open',opath])
        except Exception as e:
            print(e)

    def open_op_window(self):
        if self.READ_OP_DATA.cget('text') == "ENABLE LIVE OUTPUT":
            self.READ_OP_DATA.config(text='DISABLE LIVE OUTPUT')
        elif self.READ_OP_DATA.cget('text') == 'DISABLE LIVE OUTPUT':
            self.READ_OP_DATA.config(text='ENABLE LIVE OUTPUT')
        self.PROGRAM_STATUS_OP = not self.PROGRAM_STATUS_OP
        print(self.PROGRAM_STATUS_OP)
                  
    def openbrowser(self):
        webbrowser.open("http:localhost:5000")

    
if __name__ == "__main__":
    try:
        gui = GUI()
        gui.GUIMainloop()
    except Exception as e:
        print(e)
    finally:
        gui.stop_sensor_process()
        

        

