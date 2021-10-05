
import pynmea2
import serial
import time
from test import read_val


class read_values:

    csv_list=[]
    def read_sensor(port,rate,time,flag):

        try:

            
            
            if(flag == "sensor"):
                sensor_list=[]
                with serial.Serial(port, rate, timeout=1, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE) as ser:
                    
                    while True:
                        try:

                        
                            line = ser.readline().decode('ascii', errors='replace')
                            nmeaobj = pynmea2.parse(line.strip())
                            
                            count=0
                            # To append 4 first 4 values from H to B in one list 
                            if(nmeaobj.data[0] == 'H' and count <3):
                                sensor_list.append(nmeaobj.data)
                                count=count+1

                            time.sleep(1)
                        except:
                            pass
            
            elif(flag== "gps"):
                gps_list=[]
                with serial.Serial(port, rate, timeout=1) as ser:
                    while True:
                        try:
                        
                            line = ser.readline().decode('ascii', errors='replace')
                            nmeaobj = pynmea2.parse(line.strip())

                            # To read first GPS value 
                            gps_list.append("{} {} {} ".format(nmeaobj.latitude,nmeaobj.longitude))

                            time.sleep(5)
                        except:

                            pass


            
                        
        except:
            pass


    
    def create_csv():
        try:
            pass

            


        except:
            pass


       


               

            




      