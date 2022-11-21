from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, Dispatcher

from daily_bot.settings import TELEGRAM_TOKEN
from daily_bot.celery import app
from weather.tasks import simple_request

from .add_handlers import start

def enable_bot(token: str) -> Updater:
    bot = Updater(token)
    bot.start_polling()
    return bot

if bot := enable_bot.delay(TELEGRAM_TOKEN):
    dispatcher = bot.dispatcher
    print('Bot started')

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)