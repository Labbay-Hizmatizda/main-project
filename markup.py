from telebot import types

# employer--------------------------------------------------------------------------------------------------

def russian():
    markup = types.InlineKeyboardMarkup()

    about_us = types.InlineKeyboardButton('О нас', callback_data='about_us_rus')
    my_account = types.InlineKeyboardButton('Мои Данные', callback_data='my_account_rus')
    orders = types.InlineKeyboardButton('Заказы', callback_data='orders_rus')

    markup.add(about_us, my_account, orders)
    return markup


def my_account_rus():
    markup = types.InlineKeyboardMarkup()

    change_phone_number = types.InlineKeyboardButton('Изменить номер', callback_data='change_phone_num_rus')
    change_name_surname = types.InlineKeyboardButton('Изменить номер', callback_data='change_name_surname_rus')
    change_language = types.InlineKeyboardButton('Изменить язык', callback_data='change_language_rus')
    change_cv = types.InlineKeyboardButton('Изменить резюме', callback_data='change_cv_rus')
    back = types.InlineKeyboardButton('◀ Назад', callback_data='back')
    markup.add(change_name_surname, change_phone_number, change_cv, change_language, back)
    return markup

def change_phone_num_rus():
    ...


def orders_rus():
    markup = types.InlineKeyboardMarkup()

    active_orders = types.InlineKeyboardButton('Активные заказы', callback_data='active_orders')
    new_order = types.InlineKeyboardButton('Создать новый заказ', callback_data='new_order')
    back = types.InlineKeyboardButton('◀ Назад', callback_data='back')
    markup.add(active_orders, new_order, back)

    return markup

def active_orders_rus():
    markup = types.InlineKeyboardMarkup()

    back = types.InlineKeyboardButton('◀ Назад', callback_data='back_orders')
    markup.add(back)

    return markup

def new_order():
    ...



# uzbek lang-------------------------------------------------------------------------------

def uzbek():
    markup = types.InlineKeyboardMarkup()

    about_us = types.InlineKeyboardButton('Biz Haqimizda', callback_data='about_us_uz')
    my_account = types.InlineKeyboardButton('Mening danniylarim', callback_data='my_account_uz')
    orders = types.InlineKeyboardButton('Buyurtlamarim', callback_data='orders_uz')

    markup.add(about_us, my_account, orders)
    return markup

def my_account_uz():
    markup = types.InlineKeyboardMarkup()

    change_phone_number = types.InlineKeyboardButton('Nomerni o\'zgartirish', callback_data='change_phone_num_uz')
    back = types.InlineKeyboardButton('◀ Orqaga', callback_data='back_uz')
    markup.add(change_phone_number, back)
    return markup

def change_number_uz():
    ...


def orders_uz():
    markup = types.InlineKeyboardMarkup()

    active_orders = types.InlineKeyboardButton('Faol buyurtmalar', callback_data='active_orders_uz')
    new_order = types.InlineKeyboardButton('Yangi buyurtma yaratish', callback_data='new_order_uz')
    back = types.InlineKeyboardButton('◀ Orqaga', callback_data='back_uz')
    markup.add(active_orders, new_order, back)

    return markup

def active_orders_uz():
    markup = types.InlineKeyboardMarkup()

    back = types.InlineKeyboardButton('◀ Orqaga', callback_data='back_orders_uz')
    markup.add(back)

    return markup

def new_order_uz():
    ...




# employee-------------------------------------------------------------------------------



# def russian_employee():
#     markup = types.InlineKeyboardMarkup()

#     about_us = types.InlineKeyboardButton('О нас', callback_data='about_us_rus')
#     my_account = types.InlineKeyboardButton('Мои Данные', callback_data='my_account_rus')
#     orders = types.InlineKeyboardButton('Заявки', callback_data='orders_rus')

#     markup.add(about_us, my_account, orders)
#     return markup

# def proposals_rus_employee():
#     markup = types.InlineKeyboardMarkup()

#     active_orders = types.InlineKeyboardButton('Активные Заявки', callback_data='active_orders')
#     new_order = types.InlineKeyboardButton('Создать новый Заявку', callback_data='new_order')
#     back = types.InlineKeyboardButton('◀ Назад', callback_data='back')
#     markup.add(active_orders, new_order, back)

#     return markup

# def active_orders_rus_employee():
#     markup = types.InlineKeyboardMarkup()

#     back = types.InlineKeyboardButton('◀ Назад', callback_data='back_orders_employee')
#     markup.add(back)

#     return markup


# def uzbek_employee():
#     markup = types.InlineKeyboardMarkup()

#     about_us = types.InlineKeyboardButton('Biz Haqimizda', callback_data='about_us_uz')
#     my_account = types.InlineKeyboardButton('Mening danniylarim', callback_data='my_info_uz')
#     orders = types.InlineKeyboardButton('Buyurtlamarim', callback_data='orders_uz')

#     markup.add(about_us, my_account, orders)
#     return markup
