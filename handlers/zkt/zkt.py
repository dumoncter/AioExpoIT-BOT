import asyncio
from datetime import datetime
from aiogram import types, Dispatcher, filters
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboards import zkt_main, zkt_event_vf, zkt_event_vf_id_close, main_kb
from .zkt_sql_inject import sql_inject
import json


# FSM States
class ClientState(StatesGroup):
    INJECT_MAIN = State()


async def main_zkt(message: types.Message) -> None:
    await message.reply("Выберете функцию", reply_markup=zkt_main)


async def event_verification(message: types.Message) -> None:
    await message.reply("<b>Для работы необходимо узнать требуемый ID сканера.</b>\n"
                        "Найдите требуемый из списка.\n"
                        "<u>Если ID уже известен, переходите <b>далее - 'Отметить'</b></u>",
                        reply_markup=zkt_event_vf)


async def search_zkt_id(message: types.Message) -> None:
    await message.answer(open_file())
    await message.answer("❗ <u><b>Повторное использование через минуту</b></u>", reply_markup=zkt_event_vf_id_close)


def open_file():
    with open("zkt_ip.json", 'r', encoding='utf-8') as f:
        contents = json.load(f)
        new_line = '\n'
        id_list = []
        for i in range(len(contents)):
            id_list.append('ID: ' + '<b>' + str(contents[i]['ID']) + '</b>' + ' = ' + contents[i]['Name'])
        return new_line.join(list(map(str, id_list)))


async def notice(message: types.Message, state: FSMContext):
    await message.reply("✅ Укажите, через пробел: \n"
                        "<b>1 - ID сканера</b> и 2 - <b>ID учетной записи</b> на котором проводится проверка. \n"
                        "Пример: "
                        "<b>930 57</b>", reply_markup=zkt_event_vf_id_close)
    await state.set_state(ClientState.INJECT_MAIN)


async def func_inject(message: types.Message, state: FSMContext):
    user_msg = message.text
    formated = user_msg.split()
    await state.update_data(INJECT_MAIN=user_msg)
    if user_msg.isalpha():
        await message.reply('⛔ Сообщение не может содержать буквы .\n')
    elif len(formated) >= 3:
        await message.reply('⛔ Сообщение не может содержать более двух аргументов .\n'
                            'Пример: ID учетной записи: <b>1450</b>, ID сканера: <b>48</b>\n'
                            '<b><u>1450 48</u></b>')
    elif len(message.text) > 8:
        await message.reply('⛔ Не корректный ввод.\n'
                            'ID учетной записи может содержать <b>более 9999</b> номеров\n'
                            'ID сканера не более <b>999</b>\n'
                            'Пример: ID учетной записи: <b>1450</b>, ID сканера: <b>48</b>\n'
                            '<b><u>1450 48</u></b>')
    elif not user_msg:
        await message.reply('Сообщение не может быть пустым')
    else:
        newline = '\n'
        inject = asyncio.create_task(sql_inject(formated[0], formated[1]))
        await inject
        await message.answer(f'✅ <b>{datetime.now().strftime("%m/%d/%Y %H:%M:%S")}'
                             f' запроc выполнен успешно!</b>{newline}'
                             f'<b>ID сканера: <u>{formated[0]}{newline}</u></b>'
                             f'Установлен <b>ID пользователя: <u>{formated[1]}</u></b>',
                             reply_markup=main_kb)
        await state.finish()


def register_handler_zkt(dp: Dispatcher):
    dp.register_message_handler(main_zkt, filters.Text(equals='🈯 ZKT'))
    dp.register_message_handler(event_verification, filters.Text(equals='Проверка события'))
    dp.register_message_handler(search_zkt_id, filters.Text(equals='Показать список ID'))
    dp.register_message_handler(notice, filters.Text(equals='Отметить'))
    dp.register_message_handler(func_inject, state=ClientState.INJECT_MAIN)
