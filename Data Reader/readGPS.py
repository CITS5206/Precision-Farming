import pynmea2
import serial
import time
import os.path
import datetime


filename="./Data Reader/Textfile/GPSlog"+str(datetime.date.today())+".txt";


class readGPSData:

    def check_file_exist(self):
    
        try:
            if os.path.isfile(filename):
                return True
            else:
                return False
    
        except Exception as e: 
            print(e)

    def readGPSSensor(gps_port):
        try:

            with serial.Serial(gps_port, baudrate=38400, timeout=1) as ser:
                while True:
                    try:
                        line = ser.readline().decode('ascii', errors='replace')
                        #print(line.strip())
                        nmeaobj = pynmea2.parse(line.strip())

                        #print(nmeaobj.latitude, nmeaobj.longitude, nmeaobj.timestamp)

                        # ****** Need to check if file exists or not

                        with open('gps_data.txt','a') as outfile:
                            outfile.write(  line.strip()+"\n"
                                            + "{} {} {} ".format(nmeaobj.latitude,nmeaobj.longitude, nmeaobj.timestamp)
                                            + "\n")
                                
                    except Exception as e:
                        print(e)
                    time.sleep(1)
        except BaseException as e:
            print(e)