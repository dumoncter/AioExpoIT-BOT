from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# netttols main kb
net_tols_main_btn_1 = KeyboardButton('PING')
net_tols_main_btn_2 = KeyboardButton('В разработке')
net_tols_main_btn_3 = KeyboardButton('В главное меню')

net_tols_main = ReplyKeyboardMarkup(resize_keyboard=True)
net_tols_main.add(net_tols_main_btn_1, net_tols_main_btn_2)

# ping kb
net_tols_ping_btn1 = KeyboardButton('Повторить')
net_tols_ping_btn2 = KeyboardButton('В главное меню')
net_tols_ping_btn3 = KeyboardButton('Изменить размер пакета')
net_tols_ping_btn4 = KeyboardButton('Установить количество пакетов')
net_tols_ping_btn5 = KeyboardButton('Проверка MTU (Опр. макс. пакета)')
net_tols_ping_btn6 = KeyboardButton('Расширенная версия')

net_tols_ping = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
net_tols_ping.add(net_tols_ping_btn2)

net_tols_ping_info = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
net_tols_ping_info.add(net_tols_ping_btn2)