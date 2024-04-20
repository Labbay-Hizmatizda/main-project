from datetime import datetime, time
import os
import telebot
from telebot.types import ReplyKeyboardRemove
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from markup import *
from api_integration import *
# 6890785425:AAHJuDftXxnKdr5VhVQewZx4XcTvMV3DKD0
# @labbay_employer_bot


# fix                           IN PRIORITY                                
# TODO |>!<| 106-133 line
# TODO |>!<| create a log_in function, add basic values of employee



# FIX ALL THIS !!!!!!!!                                                    #
# TODO |>1<| add POSTing CV( get code from change_image() )| 489 field     #
# TODO |>2<| connect add_cv logic to the addaptive markups in my_info      #
# TODO |>3<| after ending add_cv logics                                    #
# TODO |>4<| add proposal canceling                                        #
# TODO |>6<| add rating and bio insight of the my_account                  #
# TODO |>5<| add markups in active proposals by ID                         #
# TODO |>6<| add output of proposal detail and order's information         #

# FIX LATER                                                                #
# TODO |>7<| THINK ABOUT NOTIFICATION LOGICS               #FIX            #
# TODO |>8<|                                                               #





token = '7150191995:AAG-bNdv-1fxsF-Jbc-EvEGYagRcSSxOCYo'
bot = telebot.TeleBot(token)

deletion = []
proposals = {}
login_ = {}
registration = {}
cvs = {}
image = {}
proposal_image=0

@bot.message_handler(commands=['start'])
def start(message): 
    user_id = message.from_user.id
    print(user_id)
    lang = get_lang(user_id)
    if lang != None or lang != []:
        if lang == 'ru':    

            markup = russian()
            message_empty = bot.send_message(message.chat.id, 'ㅤ', reply_markup=ReplyKeyboardRemove())

            delete__message(chat_id=message.chat.id, message_id=message_empty.id)
            bot.send_message(message.chat.id,
                                  'Главный меню:\n/add_proposal откликнуться на заказ\n\n\n', reply_markup=markup)
            print(patch_lang(user_id, 'ru'))
            
        elif lang == 'uz':
            markup = uzbek()
            message_empty = bot.send_message(message.chat.id, 'ㅤ', reply_markup=ReplyKeyboardRemove())
            
            delete__message(chat_id=message.chat.id, message_id=message_empty.id)
            bot.send_message(message.chat.id,
                                  'Glavniy menyu:\n\n/add_proposal - Otkliknutsa na zakaz\n\n\n', reply_markup=markup)
            print(patch_lang(user_id, 'uz'))
        else:
            markup = types.InlineKeyboardMarkup()
            lang_rus = types.InlineKeyboardButton('🇷🇺 Русский', callback_data='lang_rus')
            lang_uz = types.InlineKeyboardButton('🇺🇿 O\'zbek tili', callback_data='lang_uz')
            markup.add(lang_rus, lang_uz)

            message_smth = bot.send_message(message.chat.id, 'ㅤ', reply_markup=ReplyKeyboardRemove())
            delete__message(user_id, message_smth.id)
            bot.send_message(message.chat.id, "Выберите язык 🌍\nTilni tanlang 🌍", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global proposals
    global image
    global proposal_image
    
    if call.data == 'lang_rus':
        user_id = call.from_user.id
        try:
            patch_lang(user_id, 'ru')
        except:
            ...
        markup = russian()
        message_smth = bot.send_message(call.message.chat.id, 'ㅤㅤㅤㅤ', reply_markup=ReplyKeyboardRemove())
        
        bot.delete_message(chat_id=call.message.chat.id, message_id=message_smth.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Главный меню:\n/add_proposal откликнуться на заказ\n\n\n', reply_markup=markup)
    
    elif call.data == 'about_us_rus':
        markup = types.InlineKeyboardMarkup()
        url = types.InlineKeyboardButton(text='Наш сайт ', url='https://youtube.com')
        back = types.InlineKeyboardButton('◀ Назад', callback_data='about_us_back_menu')
        markup.add(url, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Наш сайт ⏬", reply_markup=markup)
    
    elif call.data == 'my_account_rus' or call.data == 'cancel_rus':
        user_id = call.from_user.id
        response = get_employee(user_id)
        if response != None:
            delete__message(user_id, call.message.id)
            markup = my_account_rus()
            text = f'''
    ID : {response[0]['user_id']}
Имя : {response[0]['name']}
Фамилия : {response[0]['surname']}
Телефон номера : +{response[0]['phone_number']}\n\n
            '''
            try:
                directory = os.path.join("media", "cv_photo", str(user_id))
                photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
                image_id = bot.send_photo(call.message.chat.id, photo=open(photo_path, 'rb'))
                message_id = image_id.message_id
                user = str(user_id)
                image[user] = message_id
            except:
                ...
            bot.send_message(call.message.chat.id,
                                f"{text}Какое действие вы хотите сделать :......", reply_markup=markup)
            
        else:
            markup = authorizing()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"Пожалуйста зарегайтесь или войдите в свой аккаунт чтобы получить эти функции", reply_markup=markup)

    elif call.data == 'login':
        user_id = call.from_user.id
        login_[user_id] = {}
        login_[user_id]['owner_id'] = user_id
        message__id = bot.edit_message_text(chat_id=user_id, message_id=call.message.id, text="Ваше имя ....")

        message_id = message__id.id
        bot.register_next_step_handler(message__id, login, message_id=message_id, language='ru')

    elif call.data == 'registrate':
        ...

    elif call.data == 'change_photo':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id
        
        user = str(user_id)
        try:
            delete__message(user_id, image[user])
        except:
            ...
        markup = cancel_ru()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Отправьте ваше новое фото', reply_markup=markup)    
        bot.register_next_step_handler(call.message, change_photo, message_id = message_id, lang='ru')

    elif call.data == 'change_phonenumber_rus':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id

        user = str(user_id)
        try:
            delete__message(user_id, image[user])
        except:
            ...

        markup = cancel_ru()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Напишите ваш новый номер', reply_markup=markup)    
        bot.register_next_step_handler(call.message, change_phonenumber_rus, message_id=message_id, lang='ru')
    
    elif call.data == 'change_name_rus':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id

        user = str(user_id)
        try:
            delete__message(user_id, image[user])
        except:
            ...

        markup = cancel_ru()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Напишите ваше имя', reply_markup=markup)    
        bot.register_next_step_handler(call.message, change_name_rus, message_id=message_id, lang='ru')
        
    elif call.data == 'change_surname_rus':
        user_id = call.from_user.id
        chat_id = call.message.chat.id
        message_id = call.message.message_id

        user = str(user_id)
        try:
            delete__message(user_id, image[user])
        except:
            ...
        markup = cancel_ru()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Напишите вашу фамилию', reply_markup=markup)
        bot.register_next_step_handler(call.message, change_surname_rus, message_id=message_id, lang='ru')
        
    elif call.data == 'change_language_rus':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id
        user = str(user_id)
        try:
            delete__message(user_id, image[user])
        except:
            ...

        markup = change_lang___rus()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Выберите язык 🇷🇺/🇺🇿', reply_markup=markup)    

    elif call.data == 'identify_lang_rus':
        user_id = call.from_user.id
        markup = my_account_rus()
        message_id=call.message.id
        delete__message(user_id, message_id)



        response = get_employee(user_id)
        text = f'''
ID : {response[0]['user_id']}
Имя : {response[0]['name']}
Фамилия : {response[0]['surname']}
Телефон номера : +{response[0]['phone_number']}\n\n
        '''
        directory = os.path.join("media", "cv_photo", str(user_id))
        photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
        image_id = bot.send_photo(call.message.chat.id, photo=open(photo_path, 'rb'))
        message_id = image_id.message_id
        user = str(user_id)
        image[user] = message_id

        bot.send_message(chat_id=call.message.chat.id,
                              text=f"{text}\n\nКакое действие вы хотите сделать :......", reply_markup=markup)
        print(patch_lang(user_id, 'ru'))

    elif call.data == 'back_to_main_menu_rus':
        markup = russian()
        user_id = call.from_user.id
        user = str(user_id)
        print(image)
        try:
            try:
                delete__message(user_id, image[user])
            except:
                ...
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text='Главный меню:\n     /kyc для верификации\n     /add_proposal посмотреть заказы'
                                  .format(call.from_user.first_name), 
                                  reply_markup=markup)
        except Exception:
            bot.send_message(user_id, "Просим прощения за не удобства, напишите заново /start")       
    
    elif call.data == 'about_us_back_menu':
        markup = russian()
        user_id = call.from_user.id

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Главный меню:\n     /kyc для верификации\n     /add_proposal посмотреть заказы'.format(
                                  call.from_user.first_name), reply_markup=markup)
    
    elif call.data == 'proposals_rus' or call.data == 'back_orders' or call.data == 'back_proposals':
        user_id = call.from_user.id
        response = get_employee(user_id)
        if response != None:
            user_id = call.from_user.id
            markup = proposals_rus()
            request_true, request_false = get_proposals(user_id, 'true'), get_proposals(user_id, 'false')

            request_false = '' if request_false == None else request_false
            request_true = '' if request_true == None else request_true

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Отликов в ожидании : {len(request_true)}\nИстория откликов : {len(request_false)}\n\nТут все, что связано с работой.\nНажмите одну из кнопок, чтобы посмотреть соответствующую функцию', reply_markup=markup)

        else:
            markup = authorizing()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"Пожалуйста зарегайтесь или войдите в свой аккаунт чтобы получить эти функции", reply_markup=markup)

    elif call.data == 'pending_proposals':
        markup = pending_proposals_rus()
        user_id = call.from_user.id

        response = get_proposals(user_id, 'true')
        if response:
            text = ""
            for proposals in response:
                text += f"ID : {proposals['id']}\nOwner_id : {proposals['owner_id']}\nOrder_id : {proposals['order_id']}\nPrice : {proposals['price']}\n\n"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{text}', reply_markup=markup)    
        else: 
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='У вас пока нет откликов :(', reply_markup=markup)    
    
    elif call.data == 'proposals_history':
        markup = pending_proposals_rus()
        user_id = call.from_user.id

        response = get_proposals(user_id, 'false')
        if response:
            print(response)
            text = ""
            for proposals in response:
                text += f"ID : {proposals['id']}\nOwner_id : {proposals['owner_id']}\nOrder_id : {proposals['order_id']}\nPrice : {proposals['price']}\n\n"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{text}', reply_markup=markup)    
        else: 
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='У вас нет истории откликов :(', reply_markup=markup)    
 
    elif call.data == 'new_proposal': 
        user_id = call.message.chat.id
        message_id = call.message.message_id

        lang = get_lang(user_id)
        proposals[user_id] = {}
        sent_message = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Напишите ID заказа к которому вы хотите откликнутся!")
        bot.register_next_step_handler(call.message, handle_id, message_id=message_id, language=lang)


    # --uzbek lang ---------------------------------------------------------------------------------------------
    if call.data == 'lang_uz':
        user_id = call.from_user.id
        try:
            patch_lang(user_id, 'uz')
        except:
            ...
        markup = uzbek()
        message_smth = bot.send_message(call.message.chat.id, 'ㅤㅤㅤㅤ', reply_markup=ReplyKeyboardRemove())
        
        bot.delete_message(chat_id=call.message.chat.id, message_id=message_smth.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Glavniy menyu:\n\n/add_proposal - Otkliknutsa na zakaz\n\n\n', reply_markup=markup)
    
    elif call.data == 'about_us_uz':
        markup = types.InlineKeyboardMarkup()
        url = types.InlineKeyboardButton(text='LabbayHizmat ', url='https://youtube.com')
        back = types.InlineKeyboardButton('Orqaga ◀️', callback_data='about_us_back_menu_uz')
        markup.add(url, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Bizning sayt⏬", reply_markup=markup)
    
    elif call.data == 'my_account_uz' or call.data == 'cancel_uz':
        user_id = call.from_user.id
        response = get_employee(user_id)
        if response != None:
            delete__message(user_id, call.message.id)
            print(response)
            text = f'''
        User ID : {response[0]['user_id']}
    Isim : {response[0]['name']}
    Sharif : {response[0]['surname']}
    Telefon nomer : +{response[0]['phone_number']}\n\n
                '''
            directory = os.path.join("media", "cv_photo", str(user_id
                                                              
                                                              ))
            photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
            try:
                image_id = bot.send_photo(call.message.chat.id, photo=open(photo_path, 'rb'))
                message_id = image_id.message_id
                user = str(user_id)
                image[user] = message_id
            except:
                ...
            markup = my_account_uz()
            bot.send_message(user_id,
                                f"{text}\n\nNma qilmohchisiz :......", reply_markup=markup)
        else:  
            markup = authorizing_uz()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Bu funksiyani ishlatish uchun, iltimos akkauntingizga kiring yoki yengi yarating!", reply_markup=markup)

    elif call.data == 'login_uz':
        user_id = call.from_user.id
        login_[user_id] = {}
        login_[user_id]['owner_id'] = user_id
        message__id = bot.edit_message_text(chat_id=user_id, message_id=call.message.id, text="Iltimos ismingizni yozing!")

        message_id = message__id.id
        bot.register_next_step_handler(message__id, login, message_id=message_id, language='uz')

    elif call.data == 'registrate_uz':        ...

    elif call.data == 'change_photo_uz':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id
        
        user = str(user_id)
        try:
            delete__message(user_id, image[user])
        except:
            ...
        markup = cancel_uz()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Suratingizni yuboring', reply_markup=markup)    
        bot.register_next_step_handler(call.message, change_photo, message_id=message_id, lang='uz')

    elif call.data == 'change_phonenumber_uz':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id

        user = str(user_id)
        delete__message(user_id, image[user])

        markup = cancel_uz()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Nomeringizni yozing', reply_markup=markup)    
        bot.register_next_step_handler(call.message, change_phonenumber_rus, message_id=message_id, lang='uz')
    
    elif call.data == 'change_name_uz':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id

        user = str(user_id)
        delete__message(user_id, image[user])

        markup = cancel_uz()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Ismingizni yozing', reply_markup=markup)    
        bot.register_next_step_handler(call.message, change_name_rus, message_id=message_id, lang='uz')
        
    elif call.data == 'change_surname_uz':
        user_id = call.from_user.id
        chat_id = call.message.chat.id
        message_id = call.message.message_id

        user = str(user_id)
        delete__message(user_id, image[user])

        markup = cancel_uz()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Sharifingizni yozing', reply_markup=markup)
        bot.register_next_step_handler(call.message, change_surname_rus, message_id=message_id, lang='uz')
        
    elif call.data == 'change_language_uz':
        user_id = call.from_user.id
        chat_id=call.message.chat.id
        message_id=call.message.id
        user = str(user_id)
        try:
            delete__message(user_id, image[user])
        except:
            ...

        markup = change_lang___uz()
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Tilni tanlang 🇷🇺/🇺🇿', reply_markup=markup)    

    elif call.data == 'identify_lang_uz':
        user_id = call.from_user.id
        message_id=call.message.id
        delete__message(user_id, message_id)
        
        print(patch_lang(user_id, 'uz'))
        response = get_employee(user_id)
        text = f'''
ID : {response[0]['user_id']}
Isim : {response[0]['name']}
Sharif : {response[0]['surname']}
Telefon nomer : +{response[0]['phone_number']}\n\n
        '''
        directory = os.path.join("media", "cv_photo", str(user_id))
        photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
        image_id = bot.send_photo(call.message.chat.id, photo=open(photo_path, 'rb'))
        message_id = image_id.message_id
        user = str(user_id)
        image[user] = message_id
        markup = my_account_uz()

        bot.send_message(user_id, f"{text}\n\nNma qilmohchisiz :......", reply_markup=markup)

    elif call.data == 'back_to_main_menu_uz':
        markup = uzbek()
        user_id = call.from_user.id
        user = str(user_id)
        print(image)
        try:
            try:
                delete__message(user_id, image[user])
            except:
                ...
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text='Glavniy menyu:\n\n/add_proposal - Otkliknutsa na zakaz\n\n\n'
                                  .format(call.from_user.first_name), 
                                  reply_markup=markup)
        except Exception:
            bot.send_message(user_id, "Noqulayliklar uchun uzur so\'raymiz, /start ni yana bir marotaba bosing")       
    
    elif call.data == 'about_us_back_menu_uz':
        markup = uzbek()
        user_id = call.from_user.id

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='Glavniy menyu:\n\n/add_proposal - Otkliknutsa na zakaz\n\n\n'.format(
                                  call.from_user.first_name), reply_markup=markup)
    
    elif call.data == 'proposals_uz' or call.data == 'back_orders_uz' or call.data == 'back_proposals_uz':
        user_id = call.from_user.id

        response = get_employee(user_id)
        if response != None:  
            # try:
            markup = proposals_uz()
            request_true, request_false = get_proposals(user_id, 'true'), get_proposals(user_id, 'false')

            request_false = '' if request_false == None else request_false
            request_true = '' if request_true == None else request_true
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'Kutilayotgan taklif : {len(request_true)}\nTakliflar tarixi : {len(request_false)}\n\nIshga bog\'liq funksiyalar shu yerda.\nQaysidur o\'zingizga kerakli knopkani bosing', reply_markup=markup)
            
        else:
            markup = authorizing_uz()
            message_id = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Bu funksiyani ishlatish uchun, iltimos akkauntingizga kiring yoki yengi yarating!", reply_markup=markup)

    elif call.data == 'pending_proposals_uz':
        markup = pending_proposals_uz()
        user_id = call.from_user.id

        response = get_proposals(user_id, 'true')
        if response:
            text = ""
            for proposals in response:
                text += f"ID : {proposals['id']}\nOwner_id : {proposals['owner_id']}\nOrder_id : {proposals['order_id']}\nPrice : {proposals['price']}\n\n"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{text}', reply_markup=markup)    
        else: 
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Siz hali taklif qoldirmagansiz :(', reply_markup=markup)    
    
    elif call.data == 'proposals_history_uz':
        markup = pending_proposals_uz()
        user_id = call.from_user.id

        response = get_proposals(user_id, 'false')
        if response:
            print(response)
            text = ""
            for proposals in response:
                text += f"ID : {proposals['id']}\nOwner_id : {proposals['owner_id']}\nOrder_id : {proposals['order_id']}\nPrice : {proposals['price']}\n\n"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f'{text}', reply_markup=markup)    
        else: 
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Siz hali takliflar tarixi yo\'q :(', reply_markup=markup)    
 
    elif call.data == 'new_proposal_uz':
        user_id = call.message.chat.id
        message_id = call.message.message_id

        proposals[user_id] = {}
        deletion.append(call.message.id)
        sent_message = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Taklif qoldirish uchun, zakazni IDsini yozing!")
        deletion.append(sent_message.id)
        bot.register_next_step_handler(call.message, handle_id, message_id=message_id)

'''
id = image.get(user_id)

if id:
    delete__message(user_id, id)
    image[user_id] = None
elif id == None:
    pass
    
'''


def login(message, message_id, language):
    user_id = message.from_user.id
    name = message.text
    login_[user_id]['name'] = name
    print('pre delete')
    delete__message(user_id, message.id)
    print(message.id)
    print('after')

    print('uje')

    if language == 'ru':
        message__id = bot.edit_message_text(chat_id=user_id, message_id=message_id,text="Ваше фамилия ....")
    elif language == 'uz':
        message__id = bot.edit_message_text(chat_id=user_id, message_id=message_id,text="Iltimos sharifingizni yozing!")
        # print(1)
    
    message_id = message__id.id
    bot.register_next_step_handler(message, surname, message_id=message_id, language=language)

def surname(message, message_id, language):
    user_id = message.from_user.id
    surname = message.text
    login_[user_id]['surname'] = surname

    # =(user_id, message_id)
    # print(2)
    print(message.id)
    delete__message(user_id, message.id)
    # print(message.id)

    '''
            m = 'XX-XXX-XX-XX'
            m = m.replace('-', '')
            print(m)
    '''
    if language == 'ru':
        message__id = bot.edit_message_text(chat_id=user_id, message_id=message_id,text="Ваш телефон номер\nПример: XX-XXX-XX-XX\n\n\nНапоминание‼️\nНа написанное вами номер придет смс код, введи ее чтобы подключить номер")
    elif language == 'uz':
        # print(3)
        message__id = bot.edit_message_text(chat_id=user_id, message_id=message_id,text="Nomeringizni yozing\nMasalan: XX-XXX-XX-XX\n\n\nEslatma‼️\nShu yozgan nomeringizga kod keladi kodni yuborasiz keyin akkaunt ulanadi")
    
    message_id = message__id.id
    bot.register_next_step_handler(message, login_insert_to_db, message_id=message_id, language=language)

def login_insert_to_db(message, message_id, language):
    user_id = message.from_user.id
    number = message.text
    login_[user_id]['number'] = number
    login_data = login_[user_id]
    
    if language == 'ru':
        language = 7

        loading_message = bot.edit_message_text(chat_id=user_id, message_id=message_id, text="Подождите, сохроняется ...")

        try:
            delete__message(user_id, message.id)
        except Exception as e:
            ...

        running = True
        while running:
            start_time = time.time()

            while time.time() - start_time < 2:
                time.sleep(0.1)
                bot.edit_message_text("Подождите, сохроняется .", message.chat.id, message_id=loading_message.message_id)
                time.sleep(0.1)
                bot.edit_message_text("Подождите, сохроняется ..", message.chat.id, message_id=loading_message.message_id)
                time.sleep(0.1)
                bot.edit_message_text("Подождите, сохроняется ...", message.chat.id, message_id=loading_message.message_id)
            running = False

        message_id = bot.edit_message_text(chat_id=message.chat.id, message_id=loading_message.id, text="Аккаунт создан ✔️")
        time.sleep(1)

        markup = russian()
        bot.edit_message_text(chat_id=message.chat.id, message_id=loading_message.id,
                              text='Главный меню:\n/add_proposal откликнуться на заказ\n\n\n', reply_markup=markup)
        print(post_employee(user_id, login_data['name'], login_data['surname'], login_data['number'], language))
    
    elif language == 'uz':
        language = 8
        loading_message = bot.edit_message_text(chat_id=user_id, message_id=message_id, text="Kuting, yuklanmoqda ...")
        
        try:
            delete__message(user_id, message.id)
        except Exception as e:
            ...
        
        running = True
        while running:
            start_time = time.time()

            while time.time() - start_time < 2:
                time.sleep(0.1)
                bot.edit_message_text("Kuting, yuklanmoqda .", message.chat.id, message_id=loading_message.message_id)
                time.sleep(0.1)
                bot.edit_message_text("Kuting, yuklanmoqda ..", message.chat.id, message_id=loading_message.message_id)
                time.sleep(0.1)
                bot.edit_message_text("Kuting, yuklanmoqda ...", message.chat.id, message_id=loading_message.message_id)
            running = False

        message_id = bot.edit_message_text(chat_id=message.chat.id, message_id=loading_message.id, text="Yuklandi ✔️")
        time.sleep(1)


        markup = uzbek()
        bot.edit_message_text(chat_id=message.chat.id, message_id=loading_message.id,
                              text='Glavniy menyu:\n\n/add_proposal - Otkliknutsa na zakaz\n\n\n', reply_markup=markup)
        print(post_employee(user_id, login_data['name'], login_data['surname'], login_data['number'], language))
        



@bot.message_handler(commands=['cv'])
def add_cv(message):

    user_id = message.from_user.id
    proposals[user_id] = {}
    proposals[user_id]['owner_id'] = user_id
    lang = get_lang(user_id)
    if lang == 'ru':
        message__id = bot.send_message(user_id, "Пожалуйста отправьте свою фотографию!")
    elif lang == 'uz':
        message__id = bot.send_message(user_id, "Iltimos ozingizni rasimingizni tashlang!")

    message_id = message__id.id
    bot.register_next_step_handler(message__id, bio, message_id=message_id, language=lang)

def bio(message, message_id, language):
    user_id = message.from_user.id
    image = message.text
    cvs[user_id]['image'] = image

    # =(user_id, message_id)
    delete__message(user_id, message.id)

    if language == 'ru':
        message__id = bot.edit_message_text(chat_id=user_id, message_id=message_id,text="Введите сумму денег за которую вы бы хотели получить, после выполнения работы удачно!")
    elif language == 'uz':
        message__id = bot.edit_message_text(chat_id=user_id, message_id=message_id,text="Buyurtmani muvaffaqiyatli bajarganingizdan so'ng olmoqchi bo'lgan miqdorni kiriting!")
    message_id = message__id.id
    bot.register_next_step_handler(message, cv_insert_to_db, message_id=message_id, language=language)

def cv_insert_to_db(message, message_id, language):
    user_id = message.from_user.id
    bio = message.text
    cvs[user_id]['bio'] = bio
    print(cvs)
    cvs_data = cvs[user_id]
    print(post_cv(cvs_data['image'], cvs_data['bio'], user_id))
    
    if language == 'ru':
        loading_message = bot.edit_message_text(chat_id=user_id, message_id=message_id, text="Подождите, сохроняется ...")

        try:
            delete__message(user_id, message.id)
        except Exception as e:
            ...

        running = True
        while running:
            start_time = time.time()

            while time.time() - start_time < 2:
                time.sleep(0.1)
                bot.edit_message_text("Подождите, сохроняется .", message.chat.id, message_id=loading_message.message_id)
                time.sleep(0.1)
                bot.edit_message_text("Подождите, сохроняется ..", message.chat.id, message_id=loading_message.message_id)
                time.sleep(0.1)
                bot.edit_message_text("Подождите, сохроняется ...", message.chat.id, message_id=loading_message.message_id)
            running = False

        message_id = bot.edit_message_text(chat_id=message.chat.id, message_id=loading_message.id, text="Отклик отправлен ✔️")
        time.sleep(1)

        markup = proposals_rus()
        bot.edit_message_text(chat_id=message.chat.id, message_id=loading_message.id, text="Тут все, что связано с работой.\n Нажмите одну из кнопок, чтобы посмотреть соответствующую функцию", reply_markup=markup)
    if language == 'uz':
        loading_message = bot.edit_message_text(chat_id=user_id, message_id=message_id, text="Kuting, taklif yuborilmoqda ...")
        
        try:
            delete__message(user_id, message.id)
        except Exception as e:
            ...
        
        running = True
        while running:
            start_time = time.time()

            while time.time() - start_time < 2:
                time.sleep(0.1)
                bot.edit_message_text("Kuting, yuklanmoqda .", message.chat.id, message_id=loading_message.message_id)
                time.sleep(0.1)
                bot.edit_message_text("Kuting, yuklanmoqda ..", message.chat.id, message_id=loading_message.message_id)
                time.sleep(0.1)
                bot.edit_message_text("Kuting, yuklanmoqda ...", message.chat.id, message_id=loading_message.message_id)
            running = False

        message_id = bot.edit_message_text(chat_id=message.chat.id, message_id=loading_message.id, text="Taklif yuborildi ✔️")
        time.sleep(1)

        markup = my_account_uz()
        bot.edit_message_text(chat_id=message.chat.id, message_id=loading_message.id, text="Ishga bog\'liq funksiyalar shu yerda.\nQaysidur o\'zingizga kerakli knopkani bosing", reply_markup=markup)



@bot.message_handler(commands=['add_proposal'])
def handle_add_proposal(message):

    user_id = message.from_user.id
    proposals[user_id] = {}
    proposals[user_id]['owner_id'] = user_id
    lang = get_lang(user_id)
    if lang == 'ru':
        message__id = bot.send_message(user_id, "Пожалуйста, напишите ID заказа, на который хотите подать заявку!")
    elif lang == 'uz':
        message__id = bot.send_message(user_id, "Taklif qoldirish uchun, zakazni IDsini yozing!")

    message_id = message__id.id
    bot.register_next_step_handler(message__id, handle_id, message_id=message_id, language=lang)

def handle_id(message, message_id, language):
    user_id = message.from_user.id
    order_id = message.text
    proposals[user_id]['order_id'] = order_id

    # delete__message(user_id, message_id)
    delete__message(user_id, message.id)

    if language == 'ru':
        message__id = bot.edit_message_text(chat_id=user_id, message_id=message_id,text="Напишите сумму денег, которую вы хотите получить после успешного выполнения заказа!")
    elif language == 'uz':
        message__id = bot.edit_message_text(chat_id=user_id, message_id=message_id,text="Buyurtmani muvaffaqiyatli bajarganingizdan so'ng olmoqchi bo'lgan miqdorni kiriting!")
    message_id = message__id.id
    bot.register_next_step_handler(message, proposal_insert_to_db, message_id=message_id, language=language)

def proposal_insert_to_db(message, message_id, language):
    user_id = message.from_user.id
    price = message.text
    proposals[user_id]['price'] = price
    print(proposals)
    proposals_data = proposals[user_id]
    print(post_proposal(proposals_data['order_id'], proposals_data['price'], user_id))
    
    if language == 'ru':
        loading_message = bot.edit_message_text(chat_id=user_id, message_id=message_id, text="Подождите, отправляем ваш запрос ...")

        try:
            delete__message(user_id, message.id)
        except Exception as e:
            ...

        running = True
        while running:
            start_time = time.time()

            while time.time() - start_time < 2:
                time.sleep(0.2)
                bot.edit_message_text("Подождите, отправляем ваш запрос .", message.chat.id, message_id=loading_message.message_id)
                time.sleep(0.2)
                bot.edit_message_text("Подождите, отправляем ваш запрос ..", message.chat.id, message_id=loading_message.message_id)
                time.sleep(0.2)
                bot.edit_message_text("Подождите, отправляем ваш запрос ...", message.chat.id, message_id=loading_message.message_id)
            running = False

        message_id = bot.edit_message_text(chat_id=message.chat.id, message_id=loading_message.id, text="Отклик отправлен ✔️")
        time.sleep(1)

        markup = proposals_rus()
        bot.edit_message_text(chat_id=message.chat.id, message_id=loading_message.id, text="Тут все, что связано с работой.\n Нажмите одну из кнопок, чтобы посмотреть соответствующую функцию", reply_markup=markup)
    if language == 'uz':
        loading_message = bot.edit_message_text(chat_id=user_id, message_id=message_id, text="Kuting, taklif yuborilmoqda ...")
        
        try:
            delete__message(user_id, message.id)
        except Exception as e:
            ...
        
        running = True
        while running:
            start_time = time.time()

            while time.time() - start_time < 2:
                time.sleep(0.1)
                bot.edit_message_text("Kuting, taklif yuborilmoqda .", message.chat.id, message_id=loading_message.message_id)
                time.sleep(0.1)
                bot.edit_message_text("Kuting, taklif yuborilmoqda ..", message.chat.id, message_id=loading_message.message_id)
                time.sleep(0.1)
                bot.edit_message_text("Kuting, taklif yuborilmoqda ...", message.chat.id, message_id=loading_message.message_id)
            running = False

        message_id = bot.edit_message_text(chat_id=message.chat.id, message_id=loading_message.id, text="Taklif yuborildi ✔️")
        time.sleep(1)

        markup = proposals_uz()
        bot.edit_message_text(chat_id=message.chat.id, message_id=loading_message.id, text="Ishga bog\'liq funksiyalar shu yerda.\nQaysidur o\'zingizga kerakli knopkani bosing", reply_markup=markup)



def change_photo(message, message_id, lang):
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

        try:
            directory = os.path.join("media", "cv_photo", str(user_id))
            photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
            image_id = bot.send_photo(message.chat.id, photo=open(photo_path, 'rb'))
            message_id = image_id.message_id
            user = str(user_id)
            image[user] = message_id
        except:
            ...
        if lang == 'ru':
            response = get_employee(user_id)
            text = f'''
    ID : {response[0]['user_id']}
Имя : {response[0]['name']}
Фамилия : {response[0]['surname']}
Телефон номера : +{response[0]['phone_number']}\n\n
            '''
            markup = my_account_rus()
            bot.send_message(user_id, f"{text}\n\nЧто вы хотите сделать :......", reply_markup=markup)
        elif lang == 'uz':
            response = get_employee(user_id)
            text = f'''
    ID : {response[0]['user_id']}
Isim : {response[0]['name']}
Sharif : {response[0]['surname']}
Telefon nomer : +{response[0]['phone_number']}\n\n
            '''
            markup = my_account_uz()
            bot.send_message(user_id, f"{text}\n\nNima qilmohchisiz :......", reply_markup=markup)
    else: 
        bot.register_next_step_handler(message, change_photo)

def change_phonenumber_rus(message, message_id, lang):
    user_id = message.from_user.id
    value = message.text

    delete__message(user_id, message_id)
    delete__message(user_id, message.id)

    try:
        directory = os.path.join("media", "cv_photo", str(user_id))
        photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
        image_id = bot.send_photo(message.chat.id, photo=open(photo_path, 'rb'))
        message_id = image_id.message_id
        user = str(user_id)
        image[user] = message_id
    except:
        ...
        
    if lang == 'ru':
        response = get_employee(user_id)
        text = f'''
    ID : {response[0]['user_id']}
Имя : {response[0]['name']}
Фамилия : {response[0]['surname']}
Телефон номера : +{response[0]['phone_number']}\n\n
            '''
        markup = my_account_rus()
        bot.send_message(user_id, f"{text}\n\nЧто вы хотите сделать :......", reply_markup=markup)
    elif lang == 'uz':
        response = get_employee(user_id)
        text = f'''
    ID : {response[0]['user_id']}
Isim : {response[0]['name']}
Sharif : {response[0]['surname']}
Telefon nomer : +{response[0]['phone_number']}\n\n
            '''
        markup = my_account_uz()
        bot.send_message(user_id, f"{text}\n\nNima qilmohchisiz :......", reply_markup=markup)
    print(patch_employees(user_id, value, 'phone'))

def change_name_rus(message, message_id, lang):
    user_id = message.from_user.id
    value = message.text

    delete__message(user_id, message_id)
    delete__message(user_id, message.id)


    try:
        directory = os.path.join("media", "cv_photo", str(user_id))
        photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
        image_id = bot.send_photo(message.chat.id, photo=open(photo_path, 'rb'))
        message_id = image_id.message_id
        user = str(user_id)
        image[user] = message_id
    except:
        ...
        
    if lang == 'ru':  
        response = get_employee(user_id)
        text = f'''
    ID : {response[0]['user_id']}
Имя : {response[0]['name']}
Фамилия : {response[0]['surname']}
Телефон номера : +{response[0]['phone_number']}\n\n
            '''
        markup = my_account_rus()
        bot.send_message(user_id, f"{text}\n\nЧто вы хотите сделать :......", reply_markup=markup)
    elif lang == 'uz':
        response = get_employee(user_id)
        text = f'''
    ID : {response[0]['user_id']}
Isim : {response[0]['name']}
Sharif : {response[0]['surname']}
Telefon nomer : +{response[0]['phone_number']}\n\n
            '''
        markup = my_account_uz()
        bot.send_message(user_id, f"{text}\n\nNima qilmohchisiz :......", reply_markup=markup)
    print(patch_employees(user_id, value, 'name'))

def change_surname_rus(message, message_id, lang):
    user_id = message.from_user.id
    value = message.text

    delete__message(user_id, message_id)   
    delete__message(user_id, message.id)


    try:
        directory = os.path.join("media", "cv_photo", str(user_id))
        photo_path = os.path.join(directory, f'{str(user_id)}.jpg')
        image_id = bot.send_photo(message.chat.id, photo=open(photo_path, 'rb'))
        message_id = image_id.message_id
        user = str(user_id)
        image[user] = message_id
    except:
        ...

    if lang == 'ru':
        response = get_employee(user_id)
        text = f'''
    ID : {response[0]['user_id']}
Имя : {response[0]['name']}
Фамилия : {response[0]['surname']}
Телефон номера : +{response[0]['phone_number']}\n\n
            '''
        markup = my_account_rus()
        bot.send_message(user_id, f"{text}\n\nЧто вы хотите сделать :......", reply_markup=markup)
    elif lang == 'uz':
        response = get_employee(user_id)
        text = f'''
    ID : {response[0]['user_id']}
Isim : {response[0]['name']}
Sharif : {response[0]['surname']}
Telefon nomer : +{response[0]['phone_number']}\n\n
        '''
        markup = my_account_uz()
        bot.send_message(user_id, f"{text}\n\nNima qilmohchisiz :......", reply_markup=markup)
    print(patch_employees(user_id, value, 'surname'))




def delete__message(chat_id, message_id):
    bot.delete_message(chat_id, message_id)



print('\n.', '.', '.\n')
bot.polling(none_stop=True)