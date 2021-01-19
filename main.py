import os
from googletrans import Translator
import telebot

translator = Translator()
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(token=TOKEN)

hello_message = (
    "Salom,\nhozirda bot test tartibida ishlamoqda. \nTarjimon  botiga xush kelibsiz! "
)
msg = "Iltimos ingliz yoki o'zbek tilidagi matnni yozib yuboring."

# handle /start command
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, hello_message + msg)


@bot.message_handler(content_types=["text"])
def func(message):
    detected_language = translator.detect(message)

    if detected_language in ["en"]:
        translated_msg = translator.translate(message, dest="uz").text
        bot.reply_to(message, translated_msg)
    elif detected_language in ["uz"]:
        translated_msg = translator.translate(message, dest="en").text
        bot.reply_to(message, translated_msg)
    else:
        bot.reply_to(message, msg)


bot.polling()
