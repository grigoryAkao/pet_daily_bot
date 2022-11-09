import requests

from daily_bot.celery import app

@app.task
def simple_request():
    requests.get()