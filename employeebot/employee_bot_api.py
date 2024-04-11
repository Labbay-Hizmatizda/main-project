from datetime import datetime, time
import os
import telebot
from telebot.types import ReplyKeyboardRemove
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from markup import *
from api_integration import *

token = '6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8'
bot = telebot.TeleBot(token)

user_lang = {}
deletion = []
proposals = {}
image = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    print(user_id)
    lang = get_lang(user_id)
    if lang != None:
        if lang == 'ru':
            user_lang[message.from_user.id] = 'rus'
            markup = russian()
            message_smth = bot.send_message(message.chat.id, 'ㅤㅤㅤㅤ', reply_markup=ReplyKeyboardRemove())

            bot.delete_message(chat_id=message.chat.id, message_id=message_smth.id)
            bot.send_message(chat_id=message.chat.id,
                                text='Главный меню:\n     /kyc для верификации\n     /add_proposal посмотреть заказы\n\n\n', reply_markup=markup)
    elif lang == None:
        markup = types.InlineKeyboardMarkup()
        lang_rus = types.InlineKeyboardButton('🇷🇺 Русский', callback_data='lang_rus')
        lang_uz = types.InlineKeyboardButton('🇺🇿 O\'zbek tili', callback_data='lang_uz')

        markup.add(lang_rus, lang_uz)
        message_smth = bot.send_message(message.chat.id, 'ㅤㅤㅤㅤ', reply_markup=ReplyKeyboardRemove())
        bot.delete_message(user_id, message_smth.id)
        bot.send_message(message.chat.id, "Выберите язык 🌍\nTilni tanlang 🌍", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global proposals
    global image
    if call.data == 'lang_rus':
        user_id = call.from_user.id
        patch_lang(user_id, 'ru')
        user_lang[call.from_user.id] = 'rus'
        markup = russian()
        message_smth = bot.send_message(call.message.chat.id, 'ㅤㅤㅤㅤ', reply_markup=ReplyKeyboardRemove())
        
        bot.delete_message(chat_id=call.message.chat.id, message_id=message_smth.id)
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
        directory = os.path.join("media", "cv_photo", str(user_id))
        photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
        image_id = bot.send_photo(call.message.chat.id, photo=open(photo_path, 'rb'))
        message_id = image_id.message_id
        image[user_id] = message_id
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f"{text}Какое действие вы хотите сделать :......", reply_markup=markup)

    elif call.data == 'change_photo':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id

        markup = cancel_rus()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Отправьте ваше новое фото', reply_markup=markup)    
        bot.register_next_step_handler(call.message, change_photo, message_id = message_id)

    elif call.data == 'change_phonenumber_rus':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id

        markup = cancel_rus()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Напишите ваш новый номер', reply_markup=markup)    
        bot.register_next_step_handler(call.message, change_phonenumber_rus, message_id = message_id)
    
    elif call.data == 'change_name_rus':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id

        markup = cancel_rus()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Напишите ваше имя', reply_markup=markup)    
        bot.register_next_step_handler(call.message, change_name_rus, message_id = message_id)
        
    elif call.data == 'change_surname_rus':
        user_id = call.from_user.id
        chat_id = call.message.chat.id
        message_id = call.message.message_id

        markup = cancel_rus()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Напишите вашу фамилию', reply_markup=markup)
        bot.register_next_step_handler(call.message, change_surname_rus, message_id = message_id)
        
    elif call.data == 'change_language_rus':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id

        markup = change_lang___rus()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Выберите язык 🇷🇺/🇺🇿', reply_markup=markup)    

    elif call.data == 'identify_lang_rus':
        user_id = call.from_user.id
        markup = my_account_rus()
        message_id=call.message.id

        delete__message(user_id, message_id)
        print(patch_lang(user_id, 'ru'))
        response = get_employee(user_id)
        text = f'''
User ID : {response[0]['user_id']}
Имя : {response[0]['name']}
Фамилия : {response[0]['surname']}
Телефон номера : {response[0]['phone_number']}\n\n
        '''
        directory = os.path.join("media", "cv_photo", str(user_id))
        photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
        image_id = bot.send_photo(call.message.chat.id, photo=open(photo_path, 'rb'))
        message_id = image_id.message_id
        image[user_id] = message_id
        bot.send_message(chat_id=call.message.chat.id,
                              text=f"{text}|-|-|-|-|-|-|-|-|", reply_markup=markup)
    
    elif call.data == 'identify_lang_uz':
        user_id = call.from_user.id
        message_id=call.message.id

        delete__message(user_id, message_id)
        print(patch_lang(user_id, 'uz'))

        response = get_employee(user_id)
        text = f'''
User ID : {response[0]['user_id']}
Isim : {response[0]['name']}
Sharif : {response[0]['surname']}
Telefon nomer : +{response[0]['phone_number']}\n\n
        '''
        directory = os.path.join("media", "cv_photo", str(user_id))
        photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
        image_id = bot.send_photo(call.message.chat.id, photo=open(photo_path, 'rb'))
        message_id = image_id.message_id
        image[user_id] = message_id

        markup = my_account_rus()
        bot.send_message(chat_id=call.message.chat.id,
                              text=f"{text}\n|-|-|-|-|-|-|-|-|", reply_markup=markup)


    elif call.data == 'back_to_main_menu_rus' or call.data == 'about_us_back_menu':
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Главный меню:\n     /kyc для верификации\n     /add_proposal посмотреть заказы'.format(
                                  call.from_user.first_name), reply_markup=markup)
    elif call.data == 'proposals_rus' or call.data == 'back_orders' or call.data == 'back_proposals':
        markup = proposals_rus()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Какое действие вы хотите сделать :', reply_markup=markup)
    elif call.data == 'pending_proposals':
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
        message_id = call.message.message_id

        proposals[user_id] = {}
        deletion.append(call.message.id)
        sent_message = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Напишите ID заказа к которому вы хотите откликнутся!")
        deletion.append(sent_message.id)
        bot.register_next_step_handler(call.message, handle_id, message_id=message_id)

        


    # --uzbek lang ---------------------------------------------------------------------------------------------

    if call.data == 'lang_uz':
        user_id = call.from_user.id
        patch_lang(user_id, 'uz')
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


'''
id = image.get(user_id)

if id:
    delete__message(user_id, id)
    image[user_id] = None
elif id == None:
    pass
    
'''


@bot.message_handler(commands=['add_proposal'])
def handle_add_proposal(message):
    message_id = message.message_id
    proposals[message.from_user.id] = {}
    proposals[message.from_user.id]['owner_id'] = message.from_user.id
    
    bot.send_message(message.from_user.id, "Please write the ID of the order you want to send apply")
    bot.register_next_step_handler(message, handle_id, message_id = message_id)



def handle_id(message, message_id):
    message_id = message.message_id
    user_id = message.from_user.id
    order_id = message.text
    proposals[user_id]['order_id'] = order_id

    delete__message(user_id, message_id)
    delete__message(user_id, message.id)

    bot.send_message(user_id, "Напишите сумму денег которых вы хотите получить после успешного выполнения заказа!")
    bot.register_next_step_handler(message, inset_to_db, message_id = message_id)


def inset_to_db(message, message_id):
    user_id = message.from_user.id
    price = message.text
    proposals[user_id]['price'] = price

    delete__message(user_id, message_id)
    delete__message(user_id, message.id)

    proposals_data = proposals[user_id]
    print(post_proposal(proposals_data['order_id'], proposals_data['price'], user_id))
    markup = proposals_rus()
    delete = bot.send_message(user_id, "Proposal added successfully!, you can see all your responses in the markup called \"active proposals\"")
    time.sleep(3)
    delete__message(user_id, delete.id)
    bot.send_message(user_id, 'Какое действие вы хотите сделать :', reply_markup=markup)




@bot.message_handler(commands=['kyc'])
def kyc(message):
    ...



def change_photo(message, message_id):
    if message.content_type == 'photo':
        user_id = message.from_user.id
        directory = os.path.join("media", "cv_photo", str(user_id))

        os.makedirs(directory, exist_ok=True)
        
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        downloaded_file = bot.download_file(file_path)

        image_path = os.path.join(directory, f'{str(user_id)}.jpg')
        with open(image_path, 'wb') as photo:
            photo.write(downloaded_file)

        delete__message(user_id, message_id)
        delete__message(user_id, message.id)        
        response = get_employee(user_id)
        text = f'''
User ID : {response[0]['user_id']}
Isim : {response[0]['name']}
Sharif : {response[0]['surname']}
Telefon nomer : +{response[0]['phone_number']}\n\n
        '''
        markup = my_account_rus()
        photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
        image_id = bot.send_photo(message.chat.id, photo=open(photo_path, 'rb'))
        message_id = image_id.message_id
        image[user_id] = message_id
        bot.send_message(user_id, f"{text}", reply_markup=markup)
    else:
        bot.send_message(message)
        bot.register_next_step_handler(message, change_photo)


def change_phonenumber_rus(message, message_id):
    user_id = message.from_user.id
    value = message.text
    delete__message(user_id, message_id)
    delete__message(user_id, message.id)

    print(patch_employees(user_id, value, 'phone'))

    response = get_employee(user_id)
    text = f'''
User ID : {response[0]['user_id']}
Isim : {response[0]['name']}
Sharif : {response[0]['surname']}
Telefon nomer : +{response[0]['phone_number']}\n\n
        '''
    markup = my_account_rus()
    directory = os.path.join("media", "cv_photo", str(user_id))
    photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
    image_id = bot.send_photo(message.chat.id, photo=open(photo_path, 'rb'))
    message_id = image_id.message_id
    image[user_id] = message_id
    bot.send_message(user_id, f"{text}", reply_markup=markup)

def change_name_rus(message, message_id):
    user_id = message.from_user.id
    value = message.text
    delete__message(user_id, message_id)
    delete__message(user_id, message.id)

    print(patch_employees(user_id, value, 'name'))

    response = get_employee(user_id)
    text = f'''
User ID : {response[0]['user_id']}
Isim : {response[0]['name']}
Sharif : {response[0]['surname']}
Telefon nomer : +{response[0]['phone_number']}\n\n
        '''
    markup = my_account_rus()
    directory = os.path.join("media", "cv_photo", str(user_id))
    photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
    image_id = bot.send_photo(message.chat.id, photo=open(photo_path, 'rb'))
    message_id = image_id.message_id
    image[user_id] = message_id    
    bot.send_message(user_id, f"{text}", reply_markup=markup)

def change_surname_rus(message, message_id):
    user_id = message.from_user.id
    value = message.text
    delete__message(user_id, message_id)   
    delete__message(user_id, message.id)

    print(patch_employees(user_id, value, 'surname'))

    response = get_employee(user_id)
    text = f'''
User ID : {response[0]['user_id']}
Isim : {response[0]['name']}
Sharif : {response[0]['surname']}
Telefon nomer : +{response[0]['phone_number']}\n\n
        '''
    markup = my_account_rus()
    directory = os.path.join("media", "cv_photo", str(user_id))
    photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
    image_id = bot.send_photo(message.chat.id, photo=open(photo_path, 'rb'))
    message_id = image_id.message_id
    image[user_id] = message_id
    bot.send_message(user_id, f"{text}", reply_markup=markup)



def delete__message(chat_id, message_id):
    bot.delete_message(chat_id, message_id)



print('\n.', '.', '.\n')
bot.polling(none_stop=True)