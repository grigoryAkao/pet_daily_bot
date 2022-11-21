from telegram.ext import CommandHandler, Dispatcher

from .handlers.command_handlers import command_start, command_weather

def add_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.add_handler(CommandHandler('start', command_start))
    dispatcher.add_handler(CommandHandler('start', command_weather))