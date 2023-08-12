from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# STEP 1 (branch selection)
step1_1 = KeyboardButton('📟 Поиск по MAC')
step1_2 = KeyboardButton('🈯 ZKT')
step1_3 = KeyboardButton('✅ Проверка сети')
main_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_kb.add(step1_1, step1_2, step1_3)

# inline keyboard
inline_main_1 = InlineKeyboardButton(text='Посмотреть список обновлений', callback_data='updates')
inline_main_2 = InlineKeyboardButton(text='Список будующих изменений', callback_data='updates')
inline_main = InlineKeyboardMarkup(row_width=1).add(inline_main_1, inline_main_2)
