from aiogram import types, Dispatcher, filters
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboards import zywall_main, mac_web

# FSM States
class ClientState(StatesGroup):
    IP = State()


async def zywall_ip(message: types.Message, state: FSMContext):
    await message.reply(f"☑️ Утилита для работы с сетевыми устройствами.\n"
                        f"<b>Что умеет?</b>\n"
                        f"🔹 Искать и привязывать <b>MAC адреса</b>\n"
                        f"🔹 Добавлять найденные устройства в <b>Zabbix</b>",
                        reply_markup=mac_web)
    # await state.set_state(ClientState.IP)
    # await message.reply("Укажите IP:", reply_markup=zywall_main)


# async def zywall_mac(message: types.Message):
#     await message.reply("", reply_markup=zywall_main)
#     await message.reply("""
#             <b> Ваш IP Zywall </b>
#             """)
#     await message.reply(
#         f'Введите <b>4</> последние буквы или <b>полный</b>'
#         f'MAC в формате: <b>1Х:ЕР</b>', )


# # @dp.message_handler(commands=['start', 'help'])
# async def zywall_ip(message: types.Message, state=ZywallInfo.zywal):
#     try:
#
#         if not ip.isdigit():
#             msg = bot.reply_to(message, 'Не верный формат. Укажите IP без точки.')
#             bot.register_next_step_handler(msg, zyxel_step1_add_ip)
#             return
#         elif not ip.isdigit() and not len(ip) <= 6:
#             msg = bot.reply_to(message, 'Не верный формат. IP состоит из не более 4 чисел.\nПример: 120.1')
#             bot.register_next_step_handler(msg, zyxel_step1_add_ip)
#             return
#         format_ip = message.text
#         bot.reply_to(message, """\
#                     <b> Ваш IP Zywall </b>
#                     """, parse_mode='html')
#         bot.send_message(message.chat.id,
#                          f'Введите <b>4</> последние буквы или <b>полный</b> MAC в формате: <b>1Х:ЕР</b>',
#                          parse_mode='html')
#         bot.register_next_step_handler(message, zyxel_step2_input_mac)
#     except Exception as e:
#         print(e)
#         bot.reply_to(message, 'Упс! Бот сломался начните с начала. Напишите команду /start')


def register_handler_zywall(dp: Dispatcher):
    dp.register_message_handler(zywall_ip, filters.Text(equals='📟 Поиск по MAC'))