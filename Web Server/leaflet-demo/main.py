import threading
from gpsSensor import gpsSensor

#dualem = Sensor(port=8888,baudrate=9600,sensorType='soil')
#gps = gpsSensor(port="/dev/tty.usbserial-1110",baudrate=9600,timeout=1 ,mode='prod',filename='dualem.txt')
gps2 = gpsSensor(port="8882",baudrate=38400,timeout=1 ,mode='debug',filename='d.json')

#dualem.dataout()
#gps_task_1 = threading.Thread(target=gps.readData)
gps_task_2 = threading.Thread(target=gps2.readData)

#gps_task_1.start()
gps_task_2.start()

#gps_task_1.join()
gps_task_2.join()
print("END OF PROGRAM")





