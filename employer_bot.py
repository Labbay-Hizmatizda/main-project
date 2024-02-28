import sqlite3
from datetime import datetime

import telebot
from markup import *

bot = telebot.TeleBot('6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8')
user_lang = {}
conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = conn.cursor()

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.InlineKeyboardMarkup()
    lang_rus = types.InlineKeyboardButton('🇷🇺 Русский', callback_data='lang_rus')
    lang_uz = types.InlineKeyboardButton('🇺🇿 O\'zbek tili', callback_data='lang_uz')

    markup.add(lang_rus, lang_uz)
    bot.send_message(message.chat.id, "Выберите язык 🌐\nTilni tanlang 🌐", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call): 
    if call.data == 'lang_rus':
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Привет, {0}!'.format(call.from_user.first_name), reply_markup=markup)
    elif call.data == 'about_us_rus':
        markup = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton('Назад', callback_data='back')
        markup.add(back)

        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id, text="У нас есть охуенный сайт хотите посетить ?\n pornhub.com", reply_markup=markup)

        '''
            -Мои данные
                -Изменить номер
                -Изменить пароль от аккаунта 
                -Назад
        '''
    elif call.data == 'my_account_rus':
        markup = my_account_rus()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id, text="Какую одну из функций :", reply_markup=markup)
    elif call.data == 'change_number':
        ...
    elif call.data == 'back':
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id, text="Какую одну из функций:", reply_markup=markup)



        '''
            -Заказы
                -активные заказы
                -новые заказы
                -назад
        '''
    elif call.data == 'orders_rus':
        markup = orders_rus()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id, text="Какую одну из функций :", reply_markup=markup)
    elif call.data == 'active_orders':
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id, text="Какую одну из функций :")
    elif call.data == 'new_order':
        pass
    elif call.data == 'back':
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id, text="Вы в главном меню \nКакое действие вы хотите сделать :z", reply_markup=markup)


user_info = {}
@bot.message_handler(commands=['log_into'])
def handle_services_worker(message):
    user_id = message.from_user.id
    user_info[user_id] = {}

    cursor.execute("SELECT * FROM admin_page_app_employer WHERE user_id=?", (user_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        bot.send_message(user_id, "Добро пожаловать обратно! tipa regestratsiya otboldi")
    elif message.contact.phone_number if message.contact else False:
        bot.send_message(user_id, "Для начала, давайте заполним некоторые дополнительные данные.")
        bot.send_message(user_id, "Введите ваше номер телефона:")
        bot.register_next_step_handler(message, check_handle_phone_number)
    else:
        bot.send_message(user_id, "Добро пожаловать обратно!, tipa regestratsiya otboldi")

def check_handle_phone_number(message):
    user_id = message.from_user.id
    phone_number = message.text
    # ToDo: checking if phone number written valid
    user_info[user_id]['phone_number'] = phone_number
    if phone_number:
        cursor.execute("SELECT * FROM admin_page_app_employer WHERE phone_number=?", (phone_number,))
        existing_user = cursor.fetchone()

        if existing_user:
            bot.send_message(phone_number, "Добро пожаловать обратно!")
        else:
            bot.send_message(phone_number, "Yengi useraka, keyingi stepga otamiz")
            bot.send_message(phone_number, "Введите ваше имя:")
            bot.register_next_step_handler(message, handle_name)

def handle_phone(message):
    user_id = message.from_user.id
    phone_number = message.text
    user_info[phone_number] = {}
    bot.send_message(phone_number, "Thank you. Now we can proceed.")

    print(user_info[user_id]['phone_number'])
    bot.send_message(user_id, "Введите ваше имя как указано в паспорте:")
    bot.register_next_step_handler(message, handle_name)

def handle_name(message):
    user_id = message.from_user.id
    user_info[user_id]['name'] = message.text

    bot.send_message(user_id, "Введите вашу фамилию как указано в паспорте:")
    bot.register_next_step_handler(message, handle_surname)

def handle_surname(message):
    user_id = message.from_user.id
    user_info[user_id]['surname'] = message.text

    bot.register_next_step_handler(message, insert_all_user_data)

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


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я не понимаю эту команду. Попробуйте /help для списка команд.")


if __name__ == "__main__":
    print('\n.', '.', '.\n')
    bot.polling(none_stop=True)


















'''Вывод деталей ------------------------------------------------------------------------------------------------------------'''
# @bot.message_handler(func=lambda message: message.text == "Мои данные")
# def handle_my_actions(message):
#     # Получаем информацию о пользователе
#     username = message.from_user.username
#     user_id = message.from_user.id
#     phone_number = message.contact.phone_number
#     # bot.send_message(message.chat.id, f'Спасибо, @{username}! Ваш номер телефона: {phone_number}')

#     # Запрашиваем номер телефона
#     bot.send_message(message.chat.id, f'Привет, @{username}! Пожалуйста, отправьте свой номер телефона.')
    
#     # Обработчик для получения номера телефона
# @bot.message_handler(content_types=['contact'])
# def handle_contact(message):
#     phone_number = message.contact.phone_number
#     bot.send_message(message.chat.id, f'Спасибо, @! Ваш номер телефона: {phone_number}')