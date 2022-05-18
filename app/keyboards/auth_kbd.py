from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def welcome_kbd():
    button_hi = InlineKeyboardButton(text="я друг и хочу себе vpn!", callback_data='want_vpn')
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button_hi)
    return keyboard


def choice_auth_method():
    button_inst = InlineKeyboardButton(text="по профилю инсты", callback_data='auth_inst')
    button_vk = InlineKeyboardButton(text="по вк", callback_data='auth_vk')
    button_phone_number = InlineKeyboardButton(text="по телефонному номеру", callback_data='auth_ph_nmb')
    button_token = InlineKeyboardButton(text="по токену", callback_data='auth_token')
    button_request_access = InlineKeyboardButton(text="запросить доступ у админа (долго)",
                                                 callback_data='auth_request_access')
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button_token, button_vk)
    keyboard.add(button_inst, button_phone_number)
    keyboard.add(button_request_access)
    return keyboard
