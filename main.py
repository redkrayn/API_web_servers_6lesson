import os
import random
import requests
import telegram

from pathlib import Path
from dotenv import load_dotenv


def download_random_comics(path):
    last_comics = "https://xkcd.com/info.0.json"
    random_comics = random.randint(1, requests.get(last_comics).json().get('num'))
    url = f"https://xkcd.com/{random_comics}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comics_image = response.json()
    filename = f'comics_{random_comics}.jpg'
    image_response = requests.get(comics_image.get('img'))
    image_response.raise_for_status()
    image_path_filename = path / filename

    with open(image_path_filename, 'wb') as file:
        file.write(image_response.content)

    return comics_image.get('alt'), filename


def main():
    load_dotenv()
    path = Path('images')
    path.mkdir(exist_ok=True)
    try:
        comment, filename = download_random_comics(path)
        chat_id = os.environ["TELEGRAM_CHAT_ID"]
        bot = telegram.Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
        file_path = os.path.join(path, filename)
        with open(file_path, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file, caption=comment)

        if os.path.exists(file_path):
            os.remove(file_path)
    finally:
        for file in path.iterdir():
            os.remove(file)


if __name__ == "__main__":
    main()
