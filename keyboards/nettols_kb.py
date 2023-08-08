from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# netttols main kb
netttols_main_btn_1 = KeyboardButton('PING')
netttols_main_btn_2 = KeyboardButton('В разработке')

netttols_main = ReplyKeyboardMarkup(resize_keyboard=True)
netttols_main.add(netttols_main_btn_1, netttols_main_btn_2)

# ping kb
netttols_ping_btn1 = KeyboardButton('Повторить')
netttols_ping_btn2 = KeyboardButton('В главное меню')
netttols_ping_btn3 = KeyboardButton('Изменить размер пакета')
netttols_ping_btn4 = KeyboardButton('Установить количество пакетов')
netttols_ping_btn5 = KeyboardButton('Проверка MTU (Опр. макс. пакета)')
netttols_ping_btn6 = KeyboardButton('Расширенная версия')

netttols_ping = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
netttols_ping.add(netttols_ping_btn2)

netttols_ping_info = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
netttols_ping_info.add(netttols_ping_btn2)