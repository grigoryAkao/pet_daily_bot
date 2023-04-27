import os

from dotenv import load_dotenv

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from api import get_trains_info

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Бот работает и готов помочь добраться домой.'
    )

async def get_trains(update: Update, context: ContextTypes.DEFAULT_TYPE):
    trains = get_trains_info()
    for train in trains:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=str(train)
        )


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)
    train_handler = CommandHandler('get_trains', get_trains)
    application.add_handler(start_handler)
    application.add_handler(train_handler)

    application.run_polling()