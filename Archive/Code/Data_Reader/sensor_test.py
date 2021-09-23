import datetime
import os
import unittest
from reader import readSensor
from sensorCSV import creatCSVfile

class TestSensorReader(unittest.TestCase):

    # Test case to check  sensor file exits in the path 

    def test_checkfile(self):
        

        with open("./Archive/Code/Data_Reader/test.txt",'a') as outfile:
            outfile.write("Test")
        temp =  readSensor()
        
        self.assertEqual(temp.check_file_exist("./Archive/Code/Data_Reader/test.txt"),True)
        self.assertEqual(temp.check_file_exist("./Archive/Code/Data_Reader/test123.txt"),False)

        os.remove("./Archive/Code/Data_Reader/test.txt")

    
    # def test_createcsv_sensor(self):
    #     temp = creatCSVfile()
    #     temp.readtxtfile()
    #     date=str(datetime.date.today())
    #     val=os.path.isfile("./Archive/Code/Data_Reader/CSVfile/DUALEMdata"+date+".csv")
    #     self.assertEquals(val,True)
    #     if val:
    #         os.remove("./Archive/Code/Data_Reader/CSVfile/DUALEMdata"+date+".csv")
        
        
    def test_createcsv(self):
        temp1 = creatCSVfile()
        temp1.readtxtfile()
        date=str(datetime.date.today())
        val=os.path.isfile("./Archive/Code/Data_Reader/CSVfile/DUALEMdata"+date+".csv")
        val1=os.path.isfile("./Archive/Code/Data_Reader/CSVfile/GPSdata"+date+".csv")
        val2=os.path.isfile("./Archive/Code/Data_Reader/CSVfile/Metadata"+date+".csv")
        self.assertEquals(val1,True)
        self.assertEquals(val2,True)
        self.assertEquals(val,True)
        
        if val1 and val and val:
            os.remove("./Archive/Code/Data_Reader/CSVfile/GPSdata"+date+".csv")
            os.remove("./Archive/Code/Data_Reader/CSVfile/DUALEMdata"+date+".csv")
            os.remove("./Archive/Code/Data_Reader/CSVfile/Metadata"+date+".csv")



    

    

if __name__ == '__main__':
    unittest.main()
        

