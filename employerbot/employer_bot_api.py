import telebot
import requests
import sqlite3
from telebot import types
from threading import current_thread

# Creating the bot object
bot = telebot.TeleBot('6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8')

# URL of your API to fetch categories
BASE_URL = "http://127.0.0.1:8000/api/"

def get_employers():
    response = requests.get(f'{BASE_URL}employers')
    if response.status_code == 200:
        categories = response.json()  
        return categories
    else:
        print("Error while fetching categories:", response.status_code)
        return []

get_employers()