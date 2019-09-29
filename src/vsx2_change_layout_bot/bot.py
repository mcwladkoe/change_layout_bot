# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sys
import argparse

from vsx2_change_layout.helpers import change_layout

import logging
logger = logging.getLogger('tg_bot')
hdlr = logging.FileHandler('tg_bot_rotate_text.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)


def startCommand(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Привет. Отправь мне текст и я сменю раскладку.'
    )


def textMessage(bot, update):
    text = update.message.text
    bot.send_message(
        chat_id=update.message.chat_id,
        text=change_layout(text, None, 'ru_qwerty')
    )


def main(argv=sys.argv):
    description = """
        Start bot.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        'token',
        metavar='token',
        help='Telegram bot token'
    )

    args = parser.parse_args(argv[1:])

    updater = Updater(token=args.token)
    dispatcher = updater.dispatcher

    start_command_handler = CommandHandler('start', startCommand)
    # doc_command_handler = CommandHandler('doc', docCommand)
    text_message_handler = MessageHandler(Filters.text, textMessage)

    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(text_message_handler)
    # dispatcher.add_handler(doc_command_handler)

    updater.start_polling(clean=True)

    updater.idle()
