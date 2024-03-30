import telebot
from telebot import types
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

bot = telebot.TeleBot("6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8")

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Отправить паспортные данные', request_poll=KeyboardButtonPollType(type="passport"))
    markup.add(button)
    bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы отправить паспортные данные.", reply_markup=markup)

@bot.message_handler(content_types=['location'])
def handle_location(message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    bot.send_message(message.chat.id, f"Получена геолокация: Широта {latitude}, Долгота {longitude}")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    downloaded_file = bot.download_file(file_path)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))

    image_path = os.path.join(current_dir, 'photo.jpg')
    with open(image_path, 'wb') as photo:
        photo.write(downloaded_file)
    
    # Отправляем картинку обратно в чат
    with open(image_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

import requests

# L93TD8xFcWoJNkQ1wP7650oJc55SoqqM9bfUQaRWcY4
@bot.message_handler(content_types=['video'])
def handle_video(message):
    # Получаем информацию о видео
    file_id = message.video.file_id
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    # Скачиваем видео
    downloaded_file = bot.download_file(file_path)
    
    # Получаем путь к текущей директории
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Сохраняем видео в директорию с кодом бота
    video_path = os.path.join(current_dir, 'video.mp4')
    with open(video_path, 'wb') as video:
        video.write(downloaded_file)


bot.polling()
