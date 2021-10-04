from sensor import Sensor

#dualem = Sensor(port=8888,baudrate=9600,sensorType='soil')
gps = Sensor(port="8882",baudrate=38400,sensorType='gps',timeout=1 ,mode='debug')

#dualem.dataout()
gps.readData()