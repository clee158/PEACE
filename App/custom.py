import App.constants as const

def sort_results(faces):
    emotions = []
    #print(faces)
    for face in faces:
        emotion_result = face['faceAttributes']['emotion']
        person = []
        # Good
        person.append([
            const.HAPPY,
            emotion_result['happiness'] + emotion_result['neutral'] + emotion_result['contempt']
        ])
        # Sad
        person.append([
            const.SAD,
            emotion_result['sadness']
        ])
        # Frustrated
        person.append([
            const.FRUSTRATED,
            emotion_result['anger'] + emotion_result['disgust']
        ])
        # Scared
        person.append([
            const.SCARED,
            emotion_result['fear'] + emotion_result['surprise']
        ])

        emotions.append(sorted(person, key=lambda tup: tup[1], reverse=True))

    return emotions

def print_result(emotions):
    for emotion in emotions:
        print("-----------------------------------------------------------------")
        for e in emotion:
            bar = "|" * int(e[1] * 100 / 2)
            print("{} : {} {}%".format(e[0], bar, e[1] * 100))

