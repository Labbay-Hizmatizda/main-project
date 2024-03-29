import sqlite3
from datetime import datetime
import os
import telebot
import requests
from telebot.types import ReplyKeyboardRemove
from markup import *

token = '6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8'
bot = telebot.TeleBot(token)
user_lang = {}
conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = conn.cursor()
chat_text = {}

@bot.message_handler(commands=['start'])
def start(message):
    lang = lang_identifier(message)
    user_language_req(message, lang)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'lang_rus':
        user_lang[call.from_user.id] = 'rus'
        cursor.execute('''INSERT INTO admin_page_app_language (user_id, language)
                          VALUES (?, ?)''', (call.from_user.id, 'rus'))
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Главный меню:\n     /log_into для верификации\n     /add_orders посмотреть заказы', reply_markup=markup)

    elif call.data == 'my_account_rus':
        markup = my_account_rus()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Какое действие вы хотите сделать :......", reply_markup=markup)
    elif call.data == 'change_phone_num_rus':
        ...
    elif call.data == 'back_to_main_menu_rus':
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Главный меню:\n     /log_into для верификации\n     /add_orders посмотреть заказы'.format(
                                  call.from_user.first_name), reply_markup=markup)

    elif call.data == 'orders_rus' or call.data == 'back_orders':
        markup = orders_rus()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Заказы\nКакое действие вы хотите сделать :", reply_markup=markup)
    elif call.data == 'active_orders':
        markup = active_orders_rus()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Aктивные заказы\nКакое действие вы хотите сделать :", reply_markup=markup)

    # --uzbek lang ---------------------------------------------------------------------------------------------

    if call.data == 'lang_uz':
        user_lang[call.from_user.id] = 'uz'
        cursor.execute('''INSERT INTO admin_page_app_language (user_id, language)
                          VALUES (?, ?)''', (call.from_user.id, 'uz'))
        markup = uzbek()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Glavni menu: \n     /log_into | tekshirish uchun.buyurtma qoshing\n     /add_orders | buyurtmalarni korish", reply_markup=markup)

    elif call.data == 'my_account_uz':
        markup = my_account_uz()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Nima qmohchisiz:", reply_markup=markup)
    elif call.data == 'change_phone_num_uz':
        ...
    elif call.data == 'back_uz':
        markup = uzbek()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Glavni menyu \nNma qmohchisiz: ", reply_markup=markup)

    elif call.data == 'orders_uz':
        markup = orders_uz()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Zakazla\nNma qmohchisiz: ", reply_markup=markup)
    elif call.data == 'active_orders_uz':
        markup = active_orders_uz()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Aktivni Zakazla\nNma qmohchisiz: ", reply_markup=markup)
    elif call.data == 'back_orders_uz':
        markup = orders_uz()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Nma qmohchisiz: ", reply_markup=markup)
    elif call.data == 'back_uz':
        markup = uzbek()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Glavni menyu \nNma qmohchisiz: ", reply_markup=markup)


user_info = {}

@bot.message_handler(commands=['kyc'])
def handle_services_worker(message):
    user_id = message.from_user.id
    user_info[user_id] = {}

    cursor.execute("SELECT * FROM admin_page_app_employer WHERE user_id=?", (user_id,))
    existing_user = cursor.fetchone()
    if existing_user:
        bot.send_message(user_id, "Добро пожаловать обратно! tipa oldin reg qilib login qibogan")
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        phone_button = types.KeyboardButton(text="Share my phone number", request_contact=True)
        markup.add(phone_button)
        bot.send_message(user_id, "Добро пожаловать, nomerini berishi kere", reply_markup=markup)
        bot.register_next_step_handler(message, check_handle_phone_number)


def check_handle_phone_number(message):
    user_id = message.from_user.id
    phone_number = message.contact.phone_number if message.contact else None
    user_info[user_id]['phone_number'] = phone_number

    if phone_number:
        bot.send_message(user_id, "Введите ваше имя:", reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, handle_name)
    else:
        bot.send_message(user_id, "Нажмите кнопку")
        bot.register_next_step_handler(message, check_handle_phone_number)

def handle_name(message):
    user_id = message.from_user.id
    user_info[user_id]['name'] = message.text

    bot.send_message(user_id, "Введите вашу фамилию как указано в паспорте:")
    bot.register_next_step_handler(message, handle_surname)


def handle_surname(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    passport = types.KeyboardButton('Passport')
    id_button = types.KeyboardButton('ID')
    markup.add(passport, id_button)

    user_id = message.from_user.id
    user_info[user_id]['surname'] = message.text
    bot.send_message(user_id, "Выберите тип идентификатора", reply_markup=markup)
    bot.register_next_step_handler(message, handle_choosing_identifier_type)


def handle_choosing_identifier_type(message):
    user_id = message.from_user.id
    identifier_type = message.text
    user_info[user_id]['identifier_type'] = identifier_type

    if identifier_type == "Passport":
        bot.send_message(user_id, "Пришлите изображение паспорта")
        bot.register_next_step_handler(message, handle_passport_image)
    elif identifier_type == "ID":
        bot.send_message(user_id, "Пришлите изображения удостоверения личности")
        bot.register_next_step_handler(message, handle_id_image_first)
    else:
        bot.send_message(user_id, "Тип идентификатора не распознан. Пожалуйста, выберите тип идентификатора снова.")
        handle_choosing_identifier_type(message)


def handle_id_image_first(message):
    user_id = message.from_user.id
    directory = os.path.join("media", "identifiers", str(user_id))

    os.makedirs(directory, exist_ok=True)

    file_id = message.photo[2].file_id
    photo_path = os.path.join(directory, "id_image_first.jpg")
    r = requests.get(f"https://api.telegram.org/bot{token}/getFile?file_id={file_id}")
    if r.status_code == 200:
        file_info = r.json()
        file_path = file_info['result']['file_path']
        photo_url = f"https://api.telegram.org/file/bot{token}/{file_path}"
        response = requests.get(photo_url)
        print(response.status_code)
        if response.status_code == 200:
            with open(photo_path, 'wb') as f:
                f.write(response.content)
                bot.send_message(user_id,
                                 "Image saved seccessfully. Please send the second image of your ID.")
        else:
            bot.send_message(user_id,
                             "Failed to download image.")
            bot.register_next_step_handler(message, handle_id_image_first)
    else:
        bot.send_message(user_id,
                         "Failed to get file information.")
        bot.register_next_step_handler(message, handle_id_image_first)
    bot.register_next_step_handler(message, handle_id_image_second)


def handle_id_image_second(message):
    user_id = message.from_user.id
    directory = os.path.join("media", "identifiers", str(user_id))

    os.makedirs(directory, exist_ok=True)

    # Save image
    file_id = message.photo[2].file_id
    photo_path = os.path.join(directory, "id_image_second.jpg")
    r = requests.get(f"https://api.telegram.org/bot{token}/getFile?file_id={file_id}")
    if r.status_code == 200:
        file_info = r.json()
        file_path = file_info['result']['file_path']
        photo_url = f"https://api.telegram.org/file/bot{token}/{file_path}"
        response = requests.get(photo_url)
        if response.status_code == 200:
            with open(photo_path, 'wb') as f:
                f.write(response.content)
                bot.send_message(user_id,
                                 "Image saved seccessfully. Wait a time to process your data.")
        else:
            ...
    # Failed to download image
    # Handle the error accordingly
    else:
        ...
    # Failed to get file information
    # Handle the error accordingly

    # Call function to insert user data for second ID image
    bot.register_next_step_handler(message, handle_cv_image)


def handle_passport_image(message):
    user_id = message.from_user.id
    directory = os.path.join("media", "identifiers", str(user_id))

    os.makedirs(directory, exist_ok=True)

    # Save image
    file_id = message.photo[2].file_id
    photo_path = os.path.join(directory, "passport_image.jpg")
    r = requests.get(f"https://api.telegram.org/bot{token}/getFile?file_id={file_id}")
    if r.status_code == 200:
        file_info = r.json()
        file_path = file_info['result']['file_path']
        photo_url = f"https://api.telegram.org/file/bot{token}/{file_path}"
        response = requests.get(photo_url)
        if response.status_code == 200:
            with open(photo_path, 'wb') as f:
                f.write(response.content)
                bot.send_message(user_id,
                                 "Image saved seccessfully. Wait a time to process your data.")
        else:
            ...
    # Failed to download image
    # Handle the error accordingly
    else:
        ...
    # Failed to get file information
    # Handle the error accordingly

    # Call function to insert user data for second ID image
    bot.register_next_step_handler(message, handle_cv_image)


def handle_cv_image(message):
    user_id = message.from_user.id
    directory = os.path.join("media", "cv", str(user_id))

    os.makedirs(directory, exist_ok=True)

    file_id = message.photo[2].file_id
    photo_path = os.path.join(directory, "cv_image.jpg")
    r = requests.get(f"https://api.telegram.org/bot{token}/getFile?file_id={file_id}")
    if r.status_code == 200:
        file_info = r.json()
        file_path = file_info['result']['file_path']
        photo_url = f"https://api.telegram.org/file/bot{token}/{file_path}"
        response = requests.get(photo_url)
        print(response.status_code)
        if response.status_code == 200:
            with open(photo_path, 'wb') as f:
                f.write(response.content)
                bot.send_message(user_id,
                                 "Image saved seccessfully. Please send the second image of your ID.")
        else:
            bot.send_message(user_id,
                             "Failed to download image.")
    bot.send_message(user_id, 'Напишите немного о себе....')
    bot.register_next_step_handler(message, handle_cv_bio)

def handle_cv_bio(message):
    user_id = message.from_user.id
    user_info[user_id]['bio'] = message.text
    insert_all_user_data(message)
    

def insert_all_user_data(message):
    user_id = message.from_user.id

    date_created = datetime.now()
    cursor.execute(
        "INSERT INTO admin_page_app_employer (user_id, name, surname, phone_number, date_created) VALUES ("
        "?, ?, ?, ?, ?)",
        (user_id, user_info[user_id]['name'], user_info[user_id]['surname'],
         user_info[user_id]['phone_number'], date_created))
    conn.commit()

    cursor.execute(
        "INSERT INTO admin_page_app_cv (image, bio, rating, owner_id) VALUES (?, ?, ?, ?)",
        ('media/cv/cv_image.jpg', user_info[user_id]['bio'], 0, user_id))
    conn.commit()

    bot.send_message(user_id,
                     "Отлично! Теперь вы можете использовать команду /jobs для просмотра доступных действий.")


orders = {}


@bot.message_handler(commands=['add_order'])
def handle_add_order(message):
    orders[message.from_user.id] = {}
    bot.send_message(message.from_user.id, "Please enter the category.")
    bot.register_next_step_handler(message, handle_category)


def handle_category(message):
    user_id = message.from_user.id
    category = message.text
    orders[user_id]['category'] = category
    bot.send_message(user_id, "Please enter the description of your order.")
    bot.register_next_step_handler(message, handle_description)


def handle_description(message):
    user_id = message.from_user.id
    description = message.text
    orders[user_id]['description'] = description
    bot.send_message(user_id, "Please upload an image of your order.")
    bot.register_next_step_handler(message, handle_image)


def handle_image(message):
    user_id = message.from_user.id
    image_url = message.photo[-1].file_id
    orders[user_id]['image'] = image_url
    bot.send_message(user_id, "Please enter the location.")
    bot.register_next_step_handler(message, handle_location)


def handle_location(message):
    user_id = message.from_user.id
    location = message.text
    orders[user_id]['location'] = location
    bot.send_message(user_id, "Please enter the location link.")
    bot.register_next_step_handler(message, handle_location_link)


def handle_location_link(message):
    user_id = message.from_user.id
    location_link = message.text
    orders[user_id]['location_link'] = location_link
    bot.send_message(user_id, "Please enter the price.")
    bot.register_next_step_handler(message, handle_price)


def handle_price(message):
    user_id = message.from_user.id
    price = message.text
    orders[user_id]['price'] = price

    order_data = orders[user_id]
    cursor.execute(
        "INSERT INTO admin_page_app_order (category, description, image, location, location_link, price, owner_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (order_data['category'], order_data['description'], order_data['image'], order_data['location'],
         order_data['location_link'], order_data['price'], user_id)
    )
    conn.commit()
    bot.send_message(user_id, "Order added successfully!, /orders to see your order")


@bot.message_handler(commands=['orders'])
def list_orders(message):
    user_id = message.chat.id
    cursor.execute("SELECT * FROM admin_page_app_order WHERE owner_id=?", (user_id,))
    orders = cursor.fetchall()

    for order in orders:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text='Edit', callback_data=f'edit_{order[0]}'),
                   types.InlineKeyboardButton(text='Cancel', callback_data=f'cancel_{order[0]}'))
        bot.send_message(user_id, f'Order {order[0]}: {order[1]}', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    action, order_id = call.data.split('_')
    if action == 'edit':
        # Implement edit functionality
        pass
    elif action == 'cancel':
        # Implement cancel functionality
        pass


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я не понимаю эту команду. Попробуйте /help для списка команд.")


def lang_identifier(message):
    user_id = message.from_user.id
    cursor.execute("SELECT language FROM admin_page_app_language WHERE user_id=?", (user_id,))
    existing_user = cursor.fetchone()
    if existing_user:
        print(existing_user[0])
        user_lang[user_id] = existing_user[0]
        return user_lang
    return None



def user_language_req(message, lang):
    user_id = message.chat.id
    if lang:
        if lang[user_id] == 'rus':
            user_lang[user_id] = 'rus'
            cursor.execute('''INSERT INTO admin_page_app_language (user_id, language)
                              VALUES (?, ?)''', (user_id, 'rus'))
            markup = russian()
            bot.send_message(chat_id=user_id,
                                  text='Главный меню:\n     /log_into для верификации\n     /add_orders посмотреть заказы'.format(
                                  message.from_user.first_name), reply_markup=markup)
        elif lang[user_id] == 'uz':
            user_lang[message.from_user.id] = 'uz'
            cursor.execute('''INSERT INTO admin_page_app_language (user_id, language)
                              VALUES (?, ?)''', (message.from_user.id, 'uz'))
            markup = uzbek()
            bot.send_message(chat_id=message.chat.id,
                                  text="Glavni menu: \n     /log_into | tekshirish uchun.buyurtma qoshing\n     /add_orders | buyurtmalarni korish", reply_markup=markup)
    else:

        markup = types.InlineKeyboardMarkup()
        lang_rus = types.InlineKeyboardButton('🇷🇺 Русский', callback_data='lang_rus')
        lang_uz = types.InlineKeyboardButton('🇺🇿 O\'zbek tili', callback_data='lang_uz')

        markup.add(lang_rus, lang_uz)
        bot.send_message(message.chat.id, "Выберите язык 🌐\nTilni tanlang 🌐", reply_markup=markup)


if __name__ == "__main__":
    print('\n.', '.', '.\n')
    bot.polling(none_stop=True)
