import pynmea2
import serial
import time
import os
import datetime
import json


class gpsSensor():
    '''
    A gps sensor class that initialises and reads gps serial data respectively.
    parameters:
        port, baudrate, timeout=1, mode='debug'
    returns:
        none
    '''
    def __init__(self, port, baudrate,timeout=1, mode='debug', filename=None):

        self.port = port
        self.baudrate = baudrate
        self.refreshrate = timeout
        self.mode = mode
        self.sanityCheck()
        self.tempLat = []
        self.tempLong =[]
        self.filename = filename

    def sanityCheck(self):
        self.allowed_modes = ['debug','prod']
        self.allowed_timeouts = [1,2,5,10 ]
        self.allowed_baudrates = [9600, 14400, 19200, 38400, 57600, 115200, 128000 , 256000]

        try:
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
        if   self.mode == 'debug' :    self.read_local_data()
        elif self.mode == 'prod'  :    self.read_live_data()
         
        else:
            print("Warning: acceptable values 'debug' or 'prod', check again.")
            return False
    
    def read_local_data(self):
        '''
        Warning: Only use in debug mode.
        parameters:
            None
        returns:
            list of valid data from the local sensor csv file
        '''

        # Parameters Setup
        file_name = 'gps-data.txt'

        #Output Path
        path = os.path.join( os.getcwd() , file_name )
        
        # Load the txt file in memory
        with open(path,'r') as gpsData:
            self.data = gpsData.readlines()
            gpsData.close()
        
        try:
            for eachLine in self.data:
                self.process_data(eachLine=eachLine)
        except Exception as e:
            print(e)
        finally:
            self.tempLong = []
            self.tempLat = []
        

        

    def process_data(self,eachLine):

        # Read each data points and parse it
            nmeaobj = pynmea2.parse( eachLine.strip() )
            self.tempLat.append(nmeaobj.latitude)
            self.tempLong.append(nmeaobj.longitude)
            with open(self.filename, 'w') as outputfile:
                data = [ list(points) for points in zip(self.tempLat,self.tempLong)]
                geojson = json.dumps({
                                        'LatLongs': data ,
                                        'live': [self.tempLat[-1],self.tempLong[-1]]
                                        }, indent = 4)
                outputfile.write(geojson)
                outputfile.close()
            print(nmeaobj.latitude,nmeaobj.longitude)
            time.sleep(self.refreshrate)
            #time.sleep(0.25)


    def process_data2(self,eachLine):

        # Read each data points and parse it
            nmeaobj = pynmea2.parse( eachLine.strip() )
            #self.tempLat.append(nmeaobj.latitude)
            #self.tempLong.append(nmeaobj.longitude)
            with open(self.filename, 'a') as outputfile:
                dualem=str(nmeaobj.data)+"\n"
                outputfile.write(dualem)
                outputfile.close()
            print(nmeaobj)
            time.sleep(0.01)
            

    def read_live_data(self):
        '''
        Read GPS Serial Data
        '''

        with serial.Serial(self.port, baudrate=self.baudrate, timeout=self.refreshrate) as ser:
            while True:
                try:
                    line = ser.readline().decode('ascii', errors='replace')
                    self.process_data2(eachLine=line)
                except Exception as e:
                    print(e)
                    continue
        
        
    