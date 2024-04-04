from datetime import datetime
import os
import telebot
from telebot.types import ReplyKeyboardRemove
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from markup import *
from api_integration import *
from api_integration import *

# Creating the bot object
bot = telebot.TeleBot('6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8')

user_lang = {}
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
        user_lang[call.from_user.id] = 'rus'
        # cursor.execute('''INSERT INTO admin_page_app_language (user_id, language)
        #                   VALUES (?, ?)''', (call.from_user.id, 'rus'))
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Главный меню:\n     /log_into для верификации\n     /add_orders посмотреть заказы\n\n\n', reply_markup=markup)
    elif call.data == 'about_us_rus':
        markup = types.InlineKeyboardMarkup()
        url = types.InlineKeyboardButton(text='Наш сайт', url='https://youtube.com')
        back = types.InlineKeyboardButton('◀ Назад', callback_data='about_us_back_menu')
        markup.add(url, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Наш сайт ⇣", reply_markup=markup)
    elif call.data == 'my_account_rus':
        user_id = call.from_user.id

        markup = my_account_rus()
        response = get_employee(user_id)
        text = f'''
User ID : {response[0]['user_id']}
Имя : {response[0]['name']}
Фамилия : {response[0]['surname']}
Телефон номера : {response[0]['phone_number']}\n\n
        '''
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f"{text}Какое действие вы хотите сделать :......", reply_markup=markup)
    elif call.data == 'back_to_main_menu_rus' or call.data == 'about_us_back_menu':
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Главный меню:\n     /kyc для верификации\n     /add_orders посмотреть заказы'.format(
                                  call.from_user.first_name), reply_markup=markup)
    elif call.data == 'proposals_rus' or call.data == 'back_orders' or call.data == 'back_proposals':
        markup = proposals_rus()
        user_id = call.from_user.id
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Какое действие вы хотите сделать :', reply_markup=markup)
    elif call.data == 'pending_proposals':
        message = call.message
        markup = pending_proposals_rus()
        user_id = call.from_user.id

        response = get_proposals(user_id)
        text = ""
        for proposals in response:
            text += f"ID : {proposals['id']}\nOwner_id : {proposals['owner_id']}\nOrder_id : {proposals['order_id']}\nPrice : {proposals['price']}\n\n"

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{text}', reply_markup=markup)    
    elif call.data == 'proposals_history':
        ...
    elif call.data == 'new_proposal':
        message = call.message
        if hasattr(message, 'chat'):
            user_id = message.chat.id

            
        

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










orders = {}
message_ids = {}

@bot.message_handler(commands=['add_order'])
def handle_add_order(message):
    def handle_category(message):
        def handle_description(message):
            user_id = message.from_user.id
            description = message.text
            orders[user_id]['description'] = description
            
            sent_message = bot.send_message(user_id, "Please upload an image of your order.")
            message_ids[user_id].append(sent_message.message_id)
            message_ids[user_id].append(message.id)
            print(message_ids[message.from_user.id])
            clear_messages(message.from_user.id)
            markup = russian()
            bot.send_message(message.chat.id,
                              'Главный меню:\n     /log_into для верификации\n     /add_orders посмотреть заказы\n\n\n', reply_markup=markup)

            
            # bot.register_next_step_handler(message, handle_image)
        
        user_id = message.from_user.id
        category = message.text
        orders[user_id]['category'] = category
        
        sent_message = bot.send_message(user_id, "Please enter the description of your order.")
        message_ids[user_id].append(sent_message.message_id)
        message_ids[user_id].append(message.id)
        
        bot.register_next_step_handler(message, handle_description)
    
    orders[message.from_user.id] = {}
    message_ids[message.from_user.id] = []
    
    sent_message = bot.send_message(message.from_user.id, "Please enter the category.")
    message_ids[message.from_user.id].append(sent_message.message_id)
    message_ids[message.from_user.id].append(message.message_id)
    
    bot.register_next_step_handler(message, handle_category)


def clear_messages(user_id):
    for msg_id in message_ids[user_id]:
        bot.delete_message(user_id, msg_id)
    del message_ids[user_id]



print('\n.', '.', '.\n')
bot.polling(none_stop=True)