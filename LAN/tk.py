import socketserver
import http.server
import sys
import tkinter as tk


flag=1
class Th(socketserver.ThreadingMixIn,http.server.HTTPServer):
	def serve_forever(self):
		while flag:
			self.handle_request()
		pass
    #"""Handle one request at a time until doomsday."""

def start():
	port=8123
	server = Th(('localhost', port), http.server.SimpleHTTPRequestHandler)
	pid = server.serve_forever()

def stop():
	flag=0

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.start_serving()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def start_serving(self):
    	self.st = tk.Button(self)
    	self.st["text"] = "Start"
    	self.st["command"] = start
    	self.st.pack(side="top")
    	self.stop=tk.Button(self)
    	self.stop["text"]="stop"
    	self.stop["command"]=stop
    	self.stop.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
