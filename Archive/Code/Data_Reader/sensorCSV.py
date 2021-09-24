

import csv
import datetime
import re
from typing import final


# Current datetime
datetoday=str(datetime.date.today())




sensortextpath='./Archive/Code/Data_Reader/Textfile/Dualemdata'+datetoday+'.txt'
gpstextpath='./Archive/Code/Data_Reader/Textfile/GPSdata'+datetoday+'.txt'

csvpath= './Archive/Code/Data_Reader/CSVfile/'

class creatCSVfile:

# This function is used to create the csv file for GPS and sensor using the text file that was generated in reader class
# reads the input values from both txt file and store them in seperate list
# The sensor data has single row value  for csv in 4 rows of txt file. so seperate if condition check for every 4 values and append it in one list
# Once the list is created using csv library the csv file is generarted with header 
# 2 csv files for sensor and gps and 1 csv file with metadata will be created in CSV file path
# All csv file will have timestamp attached to file name

    def readtxtfile(self):
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

        final_list=[]


        # loop that appends two list and creates the list with both values        
        for i in range(10):
            new_list=[]
            new_list.append(gps_list[i][0])
            new_list.append(gps_list[i][1])
            for j in data_list[i]:
                new_list.append(j)
            final_list.append(new_list)


        # Creates the meta data csv

        with open(csvpath+'MetaData'+datetoday+'.csv','w') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(('Latitute','Lognigtute','Timestamp [HhMmSs]',  'HCP conductivity of 0.5m array [mS/m]',    'HCP inphase of 0.5m array [ppt]',  'PRP conductivity of 0.5m array [mS/m]','PRP inphase of 0.5m array [ppt]',  'HCP conductivity of 1m array [mS/m]',  'HCP inphase of 1m array [ppt]',    'PRP conductivity of 1m array [mS/m]',  'PRP inphase of 1m array [ppt]',    'Voltage [V]'   ,'Temperature [deg]',   'Pitch [deg]',  'Roll [deg]',   'Acceleration X [gal]', 'Acceleration Y [gal]', 'Acceleration Z [gal]', 'Magnetic field X [nT]',    'Magnetic field Y [nT]',    'Magnetic field Z [nT]',    'Temperature [deg]'))
                writer.writerows(final_list)




temp = creatCSVfile()

temp.readtxtfile()



        
