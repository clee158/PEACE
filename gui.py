from Tkinter import *
from PIL import Image, ImageTk

import json, socket, cPickle, operator, os
import App.constants as const
import App.custom as custom

emotions = {'Happy':'green', 'Sad':'yellow', 'Frustrated':'purple', 'Scared':'red'}

def create_window(filepath, data):
    # set up image
    filepath = filepath.encode('ascii')
    f = open(filepath, 'rb')
    img = Image.open(f)
    w, h = img.size

    # set up window
    window = Tk()
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
        emotion = max(obj['emotion'].iteritems(), key=operator.itemgetter(1))[0]
        color = emotions[emotion]
        canvas.create_rectangle(x1, y1, x2, y2, width=1.5, outline=color)
        canvas.create_text(x1, y1-10,fill=color,text=emotion)
    
    # open window
    window.after(3000, window.destroy) 
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

while True:
    print("Listening on {}:{}...".format(ip,port))
    conn,address = s.accept()
    buf = conn.recv(1024)
    if len(buf) > 0:
        msg = cPickle.loads(buf)
        # create a new thread
        filepath = msg['filepath'].decode('utf-8')
        create_window(filepath, msg['results'])
        os.remove(filepath)
        
