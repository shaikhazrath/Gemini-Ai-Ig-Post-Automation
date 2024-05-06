from instagrapi import Client
from dotenv import load_dotenv
import os
load_dotenv()
def upload_photo_to_instagram(file_path, caption):
    try:
        username = os.environ.get('IG_USERNAME')
        password = os.environ.get('IG_PASSWORD')
        cl = Client()
        cl.login(username,password )

        media = cl.photo_upload(
            path=file_path,
            caption=caption
        )

    except Exception as e:
        print(f"Error: {e}")
