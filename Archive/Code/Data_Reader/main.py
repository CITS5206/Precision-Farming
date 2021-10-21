import sys
from reader import readSensor
import time
from sensorCSV import creatCSVfile

if __name__ == "main":
    dualport =sys.argv[1]
    GPSport = sys.argv[2]
    



    #checks the input values of port and validate them 
    # Assigns the baurd rate for the function

    if(dualport != None and GPSport != None and GPSport == '/dev/tty.usbserial-AL02V3VW'): 
        gpsbaudrate=38400

    else: 
        dualbaudrate=96000


    sensor_obj = readSensor()
    csv_file=creatCSVfile()

    # Toggles betweent the two class to read the values from two sensor at time 
    # Sensor read value for 4 second and sleeps where gps reads for a second and sleeps 
    # The process will be killed by user in stop reading command from user in GUI 
    
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

    



 
   

    

    

    


