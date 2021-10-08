
import pynmea2
import serial
import time
from test import read_val

global csv_list
csv_list=[]

gps_flag, sensor_flag,csv_flag= False,True,False

class read_values:





    def read_sensor(sensor_port,sensor_rate,gps_port,gps_rate,time):

        try:
            sensor= serial.Serial(sensor_port, sensor_rate, timeout=1, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
            gps=serial.Serial(gps_port, gps_rate, timeout=1)
            sensor_test=open('sensor_log.txt','r')
            gps_test=open('gps_log.txt')

            while True:
                create_list=[]
                # open the serial ports
                        
                if sensor_flag:





                        # if sensor_flag:
                        #     sensor_line = sensor.readline().decode('ascii', errors='replace')
                        #     sensor_nmeaobj = pynmea2.parse(sensor_line.strip())
                        #     if(sensor_nmeaobj.data[0]=='H'):
                        #         for i in range(4):
                        #             create_list.append(sensor_nmeaobj.data)


                        #     if(len(create_list)==4):
                        #         gps_line = gps.readline().decode('ascii', errors='replace')
                        #         gps_nmeaobj = pynmea2.parse(gps_line.strip())
                        #         create_list.append("{} {} ".format(gps_nmeaobj.latitude,gps_nmeaobj.longitude))
                                

                        #     if csv_flag:
                        #         print(create_list)
                                




                        
                

            



            # if(flag == "sensor"):
            #     sensor_list=[]
            
            #     with serial.Serial(port, rate, timeout=1, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE) as ser:
                    
            #         while True:
            #             try:

                        
            #                 line = ser.readline().decode('ascii', errors='replace')
            #                 nmeaobj = pynmea2.parse(line.strip())
                            
                            
            #                 # To append 4 first 4 values from H to B in one list 
            #                 if(nmeaobj.data[0] == 'H' and count <3):
            #                     sensor_list.append(nmeaobj.data)
            #                     count=count+1

                            
            #             except:
            #                 pass
            
            # elif(flag== "gps"):
            #     gps_list=[]
            #     with serial.Serial(port, rate, timeout=1) as ser:
            #         while True:
            #             try:
                        
            #                 line = ser.readline().decode('ascii', errors='replace')
            #                 nmeaobj = pynmea2.parse(line.strip())

            #                 # To read first GPS value 
            #                 gps_list.append("{} {} ".format(nmeaobj.latitude,nmeaobj.longitude))

            #                 time.sleep(5)
            #             except:

            #                 pass


            
                        
        except:
            pass


    
    def create_csv():
        try:
            pass

            


        except:
            pass


       


               

            




      