from aiogram import types, Dispatcher, filters
from keyboards import main_kb, inline_main
from aiogram.dispatcher import FSMContext
import logging


async def start_cmd_handler(message: types.Message, state: FSMContext) -> None:
    try:
        await message.reply("Вас приветствует Экспо-Бот! \n<b>v.1.3 - от 08.08.23</b>",
                            reply_markup=inline_main, parse_mode=types.ParseMode.HTML)
        await message.answer("<b>✅ Выберете действие:</b>",
                             reply_markup=main_kb, parse_mode=types.ParseMode.HTML)
        current_state = await state.get_state()
        if current_state is None:
            return

        logging.info('Cancelling state %r', current_state)
        # Cancel state and inform user about it
        await state.finish()
    except Exception as e:
        await message.reply(f'Походу что-то сломалось\n {e}', reply_markup=main_kb)


def start_bot(dp: Dispatcher):
    dp.register_message_handler(start_cmd_handler, commands=['start', 'help'], state=None)
    dp.register_message_handler(start_cmd_handler, filters.Text(equals='В главное меню', ignore_case=True), state='*')
