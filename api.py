import os
from datetime import date, datetime
from http import HTTPStatus

import requests
from dotenv import load_dotenv

from models import Train

load_dotenv()

YANDEX_SCHEDULE_KEY = os.getenv('YANDEX_SCHEDULE_KEY')
API_URL = 'https://api.rasp.yandex.net/v3.0/search/?'

params = {
    'apikey': YANDEX_SCHEDULE_KEY,
    'from':'s9600741',
    'to':'s9600901',
    'date': date.today(),
    'result_timezone':'Europe/Moscow',
}

def get_trains_info():
    respose = requests.get(API_URL, params=params)

    if respose.status_code == HTTPStatus.OK:
        results = respose.json()['segments']
        trains = []
        for result in results:
            train = Train(
                train_type=result['thread']['transport_subtype']['title'],
                from_station=result['from']['title'],
                to_station=result['to']['title'],
                departure=result['departure'],
                arrival=result['arrival']
            )
            trains.append(train)
        return [train for train in trains if train.departure.timestamp() > datetime.now().timestamp()]




