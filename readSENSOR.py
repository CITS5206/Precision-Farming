# import pynmea2
# import 

# file = open('a.txt')

# for line in file.readlines():
#     try:
#         msg = pynmea2.parse(line)
#         print(msg.data)
#     except pynmea2.ParseError as e:
#         print('Parse error: {}'.format(e))
#         continue

import serial
import pynmea2
import time

with serial.Serial('/dev/tty.usbserial-AL02V3VW', 
        baudrate=9600, timeout=1, 
        bytesize=serial.EIGHTBITS, 
        parity=serial.PARITY_NONE, 
        stopbits=serial.STOPBITS_ONE) as ser:
    # read 10 lines from the serial output
    while True:
        try:
            line = ser.readline().decode('ascii', errors='replace')
            print(line.strip())
            # with open('gps_log.txt','a') as outfile:
                # outfile.write(line.strip()+"\n")
            # nmeaobj = pynmea2.parse(line.strip())
            # print(nmeaobj.data)

        except Exception as e:
            print(e)
        time.sleep(1)