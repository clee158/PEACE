import threading
import json, socket
from Tkinter import *
from PIL import Image, ImageTk

import App.constants as const
import cPickle


window = Tk()

def gui():
    pass

def window(filepath, data):
    # parse data

    # set up image
    img = Image.open(filepath)
    w, h = img.size

    # set up window
    window.title("Testing")
    window.configure(background='black')
    window.geometry("%dx%d" % (w+200, h+200))
    
    # set up image to be displayed
    img_tk = ImageTk.PhotoImage(img)
    
    # draw rectangle
    canvas = Canvas(window, width=w, height=h)
    canvas.pack()
    canvas.config(borderwidth=0, background='black', highlightcolor='black')
    canvas.create_image(0, 0, anchor=NW, image=img_tk)

    outlines = ['white', 'yellow', 'red', 'green', 'blue']
    canvas.create_rectangle(50, 50, 100, 100, width=1.5, outline='blue')

    # open window
    window.mainloop()

with open('../Downloads/data.txt') as json_file:
    data = json.load(json_file)
    window("./index.jpeg", data)


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("Socket creation failed with error %s" % err)

ip = const.gui_ip
port = const.gui_port
s.bind((ip, port))
s.listen(1)

while True:
    print("Listening on {}:{}...".format(ip,port))
    conn,address = s.accept()
    buf = conn.recv(1024)
    if len(buf) > 0:
        msg = cPickle.loads(buf)
        print msg

