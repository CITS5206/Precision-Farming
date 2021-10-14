
# The University of Western Australia : 2021

# CITS5206 Professional Computing

# Group: Precision Farming

# Source Code

# Author:

# Co-Author:

# Date Created:

# Last Modified:

# Version: [Major Versions needs to be pushed in Github!]

# State : [Stable]


import itertools
import pynmea2
import serial
import time
import csv

def read_sensor(sensor_port,sensor_rate,gps_port,gps_rate,time):
    

    try:
        sensor= serial.Serial(sensor_port, sensor_rate, timeout=1, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        gps=serial.Serial(gps_port, gps_rate, timeout=1)

        sensor_flag=True
        first_elem=False

        
        while True:
           
            sensor_list=[]
            csv_list=[]
            if sensor_flag:
                try:
                    nmeaobj = pynmea2.parse(sensor.readline().decode('ascii', errors='replace').strip())
                    if not first_elem:
                        if nmeaobj.data[0]=='H':
                            sensor_list.append(nmeaobj.data)
                            first_elem=True
                            for i in range(4):
                                sensor_list.append(nmeaobj.data)
                                nmeaobj = pynmea2.parse(sensor.readline().decode('ascii', errors='replace').strip())
                        g_data = pynmea2.parse(gps.readline().decode('ascii', errors='replace').strip())
                        sensor_list.append([g_data.latitude, g_data.longitude])


                    else:
                        for i in range(4):
                            sensor_list.append( nmeaobj.data)
                            nmeaobj = pynmea2.parse(sensor.readline().decode('ascii', errors='replace').strip())
                        g_data = pynmea2.parse(gps.readline().decode('ascii', errors='replace').strip())
                        sensor_list.append(["{} {} {} ".format(g_data.latitude,g_data.longitude)])




                except Exception as e:
                    print(e)
                    continue

            # for k in sensor_list:
            #     print(k)


            if len(sensor_list) ==5:
                h = sensor_list[0]
                i = sensor_list[1]
                a = sensor_list[2]
                b = sensor_list[3]
                g = sensor_list[4]
                csv_list = g+ h[1:] + i[1:] + a[1:] + b[1:]
                with open("./outpu/dualem-gps.csv",'a') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(csv_list)    

            
    except Exception as e:
        print(e)
        
        




            




      