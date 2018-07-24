import vlc, time
from mutagen.mp3 import MP3

import App.custom as custom
import App.constants as const

def play_sound(emotions):
    topResults = []
    sound_directory_path = "./sounds/"
    for obj in emotions:
        topResults.append(custom.get_keyOfTopValue(obj['emotion']))
    if const.SCARED in topResults:
        sound = sound_directory_path + const.SCARED_MP3
    elif const.FRUSTRATED in topResults:
        sound = sound_directory_path + const.FRUSTRATION_MP3
    elif const.SAD in topResults:
        sound = sound_directory_path + const.SAD_MP3
    else:
        sound = sound_directory_path + const.HAPPY_MP3

    p = vlc.MediaPlayer(sound)
    try:
        p.play()
        time.sleep(MP3(sound).info.length + 2)
    except:
        print("stopping sound")
        p.stop()
