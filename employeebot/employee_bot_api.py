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

token = '6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8'
bot = telebot.TeleBot(token)

user_lang = {}
deletion = []
proposals = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    lang_rus = types.InlineKeyboardButton('🇷🇺 Русский', callback_data='lang_rus')
    lang_uz = types.InlineKeyboardButton('🇺🇿 O\'zbek tili', callback_data='lang_uz')

    markup.add(lang_rus, lang_uz)
    bot.send_message(message.chat.id, "Выберите язык 🌍\nTilni tanlang 🌍", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global proposals
    if call.data == 'lang_rus':
        user_lang[call.from_user.id] = 'rus'
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Главный меню:\n     /kyc для верификации\n     /add_proposal посмотреть заказы\n\n\n', reply_markup=markup)
    elif call.data == 'about_us_rus':
        markup = types.InlineKeyboardMarkup()
        url = types.InlineKeyboardButton(text='Наш сайт ', url='https://youtube.com')
        back = types.InlineKeyboardButton('◀ Назад', callback_data='about_us_back_menu')
        markup.add(url, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Наш сайт ⏬", reply_markup=markup)
    elif call.data == 'my_account_rus' or call.data == 'cancel_rus':
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
    

    elif call.data == 'change_photo':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id

        markup = cancel_rus()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Отправьте ваше новое фото', reply_markup=markup)    
        bot.register_next_step_handler(call.message, change_photo)

    elif call.data == 'change_phonenumber_rus':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id
        markup = cancel_rus()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Напишите ваш новый номер', reply_markup=markup)    
        bot.register_next_step_handler(call.message, change_phonenumber_rus)
    
    elif call.data == 'change_name_rus':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id

        markup = cancel_rus()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Напишите ваше имя', reply_markup=markup)    
        bot.register_next_step_handler(call.message, change_name_rus)
        
    elif call.data == 'change_surname_rus':
        user_id = call.from_user.id
        chat_id = call.message.chat.id
        message_id=call.message.id


        markup = cancel_rus()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Напишите вашу фамилию', reply_markup=markup)    
        bot.register_next_step_handler(call.message, change_surname_rus)
        
    elif call.data == 'change_language_rus':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id

        markup = change_lang___rus()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Выберите язык 🇷🇺/🇺🇿', reply_markup=markup)    

    elif call.data == 'identify_lang_rus':
        user_id = call.from_user.id
        markup = my_account_rus()
        print(patch_lang(user_id))
        response = get_employee(user_id)
        text = f'''
User ID : {response[0]['user_id']}
Имя : {response[0]['name']}
Фамилия : {response[0]['surname']}
Телефон номера : {response[0]['phone_number']}\n\n
        '''
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f"{text}|-|-|-|-|-|-|-|-|", reply_markup=markup)
    
    elif call.data == 'identify_lang_uz':
        user_id = call.from_user.id
        markup = my_account_rus()
        print(patch_lang(user_id, 'uz'))
        response = get_employee(user_id)
        text = f'''
User ID : {response[0]['user_id']}
Isim : {response[0]['name']}
Sharif : {response[0]['surname']}
Telefon nomer : +{response[0]['phone_number']}\n\n
        '''
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f"{text}\n|-|-|-|-|-|-|-|-|", reply_markup=markup)


    elif call.data == 'back_to_main_menu_rus' or call.data == 'about_us_back_menu':
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Главный меню:\n     /kyc для верификации\n     /add_proposal посмотреть заказы'.format(
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
        print(response)
        text = ""
        for proposals in response:
            text += f"ID : {proposals['id']}\nOwner_id : {proposals['owner_id']}\nOrder_id : {proposals['order_id']}\nPrice : {proposals['price']}\n\n"

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{text}', reply_markup=markup)    
    elif call.data == 'proposals_history':
        ...
    elif call.data == 'new_proposal': 
        user_id = call.message.chat.id
        proposals[user_id] = {}
        deletion.append(call.message.id)
        sent_message = bot.send_message(user_id, "Please write the ID of the order you want to send apply")
        deletion.append(sent_message.id)
        bot.register_next_step_handler(call.message, handle_id)

        


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

def change_photo(message):
    if message.content_type == 'photo':
        user_id = message.from_user.id
        directory = os.path.join("media", "cv_photo", str(user_id))

        os.makedirs(directory, exist_ok=True)
        
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        downloaded_file = bot.download_file(file_path)

        image_path = os.path.join(directory, f'{str(user_id)}.jpg')
        print(image_path)
        with open(image_path, 'wb') as photo:
            photo.write(downloaded_file)
        bot.delete_message(user_id, message.id)
        
        response = get_employee(user_id)
        text = f'''
User ID : {response[0]['user_id']}
Isim : {response[0]['name']}
Sharif : {response[0]['surname']}
Telefon nomer : +{response[0]['phone_number']}\n\n
        '''
        markup = my_account_rus()
        bot.send_message(user_id, f"{text}", reply_markup=markup)
    else:
        bot.register_next_step_handler(message, change_photo)


def change_phonenumber_rus(message):
    user_id = message.from_user.id
    value = message.text

    print(patch_employees(user_id, value, 'phone'))

def change_name_rus(message):
    user_id = message.from_user.id
    value = message.text
    print(patch_employees(user_id, value, 'name'))

def change_surname_rus(message):
    user_id = message.from_user.id
    value = message.text
    print(patch_employees(user_id, value, 'surname'))





@bot.message_handler(commands=['add_proposal'])
def handle_add_proposal(message):
    proposals[message.from_user.id] = {}
    proposals[message.from_user.id]['owner_id'] = message.from_user.id
    deletion.append(message.id)
    sent_message = bot.send_message(message.from_user.id, "Please write the ID of the order you want to send apply")
    deletion.append(sent_message.id)
    bot.register_next_step_handler(message, handle_id)



def handle_id(message):
    user_id = message.from_user.id
    deletion.append(message.id)
    order_id = message.text
    proposals[user_id]['order_id'] = order_id
    for msg_id in deletion:
        try:
            bot.delete_message(user_id, msg_id)
        except Exception as e:
            pass
    deletion.clear()
    sent_message = bot.send_message(user_id, "Please write the amount of money you want to receive")
    deletion.append(sent_message.id)
    bot.register_next_step_handler(message, inset_to_db)


def inset_to_db(message):
    user_id = message.from_user.id
    deletion.append(message.id)
    price = message.text
    proposals[user_id]['price'] = price

    proposals_data = proposals[user_id]
    
    print(post_proposal(proposals_data['order_id'], proposals_data['price'], user_id))
    for msg_id in deletion:
        try:
            bot.delete_message(user_id, msg_id)
        except Exception as e:
            pass
    deletion.clear()
    bot.send_message(user_id, "Proposal added successfully!, you can see all your responses in the markup called \"active proposals\"")

@bot.message_handler(commands=['kyc'])
def kyc(message):
    ...


print('\n.', '.', '.\n')
bot.polling(none_stop=True)