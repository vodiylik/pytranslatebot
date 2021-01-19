import os
import logging
from googletrans import Translator
import telebot

translator = Translator()
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(token=TOKEN)
log = logging.getLogger("pytanslatebot")

hello_message = "Salom,\nHozirda bot test tartibida ishlamoqda. \nTarjimon  botiga xush kelibsiz! \n"
msg = "Iltimos ingliz yoki o'zbek tilidagi matnni yozib yuboring."

# handle /start command
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, hello_message + msg)


@bot.message_handler(content_types=["text"])
def func(message):
    text = str(message.text)
    try:
        log.info("Detecting language of text: ", text)
        detected_language = translator.detect(text).lang
        log.info("Detected language: ", detected_language)
        if detected_language in ["en"]:
            log.info("Translating '", text, "' to english...")
            msg = translator.translate(text, dest="uz").text
        elif detected_language in ["uz"]:
            log.info("Translating '", text, "' to uzbek...")
            msg = translator.translate(text, dest="en").text
        else:
            msg = "Tilni aniqlab bo'lmadi, qaytadan urining!"
        bot.reply_to(message, msg)
        log.info("Message translated. Translated message: ", msg)
    except Exception as e:
        msg = "Xatolik yuz berdi birozdan so'ng urinib ko'ring!"
        log.error("Xatolik yuz berdi: ", e)
        bot.reply_to(message, msg)


bot.polling()
