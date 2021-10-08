
import time
from threading import  Thread
import pynmea2
#import multiprocessing



def sensor_value():
    new_list=[]
    with open('./Archive/Logs/sensor_log.txt') as f:
        lines = f.readlines()

        for i in lines:
                
            nmeaobj = pynmea2.parse(i.strip())

            print(nmeaobj.data[0])
                
            # print((str(nmeaobj.data).split()[0])

                
                
            time.sleep(1)


def gps_value():
    list_gps=[]
    with open('./Archive/Logs/gps_log.txt') as f:
        lines=f.readlines()
        
        for i in range(len(lines)):
            if(i%2 == 0):
                nmeaobj = pynmea2.parse(lines[i].strip())           
                                    
                list_gps.append(str("{} {} ".format(nmeaobj.latitude,nmeaobj.longitude)+"\n"))

        with open("gpsdata_log.txt",'w') as outfile:
                                
            outfile.write(str(list_gps))

            outfile.close()
                





def function1():
    count=0
    while count>=0:
        count=count+1
        time.sleep(1)
        print("fun1-"+str(count))
        


def function2():
    count=0
    while count>=0:
        count=count+1
        time.sleep(5)
        print("fun2-"+str(count))



gps_value()


# main_thread= Thread(target=function1)
# main_thread.start()

# sub_thread=Thread(target=function2)
# sub_thread.start()





