import collections
from posix import listdir
import re
import threading
import subprocess
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from typing import Collection
from tkinter import messagebox
import serial
import sys
import glob
import serial.tools.list_ports
import os
import datetime
# time = datetime.now().strftime("%H:%M:%S")



class GUI():
    """ Precicision Farming App GUI
        :parameters:
            None
        
        :methods:
            confirm_selection()
            serial_ports()
            openFolder()
            readSensor()
            stop_sensor_process()
        
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
        self.GUIMasterGrid()
        
    def GUIMainloop(self):
        self.WINDOW.mainloop()    

    def GUIWindow(self):

            #INITIALIZE GUI WINDOW
            self.WINDOW = Tk()
            self.WINDOW.title("Precision Farming App")
            self.WINDOW.geometry('440x480')
            self.WINDOW.minsize(width=440,height=460)
            self.WINDOW.maxsize(width=440,height=460)
        
    def GUIFrame(self):
            self.MAINFRAME = Frame(self.WINDOW)
            self.MAINFRAME.grid(pady=10,padx=10)

    def GUIVariables(self):
             # PROGRAM VARIABLES
            self.port= StringVar()
            self.gps_port = StringVar()
            self.status = StringVar()
            self.proc = None
            self.LEGAL_OPTIONS= ['/dev/tty.usbserial-AL02V3VW','/dev/ttyUSB-AL02V3VW']

    def GUISetupOptions(self):

            # START : SETUP OPTIONS
            self.LINE_DIVIDER_1 = ttk.Label(self.MAINFRAME, text='{:-<68}'.format(''),justify=tkinter.LEFT)
            self.SETUP_LABEL = ttk.Label(self.MAINFRAME, text="SETUP OPTIONS",justify=tkinter.CENTER)
        
            # SETUP OPTIONS --> SCAN AND VERIY 
            self.SCAN_BTN = Button(self.MAINFRAME, text="SCAN PORTS", command=self.serial_ports,width=19,padx=2,pady=2)
            self.CONFIRM_BTN = Button(self.MAINFRAME, text="CONFIRM SELECTION", command=self.confirm_selection,state="disabled",width=19,pady=2,padx=2, bg="#c90231")
        
            # SETUP OPTIONS --> SCAN DUALEM PORT
            self.DUALEM_LABEL = ttk.Label(self.MAINFRAME, text="SENSOR PORT",justify=tkinter.LEFT)
            self.DUALEM_PORT_OPTION_BTN = ttk.Combobox(self.MAINFRAME,textvariable=self.port, state='disabled',width=20)
            self.DUALEM_PORT_OPTION_BTN.set("WAIT FOR SCAN")
        
            # SETUP OPTIONS --> SCAN GPS PORT
            self.GPS_LABEL = ttk.Label(self.MAINFRAME, text="GPS PORT",justify=tkinter.LEFT)
            self.GPS_PORT_OPTION_BTN = ttk.Combobox(self.MAINFRAME,textvariable=self.gps_port, state='disabled',width=20)
            self.GPS_PORT_OPTION_BTN.set("WAIT FOR SCAN")
            # END : SETUP OPTIONS

    def GUIFileOptions(self):

            # START : FILE OPTIONS
            self.LINE_DIVIDER_2 = ttk.Label(self.MAINFRAME, text='{:-<68}'.format(''),justify=tkinter.LEFT)
            self.FILE_LABEL = ttk.Label(self.MAINFRAME, text="FILE OPTIONS",justify=tkinter.CENTER)
            self.SAVE_PROJECT_BTN = Button(self.MAINFRAME, text="SAVE PROJECT", command=self.openFolder,width=19,padx=2,pady=2,state='disabled')
            self.EXISTING_FOLDER_BTN = Button(self.MAINFRAME, text="OPEN EXISTING PROJECT", command=self.openFolder,width=19,padx=2,pady=2, state="disabled")

            # END : FILE OPTIONS
   
    def GUIControlOPtions(self):


            # START : CONTROL OPTIONS
            self.CONTROL_LABEL = ttk.Label(self.MAINFRAME, text='CONTROL PANEL',justify=tkinter.CENTER)
            self.LINE_DIVIDER_3 = ttk.Label(self.MAINFRAME, text='{:-<68}'.format(''),justify=tkinter.LEFT)

            self.START_SENSOR_BTN = Button(self.MAINFRAME,text="START SENSOR READING",command=self.readSensor, state="disabled",width=19,padx=2,pady=2)
            self.STOP_SENSOR_BTN = Button(self.MAINFRAME,text="STOP SENSOR READING", command=self.stop_sensor_process, state="disabled",width=19,padx=2,pady=2)
            # END : CONTROL OPTIONS

    def GUIVisualOptions(self):
            # START: VISUALIZATION
            self.LINE_DIVIDER_4 = ttk.Label(self.MAINFRAME, text='{:-<68}'.format(''),justify=tkinter.LEFT)
            self.VISUAL_LABEL = ttk.Label(self.MAINFRAME, text='VISUALIZATION',justify=tkinter.CENTER)
            self.START_WEBSEVER_BTN = Button(self.MAINFRAME,text="START WEBSERVER",command=self.readSensor, state="disabled",width=19,padx=2,pady=2)
            self.STOP_WEBSEVER_BTN = Button(self.MAINFRAME,text="STOP WEBSERVER",command=self.readSensor, state="disabled",width=19,padx=2,pady=2)



            # END: VISUALIZATION

    def GUIProgramStatus(self):
            # START: STATUS INDICATOR
            self.LINE_DIVIDER_5 = ttk.Label(self.MAINFRAME, text='{:-<68}'.format(''),justify=tkinter.LEFT)
            self.STATUS_INDICATOR = ttk.Label(self.MAINFRAME,textvariable=self.status,relief=tkinter.SUNKEN,width=40,justify=tkinter.LEFT)
            self.status.set("NO ACTIVITY")
        
    def GUIMasterGrid(self):
            
            # MASTER GRID LAYOUT
            self.LINE_DIVIDER_1.grid(row=0,columnspan=2)
            self.SETUP_LABEL.grid(row=1,columnspan=2,pady=2)
            self.SCAN_BTN.grid(row=2,column=0)
            self.CONFIRM_BTN.grid(row=2,column=1)
            self.DUALEM_LABEL.grid(row=3,column=0)
            self.DUALEM_PORT_OPTION_BTN.grid(row=3,column=1,pady=2)
            self.GPS_LABEL.grid(row=4,column=0)
            self.GPS_PORT_OPTION_BTN.grid(row=4,column=1,pady=2)

            self.LINE_DIVIDER_2.grid(row=5,columnspan=2)
            self.FILE_LABEL.grid(row=6,columnspan=2,pady=2)
            self.SAVE_PROJECT_BTN.grid(row=7,column=0)
            self.EXISTING_FOLDER_BTN.grid(row=7,column=1)


            self.LINE_DIVIDER_3.grid(row=8,columnspan=2)
            self.CONTROL_LABEL.grid(row=9,columnspan=2,pady=2)
            self.START_SENSOR_BTN.grid(row=10,column=0)
            self.STOP_SENSOR_BTN.grid(row=10,column=1)
        
        
            self.LINE_DIVIDER_4.grid(row=11,columnspan=2)
            self.VISUAL_LABEL.grid(row=12,columnspan=2,pady=2)
            self.START_WEBSEVER_BTN.grid(row=13,column=0)
            self.STOP_WEBSEVER_BTN.grid(row=13,column=1)

            self.LINE_DIVIDER_5.grid(row=14,columnspan=2)

            self.STATUS_INDICATOR.grid(row=20,columnspan=2,pady=2)

    def confirm_selection(self):
        FLAG = ["WAIT FOR SCAN","USB NOT DETECTED" ]
        if self.CONFIRM_BTN.cget('text') != "MODIFY SELECTION":
            if not self.port.get() in FLAG  and not self.gps_port.get() in FLAG :
                self.SCAN_BTN['state'] = tkinter.DISABLED
                self.SAVE_PROJECT_BTN['state'] = tkinter.NORMAL
                self.DUALEM_PORT_OPTION_BTN.state(['disabled'])
                self.GPS_PORT_OPTION_BTN.state(["disabled"])
                self.CONFIRM_BTN.config(bg='#02c916')
                self.CONFIRM_BTN.config(text="MODIFY SELECTION")
                self.status.set("CMD: CONFIRM SELECTION\nSTATUS: OK")

        elif self.CONFIRM_BTN.cget('text') == "MODIFY SELECTION":
                self.SCAN_BTN['state'] = tkinter.NORMAL
                self.SAVE_PROJECT_BTN['state'] = tkinter.DISABLED
                self.DUALEM_PORT_OPTION_BTN.state(['!disabled'])
                self.GPS_PORT_OPTION_BTN.state(["!disabled"])
                self.CONFIRM_BTN.config(text="CONFIRM SELECTION")
                self.status.set("CMD: MODIFY SELECTION\nSTATUS: OK")

                #self.MAINFRAME.update()

    def serial_ports(self):
        """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = serial.tools.list_ports.comports()
            print([port.name for port in ports])
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
    
        ACTIVE_PORTS = ['usb','USB']
        for port in ports:
            if True in [ eachActivePorts in port for eachActivePorts in ACTIVE_PORTS]:
                try:
                    s = serial.Serial(port)
                    s.close()
                    result.append(port)
                except (OSError, serial.SerialException):
                    pass
        if result:
            self.DUALEM_PORT_OPTION_BTN.state(['!disabled'])
            self.GPS_PORT_OPTION_BTN.state(["!disabled"])

            self.GPS_PORT_OPTION_BTN.state(["readonly"])
            self.DUALEM_PORT_OPTION_BTN.state(['readonly'])

            self.DUALEM_PORT_OPTION_BTN['values'] = result
            self.GPS_PORT_OPTION_BTN['values'] = result
            self.DUALEM_PORT_OPTION_BTN.set(result[0])
            self.GPS_PORT_OPTION_BTN.set(result[0])

            self.CONFIRM_BTN['state'] = tkinter.NORMAL
            self.status.set("CMD: SCAN PORTS\nSTATUS: OK ")
        else:
            self.GPS_PORT_OPTION_BTN.state(["disabled"])
            self.GPS_PORT_OPTION_BTN.set("USB NOT DETECTED")
            self.DUALEM_PORT_OPTION_BTN.state(['disabled'])
            self.DUALEM_PORT_OPTION_BTN.set("USB NOT DETECTED")
            self.CONFIRM_BTN['state'] = tkinter.DISABLED
            self.status.set("CMD: SCAN PORTS\nSTATUS: CHECK CONNECTION ")
        #self.SCAN_BTN.configure(text="RESCAN PORTS")
        self.CONFIRM_BTN.configure(bg="#c90231")
    
    def openFolder(self):
        try:
            filename = datetime.datetime.now().strftime("%d-%m-%Y")
        
            self.currentDir = filedialog.askdirectory()
            path = os.path.join(self.currentDir,'{}.txt'.format(filename))

            if not listdir(self.currentDir):
                self.START_SENSOR_BTN['state'] = tkinter.NORMAL
                self.status.set("CMD: SAVE PROJECT \nPATH: {}".format(path))
                self.SAVE_PROJECT_BTN.config(text="FOLDER SELECTED")
            else:
                self.status.set("CMD: SAVE PROJECT \nSTATUS: WARNING - FOUND EXISTING FILES")
                self.MAINFRAME.update()
                messagebox.showerror("WARNING: DIR NOT EMPTY", "Directory not empty!")
                OVERRIDE = messagebox.askyesno("WARNING!","Do you wish to override existing files?")
                if not OVERRIDE:
                    self.status.set("CMD: SAVE PROJECT \nSTATUS: RESELECT PROJECT FOLDER")
                    self.MAINFRAME.update()
                    self.openFolder()
                elif messagebox.askyesno("Confirm Action", "Are you sure you want to\n override files in this directory?"):
                    print("Override Confirmed")
                else:
                    None
        except Exception as e:
            print(e)
                

        
        # if self.currentDir:
        #     self.status.set("CMD: SAVE PROJECT \nCURRENT_PATH: {}".format(self.currentDir))
        #     self.SAVE_PROJECT_BTN.config(text="FOLDER SELECTED!")
        #     self.SAVE_PROJECT_BTN['state'] = tkinter.DISABLED
        #     #with open(path,'w') as outfile:
        #         #outfile.write("FILE CREATED")
        #     #print(listdir(path=self.currentDir))    
        #     print(path)    #    
    
    def readSensor(self):

        if self.port.get() == self.LEGAL_OPTIONS:
            self.proc = subprocess.Popen(['python3','readSENSOR.py', self.port.get()]) 
             # Run other script - doesn't wait for it to finish.
        print(self.proc.pid)
        if self.proc.pid:
               self.STOP_SENSOR_BTN['state'] = tkinter.NORMAL
        self.MAINFRAME.update() 
    
    def stop_sensor_process(self):
        try:
            if self.proc:
                self.proc.terminate()
                print("PROCESS: {} TERMINATED".format(self.proc.pid))
                return True
            return False

        except Exception as e:
            print("NO PROCESS TO TERMINATE")
            return False
        




    
if __name__ == "__main__":
    try:
        gui = GUI()
        gui.GUIMainloop()
    except Exception as e:
        print(e)
    finally:
        gui.stop_sensor_process()
        

        

