from tkinter import *
from tkinter import messagebox
import serial
import sys
import glob
import webbrowser
from threading import Thread

import threading
import http.server
import socketserver
import glob

ROOT_DIR = '.'

window = Tk()
window.title("Precision Farming App")
window.geometry('800x400')


lbl2 = Label(window, text="Scan Senor")
lbl2.grid(column=0, row=0)

web_server_status = False 





    #Thread(target=server, daemon=True).start()
   


def server():
    try:


        PORT = 8080
        Handler = http.server.SimpleHTTPRequestHandler

        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            
            httpd.serve_forever()

       
    except:
       
        messagebox.showerror("showerror", "Error")


def openWebsite():
    try:
       
        webbrowser.open('http://localhost:8080/') 
       



    except:
        messagebox.showerror("showerror", "Error")






def check_file_exist(filename):
    #shows all directories with csv files
    text_files_csv = glob.glob(ROOT_DIR + "/**/" + filename, recursive = True)
    #print("type of: ",type(text_files_csv))

    if not text_files_csv: #if text_files_csv is an empty list, no file is found
        print("File does not exist in the directory.")
    else: 
        print("File exists in: ", text_files_csv)

   


####m Main of Program ####
file_name = "infoc.json"
check_file_exist(file_name)




def mainprogram():
    lbl2.configure( text="Programming Started")

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    lbl2.configure(text=result)
    return result
    

btn = Button(window, text="Default Ports", command=serial_ports)
btn2 = Button(window, text="Rescan", command=serial_ports)
mainrun = Button(window, text="Start MainProgram", command=mainprogram)

Start_server = Button(window, text="Start Server", command=Thread(target=server, daemon=True).start())
Open_Application= Button(window, text="Open Application", command=openWebsite)


locatefile = Button(window, text="Locate Map File", command=check_file_exist)

btn.grid(column=1, row=0)
btn2.grid(column=2, row=0)
mainrun.grid(column = 3, row=0)
Start_server.grid(column = 4, row=0)
Open_Application.grid(column = 5, row=0)
locatefile.grid(column = 6, row=0)



window.mainloop()