# from gradio_client import Client

# client = Client("https://malay-91418-image-info.hf.space/--replicas/ljhkq/")

# def get_caption(img_url, txt):
#     result = client.predict(
#             img_url,
#             txt,
#             api_name="/predict"
#     )
#     return result

import requests
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": f"Bearer {token}"}

def get_caption(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()[0]["generated_text"].replace("arafed","")
