import asyncio
from aiogram import executor, Dispatcher
from create_bot import dp
from handlers import zywall, start_bot, zkt, nettols_main, zkt_sql_list

# all registered handlers:
start_bot.start_bot(dp)
zywall.register_handler_zywall(dp)
zkt.register_handler_zkt(dp)
nettols_main.register_handler_nettols(dp)


async def on_startup_launch(dp: Dispatcher):
    asyncio.create_task(zkt_sql_list.sql_export())

if __name__ == '__main__':
    on_startup = on_startup_launch
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup_launch)
