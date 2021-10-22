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
        title = app.WINDOW.title()
        expected="EMI Toolkit"
        self.assertEqual(title,expected,title)
    
    def test_GUI_variables(self):
        app = GUI()
        self.assertTrue(type(app.DUALEM_BAUD), StringVar())
        self.assertTrue(type(app.DUALEM_PORT), StringVar())
        self.assertTrue(type(app.DUALEM_FREQ), StringVar())
        self.assertTrue(type(app.GPS_BAUD), StringVar())
        self.assertTrue(type(app.GPS_BAUD), StringVar())
        self.assertTrue(type(app.GPS_BAUD), StringVar())
        self.assertFalse(app.PROGRAM_STATUS_OP)
        self.assertFalse(app.webserver_isAlive)


if __name__ == '__main__':
    unittest.main()