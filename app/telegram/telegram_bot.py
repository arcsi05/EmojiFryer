import logging
import os
# from random import randrange

# import advertools
# from advertools import emoji, emoji_search
from dotenv import load_dotenv
from telegram import ForceReply, Update
import telegram
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, Updater)
import requests
# import emojify
# from multilang_emoji import Emoji

# print('hallo')

# dogs = emoji_search('dog').emoji
# print(dogs.size)
# print(emoji_search('dog').emoji)
# print(emoji_search('dog').emoji)

# print(emojify.emojizeWord('kaka'))

# print(advertools.emoji_df.emoji.size)

# print(emojify.emojizeSentence("I run with the dog on the beach"))
# print(emojify.internationalEmojizer("Elmentem a kutyával a strandra futni"))

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__).setLevel(logging.DEBUG)

# hu_emojis = Emoji('hu')

# Define a few command handlers. These usually take the two arguments update and
# context.


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!\n\nTo learn about how to use this bot type /help',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('I will take the message you send me and try to put relevant emojis after *every single word*\.\n\nI speak all of the langages, however only a handful is currently used to limit my understanding of humans\.\n\nTo use a language other than the default English, you need to send me the code of the language in the first row of the message\.\n\n*Available lanugages and their codes:*\n `en`: English\n `hu`: Hungarian\n `fr`: French\n `de`: German\n\n\n_Example \(using German as language\):_\n\nde\nder Mann der Feuerwehr', parse_mode=telegram.ParseMode.MARKDOWN_V2)


def about_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        'This bot was created as a fun project to entertain myself.\nGitHub: https://github.com/arcsi05/overemojifier')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(requests.get(
        'http://localhost:4356/emojify?sentence='+update.message.text).text.strip('"'))

    # update.message.reply_text(
    #     emojify.emojizeSentence(update.message.text, hu_emojis))


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.getenv('TELEGRAM_TOKEN'))

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("about", about_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    load_dotenv()
    main()
