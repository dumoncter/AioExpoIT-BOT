from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

# MAIN (specify ip)
zywall_step1_1 = KeyboardButton('Добавить')
zywall_step1_2 = KeyboardButton('Продлить поиск')
zywall_main = ReplyKeyboardMarkup(resize_keyboard=True)
zywall_main.add(zywall_step1_1, zywall_step1_2)


mac_web_1 = KeyboardButton('Запустить утилиту', web_app = WebAppInfo(url = 'https://dumoncter.github.io/expo-bot/'))
mac_web_2 = KeyboardButton('ТЕСТ 1', web_app = WebAppInfo(url = 'https://dumoncter.github.io/test_html/'))
mac_web_3 = KeyboardButton('ТЕСТ 2', web_app = WebAppInfo(url = 'https://dumoncter.github.io/test2/'))
mac_web_4 = KeyboardButton('В главное меню')
mac_web = ReplyKeyboardMarkup(resize_keyboard=True)
mac_web.add(mac_web_1, mac_web_2, mac_web_3, mac_web_4)