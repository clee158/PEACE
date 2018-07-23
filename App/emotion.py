import requests, os
import App.constants as const

def analyze_file(image_url):
    request_data = {'url': image_url}
    request_headers = {
        'Content-Type': "application/json",
        'Ocp-Apim-Subscription-Key': os.environ[const.API_KEY]
    }

    response = requests.post(const.FACE_API_URL, 
                             params=const.REQUEST_PARAMS, 
                             headers=request_headers, 
                             json=request_data
    )

    return response.json()
