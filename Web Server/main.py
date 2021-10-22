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
import pynmea2
import csv
import itertools
import json




class GUI():
    """ EMI Toolkit GUI Class
        :parameters:
            None
        :methods:
            confirm_selection(),
            scanPorts(),
            saveProject(),
            readSensor(),
            stopSensor(),
        
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
        '''
        Initialise the MainLoop
        '''
        self.WINDOW.mainloop()    

    def GUIWindow(self):
        '''
        Initialise Gui Window
        '''

        #INITIALIZE GUI WINDOW
        self.WINDOW = Tk()
        self.WINDOW.title("EMI Toolkit")
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
            self.button_padding_y = 5
            self.combo_box_width = 20
            self.sep_padding_y = 5
            self.sep_padding_x = 0
            self.text_padding_x = 0
            self.text_padding_y = 2
            self.label_font = 'Helvetica 12 bold'
            self.button_font = 'Helvetica 10'
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
            self.webserver_isAlive = False

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
            self.EXISTING_FOLDER_BTN = Button(self.MAINFRAME, text="OUTPUT FOLDER", command=self.projectOutput,width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y, state="disabled")
            self.PREV_PROJECTS_BTN = Button(self.MAINFRAME, text="PREVIOUS PROJECTS", command=self.prevProjects,width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y, state="normal")

            # END : FILE OPTIONS
   
    def GUIControlOPtions(self):

            # START : CONTROL OPTIONS
            self.CONTROL_LABEL = ttk.Label(self.MAINFRAME, text='CONTROL PANEL',justify=tkinter.CENTER,font=self.label_font)
            self.START_SENSOR_BTN = Button(self.MAINFRAME,text="START SENSOR READING",command=self.readSensor, state="disabled",width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y)
            self.STOP_SENSOR_BTN = Button(self.MAINFRAME,text="STOP SENSOR READING", command=self.stopSensor, state="disabled",width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y)
            self.READ_OP_DATA = Button(self.MAINFRAME,text="ENABLE LIVE OUTPUT", command=self.toggleOutput, state="normal",width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y)

            # END : CONTROL OPTIONS

    def GUIVisualOptions(self):
            
            # START: VISUALIZATION
            self.VISUAL_LABEL = ttk.Label(self.MAINFRAME, text='VISUALIZATION',justify=tkinter.CENTER,font=self.label_font)
            self.START_WEBSEVER_BTN = Button(self.MAINFRAME,text="START WEBSERVER",command=self.startWebserver, state="disabled",width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y)
            self.STOP_WEBSEVER_BTN = Button(self.MAINFRAME,text="STOP WEBSERVER",command=self.stopWebserver, state="disabled",width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y)
            self.OPEN_WEBSEVER_BTN = Button(self.MAINFRAME,text="OPEN WEB BROWSER",command=self.openBrowser, state="disabled",width=self.button_width,padx=self.button_padding_x,pady=self.button_padding_y)

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
        if self.DUALEM_PORT.get() == "SENSOR PORT" or  self.GPS_PORT.get() == "GPS PORT":
            self.PROGRAM_STATUS.set("Command: Scan Ports\nStatus: Port Selection Error")
            self.MAINFRAME.update()
            messagebox.showwarning(title="WARNING",message= "PORT SELECTION ERROR")

        elif self.DUALEM_BAUD.get() == 'BAUD RATE' or self.GPS_BAUD.get()== 'BAUD RATE':
            self.PROGRAM_STATUS.set("Command: Confirm Selection\nStatus: Baud Rate Not Set")
            self.MAINFRAME.update()
            messagebox.showwarning(title="WARNING",message= "BAUD RATE NOT SELECTED")

        elif self.DUALEM_FREQ.get()=='FREQUENCY (M.P.S)' or self.GPS_FREQ.get() == 'FREQUENCY (M.P.S)':
            self.PROGRAM_STATUS.set("Command: Confirm Selection\nStatus: Frequency Rate Not Set")
            self.MAINFRAME.update()
            messagebox.showwarning(title="WARNING",message= "Frequency Not Set")

        else:
            self.PROGRAM_STATUS.set("Command: Confirm Selection\nStatus: OK")
            #self.START_WEBSEVER_BTN['state'] = tkinter.NORMAL
            self.GUISelectionToggle()

        
    def GUISelectionToggle(self):
        '''
        Function to toggle selection on or off
        '''
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
            self.PROGRAM_OS = 'win'
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
            self.PROGRAM_OS = 'unix'
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
            self.PROGRAM_OS = 'mac'
        else:
            raise EnvironmentError('Unsupported platform')

        result = ['Demo'] # Remove this in production software
        
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
            if len(s)>2:
                self.DUALEM_PORT_OPTION_BTN.set(s[2])
            else:
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
            if len(g)>3:
                self.GPS_PORT_OPTION_BTN.set(g[3])
            elif len(g)>2:
                self.GPS_PORT_OPTION_BTN.set(g[2])
            else:
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
            #jpath = os.path.join(os.path.expanduser('~'),'Desktop','Web Server','app','static','liveFeed')
            jpath = '../Web Server/app/static/liveFeed'


            if not os.path.exists(opath):
                    os.mkdir(opath)
            filename = datetime.datetime.now().strftime("data-%d-%m-%Y-%H-%M-%S")
        
            self.pwd = filedialog.askdirectory(initialdir=opath)
            print(self.pwd)
            self.project_path = os.path.join(self.pwd,'{}.csv'.format(filename))
            self.project_path_raw = os.path.join(self.pwd,'{}.txt'.format(filename))
            self.project_path_json = os.path.join(jpath,'data.json')



            if not os.path.exists(self.project_path):
                self.START_SENSOR_BTN['state'] = tkinter.NORMAL
                self.PROGRAM_STATUS.set("Command: SAVE PROJECT \nPATH: {}".format(self.project_path))
                self.SAVE_PROJECT_BTN.config(text="FOLDER SELECTED")
                self.EXISTING_FOLDER_BTN['state'] = tkinter.NORMAL
            else:
                self.PROGRAM_STATUS.set("Command: SAVE PROJECT \nSTATUS: WARNING - FOUND EXISTING FILES")
                self.MAINFRAME.update()
                messagebox.showwarning(title="WARNING",message= "Directory not empty")
                if messagebox.askyesno("Confirm Action", "Overwrite files in this directory?"):
                        self.START_SENSOR_BTN['state'] = tkinter.NORMAL 
                        self.PROGRAM_STATUS.set("Command: SAVE PROJECT \nPATH: {}".format(self.project_path))
                        self.SAVE_PROJECT_BTN.config(text="FOLDER SELECTED")
                        self.EXISTING_FOLDER_BTN['state'] = tkinter.NORMAL
                else:
                        self.PROGRAM_STATUS.set("Command: SAVE PROJECT \nSTATUS: RESELECT PROJECT FOLDER")
                        self.MAINFRAME.update()
        except Exception as e:
            print(e)
            self.EXISTING_FOLDER_BTN['state'] = tkinter.DISABLED

    def readSensor(self):
        if os.path.exists(self.project_path):
            filename = datetime.datetime.now().strftime("data-%d-%m-%Y-%H-%M-%S")
            self.project_path = os.path.join(self.pwd,'{}.csv'.format(filename))
            self.project_path_raw = os.path.join(self.pwd,'{}.txt'.format(filename))

        def readserial_Demo(self,path=self.project_path):

            f1 = open("dualem-data.txt",'r')
            f2 = open("gps-data.txt",'r')
            dualem = iter(f1.readlines())
            gps = iter(f2.readlines())
            f1.close()
            f2.close()
            with open(f"{path}",'w') as outfile:
                writer = csv.writer(outfile)
                writer.writerow((
                                    'Latitude',
                                    'Longitude',
                                    'Timestamp [HhMmSs]',  
                                    'HCP conductivity of 0.5m array [mS/m]',    
                                    'HCP inphase of 0.5m array [ppt]',  
                                    'PRP conductivity of 0.5m array [mS/m]',
                                    'PRP inphase of 0.5m array [ppt]',  
                                    'HCP conductivity of 1m array [mS/m]',  
                                    'HCP inphase of 1m array [ppt]',    
                                    'PRP conductivity of 1m array [mS/m]',  
                                    'PRP inphase of 1m array [ppt]',    
                                    'Voltage [V]'   ,
                                    'Temperature [deg]',   
                                    'Pitch [deg]',  
                                    'Roll [deg]',   
                                    'Acceleration X [gal]', 
                                    'Acceleration Y [gal]', 
                                    'Acceleration Z [gal]',    
                                    'Magnetic field X [nT]',    
                                    'Magnetic field Y [nT]',    
                                    'Magnetic field Z [nT]',    
                                    'Temperature [deg]'
                                    ))
            outfile.close()
            lats=[]
            longs=[]
            while self.threadFlag:
                checklist=[]
                output_list=[]
                try:
                    nmeaobj = pynmea2.parse(dualem.__next__().strip())
                    if nmeaobj.data[0] == 'H':
                        for i in range(4):
                                checklist.append(nmeaobj.data)
                                nmeaobj = pynmea2.parse(dualem.__next__().strip())
                        g_data = pynmea2.parse(gps.__next__())
                        checklist.append([g_data.latitude, g_data.longitude])
                        lats.append(g_data.latitude)
                        longs.append(g_data.longitude)
                        with open(self.project_path_json, 'w') as outputfile:
                            data = [ list(points) for points in zip(lats,longs)]
                            geojson = json.dumps({
                                        'LatLongs': data ,
                                        'live': [lats[-1],longs[-1]]
                                        }, indent = 4)
                            outputfile.write(geojson)
                            outputfile.close() 
                    if self.PROGRAM_STATUS_OP:
                        self.PROGRAM_STATUS.set(f"Command: Live Output\nSensor-Data:{nmeaobj.data}\nGPS-Data: {g_data.latitude},{g_data.longitude}")
                    else:
                        self.PROGRAM_STATUS.set(f"Command: Disable Live Output\nSensor-Data: ---\nGPS-Data: --- ")
                    time.sleep(2)
                except Exception as e:
                    print(e)
                if len(checklist) ==5:
                        output_list = checklist[4]+ checklist[0][1:] + checklist[1][2:] + checklist[2][1:] + checklist[3][1:]
                        with open(f"{path}",'a') as outfile:
                            writer = csv.writer(outfile)
                            print(output_list)
                            writer.writerow(output_list)
                            outfile.close()
  
                if not self.threadFlag:
                    print(f"Terminated {threading.current_thread().name}")
                          
        def readserial_Prod(self,path=self.project_path):
            if not os.path.exists(path):
                print("File Doesnt exist, creating one...")
                with open(f"{path}",'w') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow((
                                    'Latitude',
                                    'Longitude',
                                    'Timestamp [HhMmSs]',  
                                    'HCP conductivity of 0.5m array [mS/m]',    
                                    'HCP inphase of 0.5m array [ppt]',  
                                    'PRP conductivity of 0.5m array [mS/m]',
                                    'PRP inphase of 0.5m array [ppt]',  
                                    'HCP conductivity of 1m array [mS/m]',  
                                    'HCP inphase of 1m array [ppt]',    
                                    'PRP conductivity of 1m array [mS/m]',  
                                    'PRP inphase of 1m array [ppt]',    
                                    'Voltage [V]'   ,
                                    'Temperature [deg]',   
                                    'Pitch [deg]',  
                                    'Roll [deg]',   
                                    'Acceleration X [gal]', 
                                    'Acceleration Y [gal]', 
                                    'Acceleration Z [gal]',    
                                    'Magnetic field X [nT]',    
                                    'Magnetic field Y [nT]',    
                                    'Magnetic field Z [nT]',    
                                    'Temperature [deg]'
                                    ))
                    outfile.close()
            
            try:
                    sensor = serial.Serial(
                            port=self.DUALEM_PORT.get(),
                            baudrate=int(self.DUALEM_BAUD.get()),
                            timeout=int(self.DUALEM_FREQ.get()),
                            parity=serial.PARITY_NONE,
                            bytesize=serial.EIGHTBITS,
                            stopbits=serial.STOPBITS_ONE)
                    gps = serial.Serial(
                            port=self.GPS_PORT.get(),
                            baudrate=int(self.GPS_BAUD.get()),
                            timeout=int(self.GPS_FREQ.get()),
                            parity=serial.PARITY_NONE,
                            bytesize=serial.EIGHTBITS,
                            stopbits=serial.STOPBITS_ONE)
            except Exception as e:
                    print(e)
                    return False
            lats=[]
            longs=[]
            while self.threadFlag:
                    outputlist = []
                    try:
                        temp=""
                        
                        sensor_obj = pynmea2.parse(sensor.readline().decode('ascii', errors='replace').strip())
                        gps_line = gps.readline().decode('ascii', errors='replace').strip()
                        if gps_line.split(",")[0] in ['$GPGLL']:
                            gps_obj = pynmea2.parse(gps_line)
                            temp += f"{gps_obj.latitude},{gps_obj.longitude}"
                            lats.append(gps_obj.latitude)
                            longs.append(gps_obj.longitude)
                            with open(self.project_path_json, 'w') as outputfile:
                                data = [ list(points) for points in zip(lats,longs)]
                                geojson = json.dumps({
                                        'LatLongs': data ,
                                        'live': [lats[-1],longs[-1]]
                                        }, indent = 4)
                                outputfile.write(geojson)
                                outputfile.close()
                        else:
                            temp += f"{0},{0}"                 
                        for field in sensor_obj.data:
                            temp+= f",{field}"
                        
                        with open(f"{self.project_path_raw}",'a') as outfile:
                            outfile.write(f"{temp}\n")
                            outfile.close
                        if self.PROGRAM_STATUS_OP:
                            self.PROGRAM_STATUS.set(f"Command: Live Output\nSensor-Data:{sensor_obj.data}\nGPS-Data: {gps_obj.latitude},{gps_obj.longitude}")
                        else:
                            self.PROGRAM_STATUS.set(f"Command: Disable Live Output\nData: --- ")

                        print(temp)
                        time.sleep(0.125)
                    except Exception as e:
                            self.PROGRAM_STATUS.set(f"ERROR: CHECK PORTS!")
                            continue
            if not self.threadFlag:
                    print(f"Terminated {threading.current_thread().name}")

        self.threadFlag = True
        if not self.DUALEM_PORT.get()=='Demo' and not self.GPS_PORT.get() == 'Demo':
            print("Startring Thread for readSerial()")
            self.worker = threading.Thread(target=readserial_Prod,name="DemoSerialProd", args=(self,self.project_path), daemon=True)
            self.worker.start()
        if self.DUALEM_PORT.get()=='Demo' and self.GPS_PORT.get() == 'Demo':
            print("Startring Demo Thread for readSerial()")
            self.worker = threading.Thread(target=readserial_Demo,name="DemoSerialDemo", args=(self,self.project_path), daemon=True)
            self.worker.start()
        

        self.STOP_SENSOR_BTN['state'] = tkinter.NORMAL
        self.START_SENSOR_BTN['state'] = tkinter.DISABLED
        self.START_WEBSEVER_BTN['state'] = tkinter.NORMAL
        self.MAINFRAME.update() 
    
    def stopSensor(self):
        '''
        Function to stop sensor reading
        '''
        def generateCSV():
            '''
            Generate final csv and delete temp files
            '''
            if os.path.exists(self.project_path):
                f = open(self.project_path_raw,'r').readlines()
                for i in range(len(f)):
                    try:
                        if f[i].split(",")[2] == 'H':
                            c = f[i].split(",")[0:2]+f[i].split(",")[3:] + f[i+1].split(",")[4:] + f[i+2].split(",")[3:]+f[i+3].split(",")[3:]
                            with open(self.project_path,'a') as outfile:
                                writer = csv.writer(outfile)
                                writer.writerow(c)
                                outfile.close()                           
                    except Exception as e:
                        print(e)
                        pass
            #os.remove(self.project_path_raw)

        try:
            self.threadFlag = False
            if os.path.exists(self.project_path_raw):
                generateCSV()
            self.START_SENSOR_BTN['state'] = tkinter.NORMAL
            self.STOP_SENSOR_BTN['state'] = tkinter.DISABLED
            self.START_WEBSEVER_BTN['state'] = tkinter.DISABLED
            self.PROGRAM_STATUS.set(f"Command: STOP SENSOR \nSTATUS: Sensor Reading Stopped")
            return True

        except Exception as e:
            print(e)
            return False
        
    def prevProjects(self):
        '''
        Function to open ~/User/Downloads/EMI-Toolkit/ Folder
        '''
        opath = os.path.join(os.path.expanduser('~'),'Documents','EMI-Toolkit')
        if not os.path.exists(opath):
                    os.mkdir(opath)
        try:
            if self.PROGRAM_OS == 'unix':
                subprocess.Popen(['pcmanfm',opath])
            else:
                subprocess.Popen(['open',opath])
        except Exception as e:
            print(e)

    def projectOutput(self):
        '''
        Function to open ~/User/Downloads/EMI-Toolkit/ {path}
        '''

        try:
            if os.path.exists(self.pwd):
                if self.PROGRAM_OS == 'unix':
                    subprocess.Popen(['pcmanfm',f"{self.pwd}/"])
                else:
                    subprocess.Popen(['open',f"{self.pwd}/"])
        except Exception as e:
            print(e)

    def toggleOutput(self):
        if self.READ_OP_DATA.cget('text') == "ENABLE LIVE OUTPUT":
            self.READ_OP_DATA.config(text='DISABLE LIVE OUTPUT')
        elif self.READ_OP_DATA.cget('text') == 'DISABLE LIVE OUTPUT':
            self.READ_OP_DATA.config(text='ENABLE LIVE OUTPUT')
        self.PROGRAM_STATUS_OP = not self.PROGRAM_STATUS_OP

    def startWebserver(self):
        '''
        Function to start the webserver
        '''

        if os.path.exists("server.py"):
            print("Found sever")
            try:
                self.server = subprocess.Popen(["python3", "server.py"])
                self.PROGRAM_STATUS.set(f"Command: START WEBSERVER \nSTATUS: Server: {self.server.pid} ID is running.")
                self.webserver_isAlive = True
            except Exception as e:
                print(e)
                self.START_WEBSEVER_BTN['state'] = tkinter.DISABLED

            self.START_WEBSEVER_BTN['state'] = tkinter.DISABLED
            self.STOP_WEBSEVER_BTN['state'] = tkinter.NORMAL
            self.OPEN_WEBSEVER_BTN['state'] = tkinter.NORMAL

        else:
            self.START_WEBSEVER_BTN['state'] = tkinter.DISABLED
            self.OPEN_WEBSEVER_BTN['state'] = tkinter.DISABLED

    def stopWebserver(self):
        '''
        Function to stop the webserver
        '''
        try:
            if self.webserver_isAlive:
                self.server.terminate()
                self.webserver_isAlive = False
            self.PROGRAM_STATUS.set(f"Command: START WEBSERVER \nSTATUS: Server: {self.server.pid} ID is terminated.")
            self.START_WEBSEVER_BTN['state'] = tkinter.NORMAL
            self.STOP_WEBSEVER_BTN['state'] = tkinter.DISABLED
            self.OPEN_WEBSEVER_BTN['state'] = tkinter.DISABLED

        except:
            print("webserver not running")
            
    def openBrowser(self):
        '''
        Function to open default web browser port = 3152
        '''
        if self.webserver_isAlive:
            webbrowser.open("http:localhost:3152")
            self.PROGRAM_STATUS.set(f"Command: OPEN WEBSERVER \nSTATUS: Server: 'http:localhost:3152' ")
        else:
            self.PROGRAM_STATUS.set(f"Command: OPEN WEBSERVER \nSTATUS: Server is not running. ")


if __name__ == "__main__":
    try:
        gui = GUI()
        gui.GUIMainloop()
    except Exception as e:
        print(e)
    finally:
        gui.stopSensor()
        

        

