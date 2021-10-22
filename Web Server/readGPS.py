# Code written by Arjun Panicker , Deepak Sugumaran and Harper Wu 
# Date 24/08/2021

from pynmea2 import nmea
import serial
import pynmea2
import time
import os
import json

jpath = '../Web Server/app/static/liveFeed'
project_path_json = os.path.join(jpath,'data.json')

with serial.Serial('/dev/tty.usbserial-1110', 
        baudrate=9600, timeout=1) as ser:
    # read 10 lines from the serial output
    lats=[]
    longs=[]
    while True:
        try:
            line = ser.readline().decode('ascii', errors='replace')
            #print(line.strip())
            if line.split(",")[0] in ['$GPGLL',]:
                nmeaobj = pynmea2.parse(line.strip())
                    
            
            
            # print(nmeaobj.fields)
                print(nmeaobj.latitude, nmeaobj.longitude)
                lats.append(nmeaobj.latitude)
                longs.append(nmeaobj.longitude)
                with open('gps_log_debug.txt','a') as outfile:
                    outfile.write(  line.strip()+"\n"
                                + "{} {}".format(nmeaobj.latitude,nmeaobj.longitude)
                                + "\n")
                with open(project_path_json, 'w') as outputfile:
                    data = [ list(points) for points in zip(lats,longs)]
                    geojson = json.dumps({
                                        'LatLongs': data ,
                                        'live': [lats[-1],longs[-1]]
                                        }, indent = 4)
                    outputfile.write(geojson)
                    outputfile.close()
            
            # print(nmeaobj.data)
            time.sleep(0.125)
            

        except Exception as e:
            print(e)
        