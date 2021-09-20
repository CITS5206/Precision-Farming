from tkinter import *
from tkinter import messagebox
import serial
import sys
import glob
import webbrowser


import threading
import http.server
import socketserver


window = Tk()
window.title("Precision Farming App")
window.geometry('800x400')


lbl2 = Label(window, text="Scan Senor")
lbl2.grid(column=0, row=0)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)

def server():
    try:


        HOST, PORT = "localhost", 8080
        server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)

        with server:
            ip, port = server.server_address

       
            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.daemon = True
            server_thread.start()
            print("Server loop running in thread:", server_thread.name)


        # PORT = 8080
        # Handler = http.server.SimpleHTTPRequestHandler
        

        # with socketserver.TCPServer(("", PORT), Handler) as httpd:
        #     print("serving at port", PORT)
        #     httpd.serve_forever()
           # print(1)
            webbrowser.open('http://localhost:8080/')  # Go to web server 
            #exec(open('server.py').read())   # To access another python file 
    except:
        
        messagebox.showerror("showerror", "Error")




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

Start_server = Button(window, text="Start Server", command=server)

btn.grid(column=1, row=0)
btn2.grid(column=2, row=0)
mainrun.grid(column = 3, row=0)
Start_server.grid(column = 4, row=0)



window.mainloop()