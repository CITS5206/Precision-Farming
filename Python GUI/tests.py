from tkinter import StringVar
import unittest
from main import GUI
from unittest.mock import Mock
import subprocess

class GUITestCase(unittest.TestCase):
    """ GUI test
    --- More Info Coming here soon ---
    """

    def test_GUI_startup(self):
        
        app = GUI()

        # Test Window Title
        title = app.WINDOW.title()
        expected='Precision Farming App'
        self.assertEqual(title,expected,title)
    
    def test_GUI_variables(self):
        app = GUI()

        self.assertTrue(type(app.port), StringVar())
        self.assertTrue(type(app.gps_port), StringVar())
        self.assertTrue(type(app.status), StringVar())
        self.assertTrue(type(app.proc), None)
        self.assertEqual(app.status.get(),'NO ACTIVITY',"ERR: Initial Activity Should be Zero")
    
    def test_GUI_SetupOptions_startup(self):
        app = GUI()
        self.assertTrue( app.SCAN_BTN['state'], 'normal')
        self.assertTrue( app.CONFIRM_BTN['state'], 'disabled')
        self.assertTrue( app.DUALEM_PORT_OPTION_BTN['state'], 'disabled')
        self.assertTrue( app.GPS_PORT_OPTION_BTN['state'], 'disabled')
    
    def test_GUI_SetupOptions_invalid(self):
        app = GUI()
        result = app.SCAN_BTN.invoke()
        self.assertTrue( app.SCAN_BTN['state'], 'normal')
        self.assertTrue( app.CONFIRM_BTN['state'], 'disabled')
        self.assertTrue( app.DUALEM_PORT_OPTION_BTN['state'], 'disabled')
        self.assertEqual(app.DUALEM_PORT_OPTION_BTN.get(), 'USB NOT DETECTED')
        self.assertTrue( app.GPS_PORT_OPTION_BTN['state'], 'disabled')
        self.assertEqual(app.GPS_PORT_OPTION_BTN.get(), 'USB NOT DETECTED')
        self.assertEqual(app.status.get(),"CMD: SCAN PORTS\nSTATUS: CHECK CONNECTION ")

    def test_StopSubProcess_invalid(self):
        app = GUI()
        self.assertFalse(app.stop_sensor_process(),False)
    
    def test_StopSubProcess_valid(self):
        app = GUI()
        # Create a dummy sub process
        app.proc = subprocess.Popen(['python3','-m','http.server','8000'])
        self.assertTrue(app.stop_sensor_process(),True)

    def test_readSensor_valid(self):
        app = GUI()
        app.port.set('/dev/tty.usbserial-AL02V3VW')
        result = [app.port.get() in app.LEGAL_OPTIONS]
        self.assertTrue(result[0],True)


if __name__ == '__main__':
    unittest.main()
    c = GUITestCase()
    c.test_GUI_startup()