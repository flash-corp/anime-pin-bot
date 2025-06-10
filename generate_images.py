import os
import openai
import requests
from dotenv import load_dotenv
from prompt_generator import get_random_prompts

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt, save_path):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    image_data = requests.get(image_url).content
    with open(save_path, 'wb') as f:
        f.write(image_data)

def run_generate():
    prompts = get_random_prompts(n=10)
    os.makedirs("images", exist_ok=True)

    with open("used_prompts.txt", "w") as log_file:
        for i, prompt in enumerate(prompts):
            filename = f"images/anime_{i+1}.png"
            generate_image(prompt, filename)
            log_file.write(f"{prompt}\n")
            print(f"Saved: {filename} ({prompt})")

if __name__ == "__main__":
    run_generate()
