import os
import random
import requests
import telegram

from pathlib import Path
from dotenv import load_dotenv


def download_comics():
    last_comics = "https://xkcd.com/info.0.json"
    random_comics = random.randint(1, requests.get(last_comics).json().get('num'))
    url = f"https://xkcd.com/{random_comics}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comics_image = response.json()
    path = Path('images')
    path.mkdir(exist_ok=True)
    filename = f'comics_{random_comics}.jpg'
    image_response = requests.get(comics_image.get('img'))
    image_response.raise_for_status()
    image_path_filename = path / filename

    with open(image_path_filename, 'wb') as file:
        file.write(image_response.content)

    return comics_image.get('alt'), filename


def main():
    load_dotenv()
    comment, filename = download_comics()
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    bot = telegram.Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
    with open(f'images/{filename}', 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file, caption=comment)
    if os.path.exists(f'images/{filename}'):
        os.remove(f'images/{filename}')


if __name__ == "__main__":
    main()
