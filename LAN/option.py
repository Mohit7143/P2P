import requests,json
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

url = 'http://127.0.0.1:8000/'

def select():
	global choice
	global url
	sf = var.get()
	payload = {'id' : sf}
	q = requests.get(url + 'find',params=payload)
	data = json.loads(q.text)
	ip_list['menu'].delete(0, 'end')
	if not data:
		ip_list['menu'].add_command(label="None active Seeder's", command=tk._setit(vr,"None active Seeder's"))
	else:
		for choice in data:
			ip_list['menu'].add_command(label=choice['pk'], command=tk._setit(vr, choice['pk']))

def slct():
	pid = vr.get()
	file = var.get()
	payload = {'pid' : vr.get(),'file' : var.get()}
	q = requests.get(url + 'up',params=payload)
	pass

root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (800, 600, 800, 800))
root.title("tk.Optionmenu as combobox")


var = tk.StringVar(root)
p = requests.get(url + 'get/')
data = json.loads(p.text)
choices = []
for item in data:
	choices.append(item['fields']['name'])
var.set("List of file's")

option = tk.OptionMenu(root, var, *choices)
option.pack(side='left', padx=20, pady=20)
button = tk.Button(root, text="check value selected", command=select)
button.pack(side='left', padx=20, pady=10)

choice = []
vr = tk.StringVar(root)
vr.set("List of seeder's")
choice.append('No list Available')
ip_list = tk.OptionMenu(root, vr, *choice)
ip_list.pack(side='left', padx=16, pady=16)

bttn = tk.Button(root, text="Download", command=slct)
bttn.pack(side='left', padx=25, pady=25)

root.mainloop()
