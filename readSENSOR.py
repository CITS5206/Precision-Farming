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
                
                # print(nmeaobj.data)
                

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

        sensor_data=sensor_file.readlines()


        for i in range (len(sensor_data)):
            

            print(sensor_data.strip())



    with open('gps_log.txt','r') as gps_files:
        pass


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
