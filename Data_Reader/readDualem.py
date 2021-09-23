
import pynmea2
import serial
import time
import os.path
import datetime


# Needs Port number from main function

filename="./Data Reader/Textfile/SENSORlog"+str(datetime.date.today())+".txt";

class readDualemSensor: 




  
    def check_file_exist(self):

        try:
            if os.path.isfile(filename):
                return True
            else:
                return False
    
        except Exception as e: 
            print(e)
            
            



    def dualemsensor(port):

        try: 

            with serial.Serial(port, baudrate=38400, timeout=1) as ser:
                    while True:
                        try:
                            line = ser.readline().decode('ascii', errors='replace')
                            #print(line.strip())
                            nmeaobj = pynmea2.parse(line.strip())

                            #print(nmeaobj.latitude, nmeaobj.longitude, nmeaobj.timestamp)


                            # if check_file_exist():
                            #     with open(filename,"r+") as outfile:
                            #         outfile.write( line.strip()+"\n"
                            #                         + "{} {} {} ".format(nmeaobj.latitude,nmeaobj.longitude, nmeaobj.timestamp)
                            #                         + "\n")


                            # else:

                            with open(filename,'a') as outfile:
                                outfile.write( line.strip()+"\n"
                                    + "{} {} {} ".format(nmeaobj.latitude,nmeaobj.longitude, nmeaobj.timestamp)
                                    + "\n")

                        except Exception as e:
                            print(e)
                        time.sleep(1)

        except Exception as e:
            print(e)






    
