import asyncio
from aiogram import executor, Dispatcher
from create_bot import dp
from handlers import zywall, start_bot, zkt, net_tols_main, zkt_sql_list

# all registered handlers:
start_bot.start_bot(dp)
zywall.register_handler_zywall(dp)
zkt.register_handler_zkt(dp)
net_tols_main.register_handler_net_tols(dp)


async def on_startup_launch(dp):
    asyncio.create_task(zkt_sql_list.sql_export())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    on_startup = on_startup_launch
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup_launch)
    loop.create_task(dp.start_polling())
    loop.run_forever()

