import pynmea2
import serial
import time
import os.path
import datetime



# Globlal variables

path = './Data_Reader/Textfile/'
date=str(datetime.date.today())
file_name_dual = 'Dualemdata'
file_name_gps = 'GPSdata'

dualfullpath=path+file_name_dual+date+".txt"
GPSfullpath=path+file_name_gps+".txt"



class readSensor: 

    # Checks the file exist in the path or not 
    # Parameter input path value
    # parameter output boolean
    def check_file_exist(self,filepath):

        try:
            if os.path.isfile(filepath):
                return True
            else:
                return False
    
        except Exception as e: 
            print(e)

    # This function takes the port and baurd rate for Dualem sensor values as input 
    # Uses Serial class from piserial to read stream input values from the passed port number and specific barud rate
    # With reading the values as list of ascii values  uses the pynmea class and object to parse the ascci format 
    # Formated values in written into txt file to specific text file folder path  
    # The text file name will have timestamp atttached with it    

    def dualemsensor(self,port,baudrate):

        try: 

            with serial.Serial(port, baudrate, timeout=1, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE) as ser:
   
                while True:
                    try:
                    
                        line = ser.readline().decode('ascii', errors='replace')
                        if self.check_file_exist(dualfullpath):
                            
                            with open(dualfullpath,'a') as outfile:
                                nmeaobj = pynmea2.parse(line.strip())
                                outfile.write(str(nmeaobj.data)+"\n")
                        else: 

                            with open(dualfullpath,'w') as outfile:
                                nmeaobj = pynmea2.parse(line.strip())
                                outfile.write(str(nmeaobj.data)+"\n")
                        
                            

                                

                    except Exception as e:
                        print(e)
                        time.sleep(1)

        except Exception as e:
            print(e)


     # This function takes the port and baurd rate  for GPS values as input 
    # Uses Serial class from piserial to read stream input values from the passed port number and specific barud rate
    # With reading the values as list of ascii values  uses the pynmea class and object to parse the ascci format 
    # Formated values in written into txt file to specific text file folder path  
    # The text file name will have timestamp atttached with it  

    def gpssensor(self,port,baudrate):
        try:
              with serial.Serial(port, baudrate, timeout=1) as ser:
                while True:
                    try:
                        
                        line = ser.readline().decode('ascii', errors='replace')
                        
                        

                        if self.check_file_exist:
                            with open(GPSfullpath,'a') as outfile:
                                nmeaobj = pynmea2.parse(line.strip())
                            
                                outfile.write(  line.strip()+"\n"
                                + "{} {} {} ".format(nmeaobj.latitude,nmeaobj.longitude, nmeaobj.timestamp)
                                + "\n")
            
                                
                        else:
                            with open(GPSfullpath,'w') as outfile:
                                nmeaobj = pynmea2.parse(line.strip())
                                outfile.write(  line.strip()+"\n"
                                + "{} {} {} ".format(nmeaobj.latitude,nmeaobj.longitude, nmeaobj.timestamp)
                                + "\n")


                    except Exception as e:
                        print(e)
                    time.sleep(1)
        except BaseException as e:
            print(e)

