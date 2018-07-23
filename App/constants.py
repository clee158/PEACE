API_KEY = "APIKEY"
ACCESS_KEY = "ACCESSKEY"
SECRET_KEY = "SECRETKEY"

ENV_VARS = [API_KEY, ACCESS_KEY, SECRET_KEY]

IMG_FILE_PATH = "pics/"

BUCKET_NAME = "rating-imgs"

FACE_API_URL = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"

FRUSTRATED = "Frustrated"
SCARED     = "Scared    "
SAD        = "Sad       "
HAPPY      = "Happy     "

SCARED_MP3 = "slowDown.mp3"
FRUSTRATION_MP3 = "frustration.mp3"
SAD_MP3 = "checkOnPassenger.mp3"
HAPPY_MP3 = "good.mp3"

REQUEST_PARAMS = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion'
}

# Analysis.py
analysis_ip="localhost"
analysis_port=8081

# gui.py
gui_ip="localhost"
gui_port=8082
