import time

from aiogram import types, Dispatcher, filters
from keyboards import main_kb, inline_main
from aiogram.dispatcher import FSMContext
from create_bot import bot, storage, dp
import subprocess
import sys
import os
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


async def restart_bot(message: types.Message):
    await message.reply(f'Выполняется перезагрузка БОТА\n')
    # Закрытие текущего соединения с ботом
    dp.stop_polling()
    # Выполнение необходимых операций по перезагрузке
    subprocess.call([sys.executable, os.path.join(os.getcwd(), __file__)])
    # Запуск бота заново
    await dp.start_polling()

# async def restart_bot(message: types.Message):
#     await message.reply(f'Выполняется перезагрузка БОТА\n')
#     await bot.send_message(message.chat.id, 'Перезагрузка...')
#     await bot.close()
#     await main.close()
#     await storage.close()
#     await storage.wait_closed()
#     await bot.delete_webhook()
#     await bot.skip_updates()
#     await dp.reset()


def start_bot(dp: Dispatcher):
    dp.register_message_handler(start_cmd_handler, commands=['start', 'help'], state=None)
    dp.register_message_handler(restart_bot, filters.Text(equals='Рестарт'))
    dp.register_message_handler(start_cmd_handler, filters.Text(equals='В главное меню', ignore_case=True), state='*')
