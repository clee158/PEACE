import App.constants as const
import uuid, pickle, socket, json

filepath = "index.jpg"

def get_emotion(h,s,f,c):
    return {
        "happy": h,
        "sad": s,
        "frustrated": f,
        "scared": c
    }

def get_face(x,y,w,h,e):
    return {
        "id":uuid.uuid4(),
        "x-axis":x,
        "y-axis":y,
        "width":w,
        "height":h,
        "emotion":e
    }

obj = {
    "filepath":filepath,
    "results": [
        get_face(200,200,20,20,get_emotion(.8,.1,.08,.02)),
        get_face(400,350,30,40,get_emotion(.7,.1,.1,.1)),
        get_face(600,430,20,20,get_emotion(.1,0,0,0,))
    ]
}

#print(obj)
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((const.gui_ip, const.gui_port))
c.send(pickle.dumps(obj,protocol=2))
print(" [x] sent!")
