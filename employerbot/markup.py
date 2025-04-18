from telebot import types


# employer rus--------------------------------------------------------------------------------------------------

def russian():
    markup = types.InlineKeyboardMarkup(row_width=1)

    about_us = types.InlineKeyboardButton('О нас', callback_data='about_us_rus')
    my_account = types.InlineKeyboardButton('Мои Данные', callback_data='my_account_rus')
    orders = types.InlineKeyboardButton('Заказы', callback_data='orders_rus')

    markup.add(about_us, my_account, orders)
    return markup


def my_account_rus():
    markup = types.InlineKeyboardMarkup(row_width=1)

    change_phone_number = types.InlineKeyboardButton('Изменить номер', callback_data='change_phone_num_rus')
    change_name_surname = types.InlineKeyboardButton('Изменить имя фамилию', callback_data='change_name_surname_rus')
    change_language = types.InlineKeyboardButton('Изменить язык', callback_data='change_language_rus')
    change_cv = types.InlineKeyboardButton('Изменить резюме', callback_data='change_cv_rus')
    back = types.InlineKeyboardButton('◀ Назад', callback_data='back_to_main_menu_rus')
    markup.add(change_name_surname, change_phone_number, change_cv, change_language, back)
    return markup

def change_cv_info_rus():
    markup = types.InlineKeyboardMarkup(row_width=1)
    change_image = types.InlineKeyboardButton('Изменить Фото', callback_data='change_phone_num_rus')
    change_bio = types.InlineKeyboardButton('Изменить биографию', callback_data='change_name_surname_rus')
    markup.add(change_image, change_bio)

def change_phone_num_rus():
    ...

def boolean_proposal_rus():
    markup = types.InlineKeyboardMarkup(row_width=1)
    yes = types.InlineKeyboardButton('Да', callback_data='yes_proposal')
    no = types.InlineKeyboardButton('Нет', callback_data='no_proposal')
    markup.add(yes, no)

def orders_rus():
    markup = types.InlineKeyboardMarkup(row_width=1)

    active_orders = types.InlineKeyboardButton('Активные заказы', callback_data='active_orders')
    orders_history = types.InlineKeyboardButton('История заказов', callback_data='history_orders')
    new_order = types.InlineKeyboardButton('Создать новый заказ', callback_data='new_order')
    back = types.InlineKeyboardButton('◀ Назад', callback_data='back_to_main_menu_rus')
    markup.add(active_orders, new_order, orders_history, back)

    return markup


def active_orders_rus():
    markup = types.InlineKeyboardMarkup()

    back = types.InlineKeyboardButton('◀ Назад', callback_data='back_orders')
    markup.add(back)

    return markup


def new_order():
    ...


# employer uzbek-------------------------------------------------------------------------------

def uzbek():
    markup = types.InlineKeyboardMarkup(row_width=1)

    about_us = types.InlineKeyboardButton('Biz Haqimizda', callback_data='about_us_uz')
    my_account = types.InlineKeyboardButton('Mening danniylarim', callback_data='my_account_uz')
    orders = types.InlineKeyboardButton('Buyurtlamarim', callback_data='orders_uz')

    markup.add(about_us, my_account, orders)
    return markup


def my_account_uz():
    markup = types.InlineKeyboardMarkup(row_width=1)

    change_phone_number = types.InlineKeyboardButton('Nomerni o\'zgartirish', callback_data='change_phone_num_uz')
    back = types.InlineKeyboardButton('◀ Orqaga', callback_data='back_uz')
    markup.add(change_phone_number, back)
    return markup


def change_number_uz():
    ...


def orders_uz():
    markup = types.InlineKeyboardMarkup(row_width=1)

    active_orders = types.InlineKeyboardButton('Faol buyurtmalar', callback_data='active_orders_uz')
    new_order = types.InlineKeyboardButton('Yangi buyurtma yaratish', callback_data='new_order_uz')
    back = types.InlineKeyboardButton('◀ Orqaga', callback_data='back_uz')
    markup.add(active_orders, new_order, back)

    return markup


def active_orders_uz():
    markup = types.InlineKeyboardMarkup(row_width=1)

    back = types.InlineKeyboardButton('◀ Orqaga', callback_data='back_orders_uz')
    markup.add(back)

    return markup


def new_order_uz():
    ...
