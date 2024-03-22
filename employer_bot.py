import sqlite3
from datetime import datetime
import os
import telebot
import requests

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
                              text='Главный меню:\n     /log_into для верификации\n     /add_orders посмотреть заказы'.format(
                                  call.from_user.first_name), reply_markup=markup)
        '''
            -Мои данные
                -Изменить номер
                -Изменить пароль от аккаунта
                -Назад
        '''
    elif call.data == 'my_account_rus':
        markup = my_account_rus()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Какое действие вы хотите сделать :......", reply_markup=markup)
    elif call.data == 'change_phone_num_rus':
        ...
    elif call.data == 'back':
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Главный меню:\n     /log_into для верификации\n     /add_orders посмотреть заказы'.format(
                                  call.from_user.first_name), reply_markup=markup)

        '''
            -Заказы
                -активные заказы
                -новые заказы
                -назад
        '''
    elif call.data == 'orders_rus':
        markup = orders_rus()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Заказы\nКакое действие вы хотите сделать :", reply_markup=markup)
    elif call.data == 'active_orders':
        markup = active_orders_rus()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Aктивные заказы\nКакое действие вы хотите сделать :", reply_markup=markup)
    elif call.data == 'back_orders':
        markup = orders_rus()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Какое действие вы хотите сделать :", reply_markup=markup)
    elif call.data == 'back':
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text="Вы в главном меню \nКакое действие вы хотите сделать :", reply_markup=markup)

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


@bot.message_handler(commands=['potverdeniye_lichnosti', 'log_into', 'shaxsni_tasdiqlash'])
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


from telebot.types import ReplyKeyboardRemove


def check_handle_phone_number(message):
    user_id = message.from_user.id
    phone_number = message.contact.phone_number if message.contact else None
    user_info[user_id]['phone_number'] = phone_number
    if phone_number:
        cursor.execute("SELECT * FROM admin_page_app_employer WHERE phone_number=?", (phone_number,))
        existing_user = cursor.fetchone()

        if existing_user:
            # ToDo: sending sms in order to verify user
            bot.send_message(user_id, "Добро пожаловать обратно!", reply_markup=ReplyKeyboardRemove())
        else:
            bot.send_message(user_id, "Yengi useraka, keyingi stepga otamiz", reply_markup=ReplyKeyboardRemove())
            bot.send_message(user_id, "Введите ваше имя:")
            bot.register_next_step_handler(message, handle_name)
    else:
        bot.send_message(user_id, "Invalid phone number. Please share your phone number again.")


def handle_name(message):
    user_id = message.from_user.id
    user_info[user_id]['name'] = message.text

    bot.send_message(user_id, "Введите вашу фамилию как указано в паспорте:")
    bot.register_next_step_handler(message, handle_surname)


def handle_surname(message):
    user_id = message.from_user.id
    user_info[user_id]['surname'] = message.text
    bot.send_message(user_id, "Выберите тип идентификатора")
    bot.register_next_step_handler(message, handle_choosing_identifier_type)


def handle_choosing_identifier_type(message):
    user_id = message.from_user.id
    identifier_type = message.text
    user_info[user_id]['identifier_type'] = identifier_type

    if identifier_type == "passport":
        bot.send_message(user_id, "Пришлите изображение паспорта")
        bot.register_next_step_handler(message, handle_passport_image)
    elif identifier_type == "id":
        bot.send_message(user_id, "Пришлите изображения удостоверения личности")
        bot.register_next_step_handler(message, handle_id_image_first)
    else:
        bot.send_message(user_id, "Тип идентификатора не распознан. Пожалуйста, выберите тип идентификатора снова.")
        handle_choosing_identifier_type(message)


def handle_id_image_first(message):
    user_id = message.from_user.id
    phone_number = user_info[user_id]['phone_number']

    directory = os.path.join("media", "identifiers", str(phone_number))

    os.makedirs(directory, exist_ok=True)

    # Save image
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

    # Failed to download image
    # Handle the error accordingly
    else:
        bot.send_message(user_id,
                         "Failed to get file information.")
        bot.register_next_step_handler(message, handle_id_image_first)
    # Failed to get file information
    # Handle the error accordingly
    bot.register_next_step_handler(message, handle_id_image_second)


def handle_id_image_second(message):
    user_id = message.from_user.id
    phone_number = user_info[user_id]['phone_number']

    directory = os.path.join("media", "identifiers", str(phone_number))

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
    insert_all_user_data(message)


def handle_passport_image(message):
    user_id = message.from_user.id
    phone_number = user_info[user_id]['phone_number']

    directory = os.path.join("media", "identifiers", str(phone_number))

    os.makedirs(directory, exist_ok=True)

    # Save images
    for i, photo in enumerate(message.photo, start=1):
        photo_file_id = photo.file_id
        photo_path = os.path.join(directory, f"photo_{i}.jpg")
        photo_file = bot.get_file(photo_file_id)
        photo_file.download_file(photo_path)

    # Call function to insert all user data
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
    # Assuming the image is uploaded and saved to some location
    image_url = message.photo[-1].file_id  # You may need to adjust this based on how you handle images
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

    # Save order to database
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
    # if user_lang[user_id] == 'uz' or user_lang[user_id] == 'rus':
    #     return user_lang[user_id]
    cursor.execute("SELECT language FROM admin_page_app_language WHERE user_id=?", (user_id,))
    existing_user = cursor.fetchone()
    if existing_user:
        print(existing_user[0])
        user_lang[user_id] = existing_user[0]
        return user_lang
    return None
    # markup = types.InlineKeyboardMarkup()
    # lang_rus = types.InlineKeyboardButton('🇷🇺 Русский', callback_data='lang_rus')
    # lang_uz = types.InlineKeyboardButton('🇺🇿 O\'zbek tili', callback_data='lang_uz')
    #
    # markup.add(lang_rus, lang_uz)
    # bot.send_message(message.chat.id, "Выберите язык 🌐\nTilni tanlang 🌐", reply_markup=markup)


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
