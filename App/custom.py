import operator
import App.constants as const

def get_emotion(h,s,f,c):
    return {
        "Happy": h,
        "Sad": s,
        "Frustrated": f,
        "Scared": c
    }

def get_face(uid,x,y,w,h,e):
    return {
        "id":uid,
        "x-axis":x,
        "y-axis":y,
        "width":w,
        "height":h,
        "emotion":e
    }


def get_results(faces):
    results = []
    for face in faces:
        # emotion creation
        e = face['faceAttributes']['emotion']
        emotion = get_emotion(
            e['happiness'] + e['neutral'] + e['contempt'],
            e['sadness'],
            e['anger'] + e['disgust'],
            e['fear'] + e['surprise']
        )
        # face creation
        loc = face['faceRectangle']
        results.append(get_face(
            face['faceId'],
            loc['left'],
            loc['top'],
            loc['width'],
            loc['height'],
            emotion
        ))
    return results

def get_keyOfTopValue(emotions):
    return max(emotions.items(), key=operator.itemgetter(1))[0]


def print_result(emotions):
    for emotion in emotions:
        print("-----------------------------------------------------------------")
        for e in emotion:
            bar = "|" * int(e[1] * 100 / 2)
            print("{} : {} {}%".format(e[0], bar, e[1] * 100))

