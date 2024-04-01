import telebot
import requests
import sqlite3
from telebot import types
from threading import current_thread

# Creating the bot object
bot = telebot.TeleBot('6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8')

# URL of your API to fetch categories
API_URL = "http://127.0.0.1:8000/api/category/"

# Function to fetch categories from API
def get_categories_from_api():
    response = requests.get(API_URL)
    if response.status_code == 200:
        categories = response.json()  
        return categories
    else:
        print("Error while fetching categories:", response.status_code)
        return []

# Function to create dynamic markup
def create_dynamic_markup(categories):
    markup = types.InlineKeyboardMarkup(row_width=1)  

    for category in categories:
        button = types.InlineKeyboardButton(text=category['name'], callback_data=category['id'])
        markup.add(button)

    return markup

# Handler for /start command
@bot.message_handler(commands=['start'])
def start(message):
    categories = get_categories_from_api()

    if categories:
        markup = create_dynamic_markup(categories)
        bot.send_message(message.chat.id, "Choose a category:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Failed to fetch categories from API.")

# Handler for button clicks
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    bot.send_message(call.message.chat.id, f"You've selected the category with ID: {call.data}")

    # Saving the selected category ID
    selected_category_id = call.data

    # Asking user for product description
    bot.send_message(call.message.chat.id, "Enter the product description:")
    bot.register_next_step_handler(call.message, lambda message: ask_price(message, selected_category_id))

# Asking user for product price
def ask_price(message, category_id):
    description = message.text
    bot.send_message(message.chat.id, "Enter the product price:")
    bot.register_next_step_handler(message, lambda message: add_product_to_database(message, description, category_id))

# Adding product to the database
def add_product_to_database(message, description, category_id):
    price = message.text
    thread_id = current_thread().ident  # Get current thread ID for debugging

    # Creating a separate connection and cursor for each thread
    conn = sqlite3.connect('products.sqlite3')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO products (description, price, category) VALUES (?, ?, ?)",
                       (description, price, category_id))
        conn.commit()
        bot.send_message(message.chat.id, "Product successfully added to the database!")
    except sqlite3.Error as e:
        bot.send_message(message.chat.id, f"Error while adding product to the database: {e}")
    finally:
        cursor.close()
        conn.close()

# Running the bot
bot.polling()