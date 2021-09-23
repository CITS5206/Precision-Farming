import datetime
import os
import unittest
from reader import readSensor

class TestSensorReader(unittest.TestCase):

    # Test case to check  sensor file exits in the path 

    def test_checkfile(self):
        

        with open("./Data_Reader/test.txt",'a') as outfile:
            outfile.write("Test")
        temp =  readSensor()
        
        self.assertEqual(temp.check_file_exist("./Data_Reader/test.txt"),True)
        self.assertEqual(temp.check_file_exist("./Data_Reader/test123.txt"),False)

        os.remove("./Data_Reader/test.txt")

    
        

if __name__ == '__main__':
    unittest.main()
        

