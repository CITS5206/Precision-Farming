from threading import Thread
import time
import serial.tools.list_ports
from Readvalues import read_values


def checking_ports(port, baud_rate):
    for i in list(serial.tools.list_ports.comports()):  # check the port match
        if(i == port and baud_rate == 38400):
            return True
        elif(i==port and baud_rate == 9000):
            return True


def main_call(sensor_port,sensor_baud_rate,gps_port,gps_baud_rate,interval):
    try:
        if(checking_ports(sensor_port,sensor_baud_rate)):
            if(checking_ports(gps_port,gps_baud_rate)):
                
                sensorthread=Thread(target=read_values.read_sensor(sensor_port,sensor_baud_rate,interval,"Sensor"))
                sensorthread.start()

                gpsthread=Thread(target=read_values.read_sensor(gps_port,gps_baud_rate,interval,"GPS"))
                gpsthread.start()

                time.sleep(10)

                

            else:
                print("GPS port not found")

        else:
            print("Sensor port not found")



    except:
        pass



    finally:

        pass

 
# def func1():
#     count=1
#     while count < 10:
#         count=count+1
#         print('1')
#         time.sleep(4)

# def func2():
#     count=1
#     while count <10 :
#         count=count+1
#         print('2')
#         time.sleep(1)

# if __name__ == '__main__':
#     #Thread(target = func1).start()
#     #Thread(target = func2).start()
#     checking_ports()
