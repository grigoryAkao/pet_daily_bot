import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'daily_bot.settings')
django.setup()

from telegram.ext import Updater

from daily_bot.settings import TELEGRAM_TOKEN
from tg.add_handlers import add_handlers


def run_polling(token: str):
    updater = Updater(token)
    dispatcher = updater.dispatcher
    add_handlers(dispatcher)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    run_polling(TELEGRAM_TOKEN)
