import os

from dotenv import load_dotenv

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

from api import get_trains_info

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Get trains info", callback_data="get_trains"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Parses the CallbackQuery and updates the message text."""

    query = update.callback_query

    await query.answer()
    await query.edit_message_text(text=f"Selected option: {query.data}")

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
    get_trains = CallbackQueryHandler(button)
    application.add_handler(start_handler)
    application.add_handler(get_trains)


    application.run_polling()