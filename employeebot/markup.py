from telebot import types


# employer rus--------------------------------------------------------------------------------------------------

def russian():
    markup = types.InlineKeyboardMarkup(row_width=1)

    about_us = types.InlineKeyboardButton('О нас ℹ️ ', callback_data='about_us_rus')
    my_account = types.InlineKeyboardButton('Мои Данные 💾', callback_data='my_account_rus')
    orders = types.InlineKeyboardButton('Отлики 📜', callback_data='proposals_rus')

    markup.add(about_us, my_account, orders)
    return markup

def back_about_us():
    markup = types.InlineKeyboardMarkup()

    back = types.InlineKeyboardButton('Назад ◀️', callback_data='about_us_back_menu')
    markup.add(back)

    return markup

def my_account_rus():
    markup = types.InlineKeyboardMarkup(row_width=1)

    change_photo = types.InlineKeyboardButton('Изменить фото 🖼', callback_data='change_photo')
    change_phone_number = types.InlineKeyboardButton('Изменить номер ☎️', callback_data='change_phonenumber_rus')
    change_name = types.InlineKeyboardButton('Изменить имя 👤', callback_data='change_name_rus')
    change_surname = types.InlineKeyboardButton('Изменить фамилию 👤', callback_data='change_surname_rus')
    change_language = types.InlineKeyboardButton('Изменить язык 🌍', callback_data='change_language_rus')
    back = types.InlineKeyboardButton('Назад ◀️', callback_data='back_to_main_menu_rus')
    markup.add(change_photo, change_name, change_surname, change_phone_number, change_language, back)
    return markup

def change_lang___rus():
    markup = types.InlineKeyboardMarkup(row_width=1)
    lang_rus = types.InlineKeyboardButton('Русский 🇷🇺 ', callback_data='identify_lang_rus')
    lang_uz = types.InlineKeyboardButton('O\'zbek tili 🇺🇿 ', callback_data='identify_lang_uz')
    back = types.InlineKeyboardButton('Отменить ❌', callback_data='cancel_rus')
    
    markup.add(lang_rus, lang_uz, back)
    return markup

def cancel_ru():
    markup = types.InlineKeyboardMarkup(row_width=1)
    cancel = types.InlineKeyboardButton('Отменить ❌', callback_data='cancel_rus')
    markup.add(cancel)

    return markup

def proposals_rus():
    markup = types.InlineKeyboardMarkup(row_width=1)

    active_orders = types.InlineKeyboardButton('Отклики в ожидании 📬', callback_data='pending_proposals')
    proposals_history = types.InlineKeyboardButton('История откликов 🗄', callback_data='proposals_history')
    new_order = types.InlineKeyboardButton('Откликнуться на заказ 📤', callback_data='new_proposal')
    back = types.InlineKeyboardButton('Назад ◀️', callback_data='about_us_back_menu')
    markup.add(active_orders, new_order, proposals_history, back)

    return markup

def pending_proposals_rus():
    markup = types.InlineKeyboardMarkup()

    back = types.InlineKeyboardButton('Назад ◀️', callback_data='back_proposals')
    markup.add(back)

    return markup



# employer uzbek-------------------------------------------------------------------------------

def uzbek():
    markup = types.InlineKeyboardMarkup(row_width=1)

    about_us = types.InlineKeyboardButton('Biza Haqqimizda ℹ️ ', callback_data='about_us_uz')
    my_account = types.InlineKeyboardButton('Mening tafsilotlarim 💾', callback_data='my_account_uz')
    orders = types.InlineKeyboardButton('Arizalar 📜', callback_data='proposals_uz')

    markup.add(about_us, my_account, orders)
    return markup

def back_about_us_uz():
    markup = types.InlineKeyboardMarkup()

    back = types.InlineKeyboardButton('Orqaga ◀️', callback_data='about_us_back_menu_uz')
    markup.add(back)

    return markup

def my_account_uz():
    markup = types.InlineKeyboardMarkup(row_width=1)

    change_photo = types.InlineKeyboardButton('Rasimni o\'zgartirish 🖼', callback_data='change_photo_uz')
    change_phone_number = types.InlineKeyboardButton('Nomerni o\'zgartirish ☎️', callback_data='change_phonenumber_uz')
    change_name = types.InlineKeyboardButton('Isimni o\'zgartirish 👤', callback_data='change_name_uz')
    change_surname = types.InlineKeyboardButton('Sharifni o\'zgartirish 👤', callback_data='change_surname_uz')
    change_language = types.InlineKeyboardButton('Tilni o\'zgartirish 🌍', callback_data='change_language_uz')
    back = types.InlineKeyboardButton('Orqaga ◀️', callback_data='back_to_main_menu_uz')
    markup.add(change_photo, change_name, change_surname, change_phone_number, change_language, back)
    return markup

def change_lang___uz():
    markup = types.InlineKeyboardMarkup(row_width=1)
    lang_rus = types.InlineKeyboardButton('Русский 🇷🇺 ', callback_data='identify_lang_rus')
    lang_uz = types.InlineKeyboardButton('O\'zbek tili 🇺🇿 ', callback_data='identify_lang_uz')
    back = types.InlineKeyboardButton('Bekor qilish ❌', callback_data='cancel_uz')
    
    markup.add(lang_rus, lang_uz, back)
    return markup

def cancel_uz():
    markup = types.InlineKeyboardMarkup(row_width=1)
    cancel = types.InlineKeyboardButton('Bekor qilish ❌', callback_data='cancel_uz')
    markup.add(cancel)

    return markup

def proposals_uz():
    markup = types.InlineKeyboardMarkup(row_width=1)

    active_orders = types.InlineKeyboardButton('Mening Takliflarim 📬', callback_data='pending_proposals_uz')
    proposals_history = types.InlineKeyboardButton('Takliflar tarixi🗄', callback_data='proposals_history_uz')
    new_order = types.InlineKeyboardButton('Taklif qoldirish 📤', callback_data='new_proposal_uz')
    back = types.InlineKeyboardButton('Orqaga ◀️', callback_data='about_us_back_menu_uz')
    markup.add(active_orders, new_order, proposals_history, back)

    return markup

def pending_proposals_uz():
    markup = types.InlineKeyboardMarkup()

    back = types.InlineKeyboardButton('Orqaga ◀️', callback_data='back_proposals_uz')
    markup.add(back)

    return markup
