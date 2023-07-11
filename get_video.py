import requests
import json
from dotenv import load_dotenv
load_dotenv()
import os

did_key = os.getenv("DID")
headers = {
    "accept": "application/json",
    "authorization": did_key
}

def get_url(id):
    url = "https://api.d-id.com/talks/{}".format(id)
    response = requests.get(url, headers=headers)
    video_url = response.json()['result_url']
    # print(response.text)
    return video_url 