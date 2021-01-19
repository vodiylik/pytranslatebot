import os
from googletrans import Translator
import telebot

translator = Translator()
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(token=TOKEN)

# handle /start command
@bot.message_handler(commands=["start"])
def send_welcome(message):
    hello_msg = "Salom,\nhozirda bot test tartibida ishlamoqda. \nTarjimon  botiga xush kelibsiz!"
    hello_msg += "\nIngliz yoki o'zbek tilidagi matnni yozib yuboring."
    bot.reply_to(message, hello_msg)


@bot.message_handler(content_types=["text"])
def func(message):
    detected_language = translator.detect(message)

    if detected_language in ["uz", "en", "ru"]:
        word = translator.translate(message, dest=detected_language).text
        bot.reply_to(message, word)
    else:
        a = "bugun siz uz dan en ga yoki \n en dan uz ga o'talolasiz "
        bot.reply_to(message, a)


bot.polling()
