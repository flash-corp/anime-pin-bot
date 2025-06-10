import os
import requests
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv("PINTEREST_ACCESS_TOKEN")
BOARD_ID = os.getenv("BOARD_ID")

def upload_pin(image_path, title, description):
    url = "https://api.pinterest.com/v5/pins"
    with open(image_path, "rb") as image_file:
        files = {'image': image_file}
        data = {
            "title": title,
            "alt_text": description,
            "board_id": BOARD_ID
        }
        headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
        response = requests.post(url, headers=headers, data=data, files=files)

    if response.status_code == 201:
        print(f"Posted: {title}")
    else:
        print(f"Error posting: {response.status_code} - {response.text}")

def run_post():
    with open("used_prompts.txt", "r") as f:
        prompts = [line.strip() for line in f if line.strip()]
    images = sorted(os.listdir("images"))

    for i, image_name in enumerate(images[:10]):
        path = f"images/{image_name}"
        title = prompts[i] if i < len(prompts) else "AI Anime Art"
        description = f"AI-generated anime art: {title}"
        upload_pin(path, title, description)

if __name__ == "__main__":
    run_post()
