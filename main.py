import telebot
from random import randint
from telebot import types
from PIL import Image, ExifTags
import os

# speak = ["ИДИ НАХУЙ", "ИДИ НАХУЙ ГНИДА", "ТЫ МРАЗЬ", "У ТЕБЯ В ЯКОРЕ ЖОПА", "У ТЕБЯ В ЖОПЕ ЯКОРЬ", "ДАНЯ ЛОХ", "ВЫСУНЬ ЦВЕТОК ИЗ ЗАДНИЦЫ", "МИША КРЫСА","У ТЕБЯ МАТЬ УМЕРЛА"]

TOKEN = "1707242756:AAHeN1bEdS-WemLtmvxlQ9ucjQdibxDvRtc"
meta = {}

bot = telebot.TeleBot(TOKEN)


def get_meta(path):
    img = Image.open(path)
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    return exif
# @bot.message_handler(content_types=["text"])
# def get_message(message):
#     bot.reply_to(message,speak[randint(0,len(speak))])

@bot.message_handler(content_types=['document',"text"])
def handle_docs_photo(message):
    global meta
    if meta.get(message.text) == None:
        try:
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path) 

            src=file_info.file_path
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)


            meta = get_meta("documents/" + os.listdir("documents")[0])
            filelist = os.listdir("documents")
            for f in filelist:
                os.remove(os.path.join('documents', f))  
            user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
            
            for key in meta:
                user_markup.row(key)

            # user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            # user_markup.row('Тренировки', 'Техника выполнения упражнений')
            # user_markup.row('Советы', '/end')
            bot.reply_to(message,"Изображение обробатывается", reply_markup = user_markup) 

            
                    

        except Exception as e:
            bot.reply_to(message,e)
    else:
        bot.send_message(message.chat.id, meta[message.id]) 


@bot.message_handler(content_types=['text'])
def info(message):
    bot.send_message(message.chat.id, meta[message.id]) 


bot.polling(none_stop=True, interval=0)