import sys
from reader import readSensor
import time
from sensorCSV import creatCSVfile

if __name__ == "main":
    dualport =sys.argv[1]
    GPSport = sys.argv[2]
    



    #check the values of port and validate 


    if(dualport != None and GPSport != None and GPSport == '/dev/tty.usbserial-AL02V3VW'): 
        gpsbaudrate=38400

    else: 
        dualbaudrate=96000


    sensor_obj = readSensor()
    csv_file=creatCSVfile()

    while True:
        while FLAG:
            #do this for 4 seconds
            sensor_obj.dualemsensor(dualport,dualbaudrate)
            time.sleep(4)
            FLAG = False

        while not FLAG:
            sensor_obj.gpssensor(GPSport,gpsbaudrate)
            FLAG = True
        time.sleep(1)

    



 
   

    

    

    


