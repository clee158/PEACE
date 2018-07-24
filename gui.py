import ast
from threading import *
from collections import OrderedDict
import json, socket
from Tkinter import *
from PIL import Image, ImageTk
import logging

import App.constants as const
import cPickle

window = Tk()
emotions = {'happy':'green', 'sad':'yellow', 'frustrated':'purple', 'scared':'red'}

def create_window(filepath, data):
    # set up image
    img = Image.open(filepath)
    w, h = img.size

    # set up window
    window.title(filepath)
    window.configure(background='black')
    window.geometry("%dx%d" % (w+200, h+200))
    
    # set up image to be displayed
    img_tk = ImageTk.PhotoImage(img)
    
    # draw rectangle
    canvas = Canvas(window, width=w, height=h)
    canvas.pack()
    canvas.config(borderwidth=0, background='black', highlightcolor='black')
    canvas.create_image(0, 0, anchor=NW, image=img_tk)
    for obj in data:
        x1 = obj['x-axis']
        y1 = obj['y-axis']
        x2 = x1 + obj['width']
        y2 = y1 + obj['height']
        emotion = obj['emotion'].keys.index(max(obj['emotion'].values()))
        #emotion = list(obj['emotion'].keys())[0]
        color = emotions[emotion]
        canvas.create_rectangle(x1, y1, x2, y2, width=1.5, outline=color)
        canvas.create_text(x1, y1-10,fill=color,text=emotion)
    
    # open window
    window.mainloop()

## main start
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("Socket creation failed with error %s" % err)

ip = const.gui_ip
port = const.gui_port
s.bind((ip, port))
s.listen(1)

t = None

while True:
    print("Listening on {}:{}...".format(ip,port))
    conn,address = s.accept()
    buf = conn.recv(1024)
    if len(buf) > 0:
        msg = cPickle.loads(buf)
        # if there is a existing thread kill it
        if t is not None and t.isAlive():
            t._Thread_stop()
       
        #create a new thread
        filepath = msg['filepath'].decode('utf8')
        results = msg['results']
        t = Thread(name='blocking', target=gui(), args=(filepath, results))
        t.start()
 
        #for thread in enumerate():
        #  if thread.isAlive():
        #       thread._Thread_stop()
        
        #print msg
        #for person in msg['results']:
        #    print person['emotion']
        #print msg['filepath'].decode('utf8')
