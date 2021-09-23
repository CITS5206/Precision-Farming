
import serial
import time
import sys
import csv
import datetime
import re


datetoday=str(datetime.date.today())

# Only works for the lasted txt file in the same day

sensortextpath='./Data Reader/Textfile/SENSORlog'+datetoday+'.txt'
gpstextpath='./Data Reader/Textfile/GPSlog'+datetoday+'.txt'

csvpath= './Data Reader/CSVfile/'

class creatCSVfile:

    def readtxtfile(self):

        # Read the txt file generate from program

        with open(sensortextpath, 'r') as sensor_file:

            sensor_list=[]
            sensor_data=sensor_file.readlines()

            for i in sensor_data:
                sensor_list.append(i.strip().replace('[','').replace(']','').replace("'",'').split(','))

            data_list=[]

            for i in range(0,len(sensor_list)):
            
                if sensor_list[i][0] =='H':
                    
                    c=sensor_list[i][1:] + sensor_list[i+1][2:] + sensor_list[i+2][1:] + sensor_list[i+3][1:]
                    data_list.append(c)

        # Created the CSV file for sensor data

        with open(csvpath+'DUALEMdata'+datetoday+'.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('Timestamp [HhMmSs]',  'HCP conductivity of 0.5m array [mS/m]',    'HCP inphase of 0.5m array [ppt]',  'PRP conductivity of 0.5m array [mS/m]','PRP inphase of 0.5m array [ppt]',  'HCP conductivity of 1m array [mS/m]',  'HCP inphase of 1m array [ppt]',    'PRP conductivity of 1m array [mS/m]',  'PRP inphase of 1m array [ppt]',    'Voltage [V]'   ,'Temperature [deg]',   'Pitch [deg]',  'Roll [deg]',   'Acceleration X [gal]', 'Acceleration Y [gal]', 'Acceleration Z [gal]',    
            'Magnetic field X [nT]',    'Magnetic field Y [nT]',    'Magnetic field Z [nT]',    'Temperature [deg]'))

            writer.writerows(data_list)


        # Reads the GPS txt file  generates from program
        with open(gpstextpath,'r') as gps_file:

            gps_list=[]
            gps_data=gps_file.readlines()

            for i in range(len(gps_data)):
                if i%2 != 0 :
                    temp = gps_data[i].strip().split(',')
                    gps_list.append(temp[0].split(' '))




        # Creates CSV file to folder         

        with open(csvpath+'GPSdata'+ datetoday +'.csv', 'w') as out_file:
            writer = csv.writer(out_file)

            writer.writerow(('Latitute','Lognigtute','TimeStamp'))
            writer.writerows(gps_list)




temp = creatCSVfile()

temp.readtxtfile()



        
