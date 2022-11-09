from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

from daily_bot.settings import TELEGRAM_TOKEN
from weather.tasks import simple_request

updater = Updater(TELEGRAM_TOKEN)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    text = simple_request()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)