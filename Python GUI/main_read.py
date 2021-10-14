
from tkinter.constants import OUTSIDE
import pynmea2
import itertools
import time
import serial
import csv
import sys


def main(SENSOR ='/dev/tty.usbserial-1110', path=''):
    op = path
    f1 = open("dualem-data.txt",'r')
    f2 = open("gps-data.txt",'r')
    with open(f"{op}",'a') as outfile:
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



    dualem = iter(f1.readlines())
    gps = iter(f2.readlines())
    f1.close()
    f2.close()
    outfile.close()


    readSensor, readGPS, compile2 = True,True,False
    

    ser = serial.Serial(SENSOR, 
                                baudrate=9600, timeout=1, 
                                bytesize=serial.EIGHTBITS, 
                                parity=serial.PARITY_NONE, 
                                stopbits=serial.STOPBITS_ONE)
    if ser.is_open:
        while True:
            #firstH = False
            checklist=[]
            output_list =[]
            if readSensor:
                try:
                    nmeaobj = pynmea2.parse(ser.readline().decode('ascii', errors='replace').strip())
                    #if not firstH:
                    if nmeaobj.data[0] == 'H':
                            #firstH = True
                        for i in range(4):
                                checklist.append(nmeaobj.data)
                                nmeaobj = pynmea2.parse(ser.readline().decode('ascii', errors='replace').strip())
                        g_data = pynmea2.parse(gps.__next__())
                        checklist.append([g_data.latitude, g_data.longitude])

                except Exception as e:
                    print(e)
                    continue
            for k in checklist:
                print(k)
        #print(len(checklist))
            if len(checklist) ==5:
                h = checklist[0]
                i = checklist[1]
                a = checklist[2]
                b = checklist[3]
                g = checklist[4]
                output_list = g+ h[1:] + i[2:] + a[1:] + b[1:]
                with open(f"{op}",'a') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(output_list)
            
    
if __name__ == "__main__":
    SENSOR = sys.argv[1]
    path = sys.argv[2]
    main(SENSOR,path)



