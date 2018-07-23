import pygame, uuid, socket
import pygame.camera
import App.constants as const

clientSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pygame.init()
pygame.camera.init()
camlist = pygame.camera.list_cameras()

if len(camlist) > 0:
    cam = pygame.camera.Camera(camlist[0], (640,480))
    cam.start()
    img = cam.get_image()
    full_path = const.IMG_FILE_PATH + str(uuid.uuid4())+ '.jpg'
    pygame.image.save(img, full_path)
    clientSoc.connect((const.analysis_ip,const.analysis_port))
    clientSoc.send(full_path.encode('ascii'))
    print(' [x] Sent: {}'.format(full_path))
else:
    print("No Camera detected. Please connect your camera")
