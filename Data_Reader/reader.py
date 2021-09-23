import pynmea2
import serial
import time
import os.path
import datetime


path = './Data_reader/txt/'
date=str(datetime.date.today())
file_name_dual = 'Dualemdata'
file_name_gps = 'GPSdata'

dualfullpath=path+file_name_dual+date+".txt"
GPSfullpath=path+file_name_gps+".txt"




# Only works for the lasted txt file in the same day


class readSensor: 


    def check_file_exist(self,filepath):

        try:
            if os.path.isfile(filepath):
                return True
            else:
                return False
    
        except Exception as e: 
            print(e)
            

    def dualemsensor(self,port,baudrate):

        try: 

            with serial.Serial(port, baudrate, timeout=1, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE) as ser:
   
                while True:
                    try:
                    
                        if self.check_file_exist(dualfullpath):
                        
                            with open(dualfullpath,'a') as outfile:

                                line = ser.readline().decode('ascii', errors='replace')
                                nmeaobj = pynmea2.parse(line.strip())
                                outfile.write(str(nmeaobj.data)+"\n")
                        else: 

                            with open(dualfullpath,'w') as outfile:

                                line = ser.readline().decode('ascii', errors='replace')
                                nmeaobj = pynmea2.parse(line.strip())
                                outfile.write(str(nmeaobj.data)+"\n")
                        
                            

                                

                    except Exception as e:
                        print(e)
                        time.sleep(1)

        except Exception as e:
            print(e)


    def gpssensor(self,port,baudrate):
        try:
              with serial.Serial(port, baudrate, timeout=1) as ser:
                while True:
                    try:
                        
                        line = ser.readline().decode('ascii', errors='replace')
                        
                        nmeaobj = pynmea2.parse(line.strip())

                        if self.check_file_exist:
                            with open(GPSfullpath,'a') as outfile:
                            
                                outfile.csv.write( line.strip()+"\n"
                                + "{} {} {} ".format(nmeaobj.latitude,nmeaobj.longitude, nmeaobj.timestamp)
                                + "\n")
                                
                        else:
                            with open(GPSfullpath,'w') as outfile:
                            
                                outfile.csv.write( line.strip()+"\n"
                                + "{} {} {} ".format(nmeaobj.latitude,nmeaobj.longitude, nmeaobj.timestamp)
                                + "\n")


                    except Exception as e:
                        print(e)
                    time.sleep(1)
        except BaseException as e:
            print(e)

