import ipaddress
from aiogram import types, Dispatcher, filters
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from pythonping import ping
from keyboards import net_tols_main, net_tols_ping, net_tols_ping_info


class ClientState(StatesGroup):
    PING = State()


async def main_nettols(message: types.Message):
    await message.reply("Выберете функцию:", reply_markup=net_tols_main)


async def icmp_ping(message: types.Message, state: FSMContext):
    await message.reply("Утилита для работы с <b>ICMP</b>. Укажите IP без приставки <b>192.168</b>\n"
                        "Пример: <b>20.1</b>\n"
                        "",
                        reply_markup=net_tols_ping, parse_mode=types.ParseMode.HTML)
    await state.set_state(ClientState.PING)


async def run_ping(message: types.Message, state: FSMContext):
    user_msg = message.text
    reduced = user_msg.split('.')
    line = '-' * 55
    first_ip = '192.168'
    if len(reduced) == 2 and len(reduced[0]) <= 3 and len(reduced[1]) <= 3:
        if reduced[0].isdigit() and reduced[1].isdigit():
            await message.reply("<b>🔥 Запрос обрабатывается</b>")
            await message.reply(f'<b>Ваш адрес: {first_ip + "." + reduced[0] + "." + reduced[1]}\n'
                                f'{line}\n'
                                f'{ping(first_ip + "." + reduced[0] + "." + reduced[1], count=5)}</b>',
                                reply_markup=net_tols_ping_info)
            await message.answer(f'⚠️ Если требуется проверить другой адрес, <b>то в этом окне укажите <u>новый ip адрес.</u>\n</b>'
                                 f'Для завершения работы нажмите - <b><u>В главное меню</u></b>')
            # await state.finish()
        else:
            await message.reply("❌ <b>Адрес указан не корректно, повторите снова</b>")

    elif len(reduced) == 4:
        try:
            ip = ipaddress.ip_address(user_msg)
            await message.reply(f'<b>Ваш адрес: {first_ip + "." + reduced[0] + "." + reduced[1]}\n'
                                f'{line}\n'
                                f'{ping(user_msg, count=5)}</b>',
                                reply_markup=net_tols_ping_info)
            await message.answer(f'⚠️ Если требуется проверить другой адрес, <b>то в этом окне укажите новый ip адрес.</b>'
                                 f'Для завершения работы нажмите <b>В главное меню</b>')
            # await state.finish()
        except ValueError:
            await message.reply("❌ <b>Адрес указан не корректно, повторите снова</b>")
    else:
        await message.reply("❌ <b>Адрес указан не корректно, повторите снова</b>")


async def extended_ping(message: types.Message):
    await message.reply("Находится в разработке", reply_markup=net_tols_main)


def register_handler_net_tols(dp: Dispatcher):
    dp.register_message_handler(main_nettols, filters.Text(equals='✅ Проверка сети'))
    dp.register_message_handler(icmp_ping, filters.Text(equals='PING'))
    dp.register_message_handler(icmp_ping, filters.Text(equals='Расширенная версия'))
    # dp.register_message_handler(run_ping, filters.Text(equals='Повторить'))
    dp.register_message_handler(run_ping, state=ClientState.PING)