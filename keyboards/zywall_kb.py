from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# MAIN (specify ip)
zywall_step1_1 = KeyboardButton('Добавить')
zywall_step1_2 = KeyboardButton('Продлить поиск')
zywall_main = ReplyKeyboardMarkup(resize_keyboard=True)
zywall_main.add(zywall_step1_1, zywall_step1_2)
