from datetime import datetime
import os
import telebot
from telebot.types import ReplyKeyboardRemove
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from markup import *
from api_integration import *

# Creating the bot object
bot = telebot.TeleBot('6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8')

token = '6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8'
bot = telebot.TeleBot(token)
user_lang = {}

@bot.message_handler(commands=['start'])
def start(message):
    lang = lang_identifier(message)
    user_language_req(message, lang)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'lang_rus':
        user_lang[call.from_user.id] = 'rus'
        # cursor.execute('''INSERT INTO admin_page_app_language (user_id, language)
        #                   VALUES (?, ?)''', (call.from_user.id, 'rus'))
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
    elif call.data == 'active_orders' or call.data == 'history_orders':
        message = call.message
        if hasattr(message, 'chat'):
            user_id = message.chat.id
            # cursor.execute("SELECT * FROM admin_page_app_order WHERE owner_id=?", (user_id,))
            # orders = cursor.fetchall()

            for order in orders:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text='Edit', callback_data=f'edit_{order[0]}'),
                           types.InlineKeyboardButton(text='Cancel', callback_data=f'cancel_{order[0]}'))
                bot.send_message(user_id, f'ID : {order[0]}\nCategory : {order[1]}\nDescription : {order[2]}\nLocation : {order[4]}\nPrice : {order[5]}\nOwner_id : {order[6]}\n\n\nChoose an action:', reply_markup=markup)
    elif call.data == 'new_order':
        ...


    # --uzbek lang ---------------------------------------------------------------------------------------------

    if call.data == 'lang_uz':
        user_lang[call.from_user.id] = 'uz'
        # cursor.execute('''INSERT INTO admin_page_app_language (user_id, language)
        #                   VALUES (?, ?)''', (call.from_user.id, 'uz'))
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
