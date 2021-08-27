# Code written by Arjun Panicker , Deepak Sugumaran and Harper Wu 
# Date 24/08/2021

from pynmea2 import nmea
import serial
import pynmea2
import time

with serial.Serial('/dev/tty.usbserial-AL02V3VW', 
        baudrate=38400, timeout=1) as ser:
    # read 10 lines from the serial output
    while True:
        try:
            line = ser.readline().decode('ascii', errors='replace')
            print(line.strip())
            nmeaobj = pynmea2.parse(line.strip())
            # print(nmeaobj.fields)
            print(nmeaobj.latitude, nmeaobj.longitude, nmeaobj.timestamp)
            with open('gps_log.txt','a') as outfile:
                outfile.write(  line.strip()+"\n"
                                + "{} {} {} ".format(nmeaobj.latitude,nmeaobj.longitude, nmeaobj.timestamp)
                                + "\n")
            
            # print(nmeaobj.data)
            

        except Exception as e:
            print(e)
        time.sleep(1)