import sys, socket, pickle

import App.constants as const
import App.validations as validations
import App.aws as aws
import App.emotion as emotion
import App.custom as custom
import App.sound as sound

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("Socket creation failed with error %s" % err)

ip = const.analysis_ip
port = const.analysis_port
s.bind((ip, port))
s.listen(1)

while True:
    print("Listening on {}:{}...".format(ip,port))
    conn,address = s.accept()
    buf = conn.recv(64)
    if len(buf) > 0:
        file_path = buf.decode('ascii')
        print(' [x] Msg Recieved: {}'.format(file_path))
#       file_path = sys.argv[-1]

        print(' [x] Check env')
        validations.env_check(const.ENV_VARS)

        print(' [x] Check file for validity')
        validations.check_file(file_path)

        print(' [x] Upload to S3')
        fileUrl = aws.upload_images(file_path)

       # print(' [x] Delete Local File')
       # validations.remove_file(file_path)

        print(' [x] Run Analysis')
        faces = emotion.analyze_file(fileUrl)

        print(' [x] Sort Result')
        results = custom.get_results(faces)

        msg = {
            "filepath":file_path,
            "results":results
        }
        #print(msg) 
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((const.gui_ip, const.gui_port))
        c.send(pickle.dumps(msg, protocol=2))
        print(" [x] sent!")

        #print(' [x] Display Result')
        #custom.print_result(emotions)
        print()
        #print(' [x] Play Sound')
        #sound.play_sound(emotions)
