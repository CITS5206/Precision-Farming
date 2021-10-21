import pynmea2
import serial
import time
import os
import datetime
import json



class Sensor():
    '''
    A sensor class that initialises and reads serial data respectively.
    parameters:
        port, baudrate, sensortype, mode='debug'
    returns:
        none
    '''
    def __init__(self, port, baudrate, sensorType,timeout=1, mode='debug'):

        self.port = port
        self.baudrate = baudrate
        self.sensorType = sensorType
        self.refreshrate = timeout
        self.mode = mode
        
        self.sanityCheck()

    def sanityCheck(self):
        self.allowed_modes = ['debug','prod']
        self.allowed_timeouts = [1,2,5,10 ]
        self.allowed_baudrates = [9600, 14400, 19200, 38400, 57600, 115200, 128000 , 256000]
        self.allowed_types = ['gps', 'dualem', 'test']

        try:
            if self.sensorType not in self.allowed_types: raise TypeError("Warning: Unable to determine the right sensor type; Accetpable values: 'dualem', 'gps' ")
            if self.baudrate not in self.allowed_baudrates: raise TypeError("Warning: Please use appropriate baudrates!")
            if self.refreshrate not in self.allowed_timeouts: raise TypeError("Warning: use 1,2 or 5 seconds")
            if self.mode not in self.allowed_modes: raise TypeError("Warning: acceptable values 'debug' or 'prod', check again.")
            if not isinstance(self.port,str): raise TypeError("Warning: Serial Ports mismatch")
        except Exception as e:
            print(e)
    
    def readData(self):
        '''
        if debug, read local data;
        if prod, read sensor data;
        else flash warning!
        
        '''
        if self.mode == 'debug':
            self.readLocalData()
        elif self. mode == 'prod':
            self.readSensorData()
        else:
            print("Warning: acceptable values 'debug' or 'prod', check again.")
    
    def readLocalData(self):
        '''
        Warning: Only use in debug mode.
        parameters:
            self
        returns:
            list of valid data from the local sensor csv file
        '''
        p = os.getcwd()
        f_name = self.sensorType+'-data.txt'
        path = os.path.join(p,f_name)
        
        with open(path,'r') as file:
            f = file.readlines()
            file.close()
        
        lats=[]
        longs=[]
        
        for line in f:
                nmeaobj = pynmea2.parse(line.strip())
                # print(nmeaobj.fields)
                lats.append(nmeaobj.latitude)
                longs.append(nmeaobj.longitude)
                with open("gps-data.json", 'w') as outputfile:
                    outputfile.write( json.dumps({'LAT': lats, 'LONG': longs, 'CURRENT_POS': [lats[-1],longs[-1]]},indent=4))
                    outputfile.close()
                print(nmeaobj.latitude,nmeaobj.longitude)
                time.sleep(self.refreshrate)
        #print(lats)
        #print(longs)

    def readSensorData(self):
        '''
        Read Serial Data
        '''
    