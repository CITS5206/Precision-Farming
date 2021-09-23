import pynmea2
import serial
import time
import sys
import csv




def readGPSSensor(GPS_SENSOR='/dev/tty.usbserial-10'):
    
    with serial.Serial(GPS_SENSOR, baudrate=38400, timeout=1) as ser:
        while True:
            try:
                line = ser.readline().decode('ascii', errors='replace')
                print(line.strip())
                nmeaobj = pynmea2.parse(line.strip())
                print(nmeaobj.latitude, nmeaobj.longitude, nmeaobj.timestamp)
                with open('gps_data.txt','a') as outfile:
                    outfile.write(  line.strip()+"\n"
                                    + "{} {} {} ".format(nmeaobj.latitude,nmeaobj.longitude, nmeaobj.timestamp)
                                    + "\n")
                            

            except Exception as e:
                print(e)
            time.sleep(1)



def readSensor(SENSOR='/dev/tty.usbserial-10'):
# with serial.Serial('/dev/tty.usbserial-AL02V3VW',
    with serial.Serial(SENSOR, 
 
            baudrate=9600, timeout=1, 
            bytesize=serial.EIGHTBITS, 
            parity=serial.PARITY_NONE, 
            stopbits=serial.STOPBITS_ONE) as ser:
    # read 10 lines from the serial output
        while True:
            try:
                line = ser.readline().decode('ascii', errors='replace')
                print(line.strip())
                with open('dualem_sensor.txt','a') as outfile:
                    nmeaobj = pynmea2.parse(line.strip())
                    outfile.write(str(nmeaobj.data)+"\n")

            except Exception as e:
                print(e)
            time.sleep(1)



def readtxtfile():
    with open('dualem_sensor.txt', 'r') as sensor_file:

        sensor_list=[]
        sensor_data=sensor_file.readlines()

        for i in sensor_data:
           sensor_list.append(i.strip().replace('[','').replace(']','').replace("'",'').split(','))

        data_list=[]

        for i in range(0,len(sensor_list)):
           
            if sensor_list[i][0] =='H':
                
                c=sensor_list[i][1:] + sensor_list[i+1][2:] + sensor_list[i+2][1:] + sensor_list[i+3][1:]
                data_list.append(c)

    with open('log_sensor.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Timestamp [HhMmSs]',  'HCP conductivity of 0.5m array [mS/m]',    'HCP inphase of 0.5m array [ppt]',  'PRP conductivity of 0.5m array [mS/m]','PRP inphase of 0.5m array [ppt]',  'HCP conductivity of 1m array [mS/m]',  'HCP inphase of 1m array [ppt]',    'PRP conductivity of 1m array [mS/m]',  'PRP inphase of 1m array [ppt]',    'Voltage [V]'   ,'Temperature [deg]',   'Pitch [deg]',  'Roll [deg]',   'Acceleration X [gal]', 'Acceleration Y [gal]', 'Acceleration Z [gal]',    
        'Magnetic field X [nT]',    'Magnetic field Y [nT]',    'Magnetic field Z [nT]',    'Temperature [deg]'))

        writer.writerows(data_list)



    with open('gps_log.txt','r') as gps_file:

        gps_list=[]
        gps_data=gps_file.readlines()

        for i in range(len(gps_data)):
            if i%2 != 0 :
                temp = gps_data[i].strip().split(',')
                gps_list.append(temp[0].split(' '))

    with open('log.csv', 'w') as out_file:
        writer = csv.writer(out_file)

        writer.writerow(('Latitute','Lognigtute','TimeStamp'))
        writer.writerows(gps_list)



        

                # writer.writerow(('title', 'intro'))

       



        
            
       

        # for i in range (len(sensor_data)):
        #     if(sensor_data[i][0]=='H'):
        #         print(sensor_data[i][1:],sensor_data[i+1][2:])
                

            

            



    # with open('gps_log.txt','r') as gps_files:
    #     pass


        # stripped = (line.strip() for line in in_file)
        # lines = (line.split(",") for line in stripped if line)
        # with open('log.csv', 'w') as out_file:
        #     writer = csv.writer(out_file)

            
        #     writer.writerows(lines)
        
        





if __name__ == "__main__":
    #SENSOR = sys.argv[1]
    #GPS_SENSOR=sys.argv[2]
    #readSensor()
   #readGPSSensor(GPS_SENSOR)
    readtxtfile()
