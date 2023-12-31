import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

did_key = os.getenv("DID")

url = "https://api.d-id.com/talks"

def post_req(text):
    payload = {
        "script": {
            "type": "text",
            "subtitles": "false",
            "provider": {
                "type": "microsoft",
                "voice_id": "en-US-JennyNeural"
            },
            "ssml": "false",
            "input": text
        },
        "config": {
            "fluent": "false",
            "pad_audio": "0.0"
        },
        "source_url": "https://media.discordapp.net/attachments/1008571129012695100/1108694757259104256/daisuke-nagoya_Cinema_shooting_scene_of_a_Japanese_lady_is_watc_1044d115-1f26-443a-a703-2f1e0b231db7.png"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": did_key 
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()['id']
    # print(response.text)