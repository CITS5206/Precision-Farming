
# The University of Western Australia : 2021

# CITS5206 Professional Computing

# Group: Precision Farming

# Source Code

# Author: Deepakraj Sugumaran

# Co-Author: Arjun Panicker

# Date Created:

# Last Modified:

# Version: [Major Versions needs to be pushed in Github!]

# State : [Stable]


import pynmea2
import serial
import csv


#check the file existing or not 
# if existing pass parameter a or pass parameter w to csv write

# check the port numbers valid or not

# add time stamp to the file name 


def read_sensor():


    with open("./dualem-gps.csv",'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(
        (
         'Latitude',
         'Longitude',
         'Timestamp [HhMmSs]',  
         'HCP conductivity of 0.5m array [mS/m]',    
         'HCP inphase of 0.5m array [ppt]',  
         'PRP conductivity of 0.5m array [mS/m]',
         'PRP inphase of 0.5m array [ppt]',  
         'HCP conductivity of 1m array [mS/m]',  
         'HCP inphase of 1m array [ppt]',    
         'PRP conductivity of 1m array [mS/m]',  
         'PRP inphase of 1m array [ppt]',    
         'Voltage [V]'   ,
         'Temperature [deg]',   
         'Pitch [deg]',  
         'Roll [deg]',   
         'Acceleration X [gal]', 
         'Acceleration Y [gal]', 
         'Acceleration Z [gal]',    
         'Magnetic field X [nT]',    
         'Magnetic field Y [nT]',    
         'Magnetic field Z [nT]',    
         'Temperature [deg]')
         )
        outfile.close()

    try:

        sensor= serial.Serial('/dev/tty.usbserial-120', 9600, timeout=1, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
        #gps=serial.Serial(gps_port, gps_rate, timeout=1)

        sensor_flag=True
        first_elem=False

        gps=[-31.977426123666667, 115.81717328233333]
        
        while True:
           
            sensor_list=[]
            csv_list=[]
            try:
                nmeaobj = pynmea2.parse(sensor.readline().decode('ascii', errors='replace').strip())

                if not first_elem:
                    if nmeaobj.data[0]=='H':
                        sensor_list.append(nmeaobj.data)
                        first_elem=True
                        
                        for i in range(4):
                            sensor_list.append(nmeaobj.data)
                            nmeaobj = pynmea2.parse(sensor.readline().decode('ascii', errors='replace').strip())
                                        
                    #g_data = pynmea2.parse(gps.readline().decode('ascii', errors='replace').strip())
                    #sensor_list.append(["{} {} {} ".format(g_data.latitude,g_data.longitude)])
                    sensor_list.append(["{} {}".format(gps[0],gps[1])])


                else:
                    for i in range(4):
                        sensor_list.append( nmeaobj.data)
                        nmeaobj = pynmea2.parse(sensor.readline().decode('ascii', errors='replace').strip())
                    #g_data = pynmea2.parse(gps.readline().decode('ascii', errors='replace').strip())
                    #sensor_list.append(["{} {} {} ".format(g_data.latitude,g_data.longitude)])
                    sensor_list.append(["{} {}".format(gps[0],gps[1])])




            except Exception as e:
                print(e)
                continue

            if len(sensor_list) == 5:
                h = sensor_list[0]
                i = sensor_list[1]
                a = sensor_list[2]
                b = sensor_list[3]
                g = sensor_list[4]
                csv_list =  g + h[1:] + i[1:] + a[1:] + b[1:]
                #print(len(sensor_list))

                with open("./dualem-gps.csv",'a') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(csv_list)    


                    outfile.close()
            
    except Exception as e:
        print(e)


read_sensor()
        
        




            




      