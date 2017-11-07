import socketserver
import http.server
import sys,time,subprocess,os,signal
import tkinter as tk
from tkinter import ttk
from threading import Thread
from uuid import getnode as get_mac
import requests

flag=1
server_ip = '127.0.0.1'
mac = get_mac()
payload = {'mac': mac}

class Th(socketserver.ThreadingMixIn,http.server.HTTPServer):
    pass
    #"""Handle one request at a time until doomsday."""
port = 8123
server = Th(('0.0.0.0', port), http.server.SimpleHTTPRequestHandler)

def start():
    global server
    global flag
    flag = 1
    while flag==1:
        server.handle_request()
    #server.serve_forever()

def ack():
    global flag
    flag = 1
    global server_ip
    while flag==1:
        p = requests.get(server_ip,params=payload)
        time.sleep(60)

#def shut():
    #global server
    #server.shutdown()
    #server.close()

def stop():
    global server
    global flag
    flag = 0
    #tm = Thread(target=shut)
    #tm.deamon = True
    #tm.start()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.start_serving()

    def start_serving(self):
        self.e=tk.Entry(root)
        self.e.pack()
        self.e.focus_set()
        self.st = tk.Button(self)
        self.st["text"] = "Start"
        self.st["command"] = self.action
        self.st.pack(side="top")
        self.stop=tk.Button(self)
        self.stop["text"]="stop"
        self.stop["command"]=stop
        self.stop.pack(side="bottom")
    
    def action(self):
        global server
        global server_ip
        server_ip = "http://" + self.e.get()
        thread = Thread(target = start)
        thread.deamon = False
        thread.start()
        another = Thread(target = ack)
        another.deamon = False
        another.start()

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
