
import unittest
from readDualem import readDualemSensor


class TestSensorReader(unittest.TestCase):

    def test_file(self):
        temp=  readDualemSensor
        self.assertEqual(temp.check_file_exist("./Data Reader/Textfile/GPSlog2021-09-23.txt"),True)

    


if __name__ == '__main__':
    unittest.main()
        

