from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


zkt_main_btn_1 = KeyboardButton('Проверка события')
zkt_main_btn_2 = KeyboardButton('Пока не известно')
zkt_main = ReplyKeyboardMarkup(resize_keyboard=True)
zkt_main.add(zkt_main_btn_1, zkt_main_btn_2)

# event verification
zkt_event_vf_btn1 = KeyboardButton('Вернуться выше')
zkt_event_vf_btn2 = KeyboardButton('Показать список ID')
zkt_event_vf_btn3 = KeyboardButton('Отметить')
zkt_event_vf_btn4 = KeyboardButton('В главное меню')

zkt_event_vf = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
zkt_event_vf.add(zkt_event_vf_btn3, zkt_event_vf_btn2, zkt_event_vf_btn1)

# sql list
zkt_event_vf_id_close = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
zkt_event_vf_id_close.add(zkt_event_vf_btn3, zkt_event_vf_btn1, zkt_event_vf_btn4)
