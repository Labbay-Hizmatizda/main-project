import os 
from markup import *
from employee_bot_api import *
from api_integration import *



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
    bot.send_message(user_id, f"{text}", reply_markup=markup)


def delete__message(chat_id, message_id):
    bot.delete_message(chat_id, message_id)