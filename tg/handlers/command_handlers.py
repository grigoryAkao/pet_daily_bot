from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

from core.models import User
from weather.tasks import weather_request

def command_start(update: Update, context: CallbackContext):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([['/weather']])
    if User.objects.filter(telegram_profile__id=chat.id):
        context.bot.send_message(
            chat_id=chat.id,
            text='Bot запущен!',
        )
    else:
        context.bot.send_message(
            chat_id=chat.id,
            text='Доступ запрещен, обратитесь к администратору',
        )

def command_weather(update: Update, context: CallbackContext):
    chat = update.effective_chat
    if User.objects.filter(telegram_profile__id=chat.id):
        weather = weather_request()
        print(weather['info'])
        context.bot.send_message(
            chat_id=chat.id,
            text=f'{weather["info"]}'
        )