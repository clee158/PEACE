import sys, socket

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
print("Listening on {}:{}...".format(ip,port))

while True:
    conn,address = s.accept()
    buf = conn.recv(64)
    if len(buf) > 0:
        file_path = buf.decode('ascii')
        print(' [x] Recieved: {}'.format(file_path))
#       file_path = sys.argv[-1]

        print('Check env')
        validations.env_check(const.ENV_VARS)

        print('Check file for validity')
        validations.check_file(file_path)

        print('Upload to S3')
        fileUrl = aws.upload_images(file_path)

        print('Delete Local File')
        validations.remove_file(file_path)

        print('Run Analysis')
        faces = emotion.analyze_file(fileUrl)

        print('Sort Result')
        emotions = custom.sort_results(faces)

        print('Display Result')
        custom.print_result(emotions)

        print('Play Sound')
        sound.play_sound(emotions)
