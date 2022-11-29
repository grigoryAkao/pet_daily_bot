import requests

from daily_bot.celery import app
from daily_bot.settings import YANDEX_WEATHER_TOKEN

headers = {
    'X-Yandex-API-Key': YANDEX_WEATHER_TOKEN
}

URL = 'https://api.weather.yandex.ru/v2/forecast?lat=55.75396&lon=37.620393&extra=false'

@app.task
def get_weather():
    resp = requests.get(url=URL, headers=headers)
    if resp.status_code == 200:
        print(resp.json())
        return resp.json()