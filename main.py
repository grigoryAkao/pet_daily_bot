import os
from datetime import datetime,date
from http import HTTPStatus

import requests
from dotenv import load_dotenv


# Загрузка переменных из файла .env
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
YANDEX_SCHEDULE_KEY = os.getenv('YANDEX_SCHEDULE_KEY')
API_URL = 'https://api.rasp.yandex.net/v3.0/search/?'

params = {
    'apikey': YANDEX_SCHEDULE_KEY,
    'from':'s9600741',
    'to':'s9601934',
    'date': date.today()
}

print(params['date'])

respose = requests.get(API_URL, params=params)

if respose.status_code == HTTPStatus.OK:
    print(respose.json())
