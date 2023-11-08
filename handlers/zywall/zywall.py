import asyncio
import transliterate.exceptions
from transliterate import translit
from aiogram import types, Dispatcher, filters
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import subprocess
from keyboards import mac_web
import json


# FSM States
class ClientState(StatesGroup):
    IP = State()


async def zywall_ip(message: types.Message):
    await message.reply(f"☑️ Утилита для работы с сетевыми устройствами.\n"
                        f"<b>Что умеет?</b>\n"
                        f"🔹 Искать и привязывать <b>MAC адреса</b>\n"
                        f"🔹 Добавлять найденные устройства в <b>Zabbix</b>",
                        reply_markup=mac_web)


async def web_appdata(message: types.Message):
    web_app = message.web_app_data.data
    data = json.loads(web_app)
    name = data['name']
    ip = data['ip']
    ip_zywall = data['zywall_ip']
    mac = data['mac']
    tags_1 = data['tags']['city']
    tags_2 = data['tags']['data_tags']
    zkt_name = data['zkt_name']
    descript = f'{zkt_name} - {name}'
    # request_interval = data['request_interval']
    latin_name = str(translate(name))
    if tags_1 != '':
        await message.answer(f'''
<b>💬 Вы указали данные:</b>
<b>➖ Zywall: {ip_zywall}</b>
<b>➖ Имя: <u>{name}</u> </b>
<b>➖ IP адрес: <u>{ip}</u> </b>
<b>➖ Mac адрес: <u>{mac}</u> </b>
<b>🔸 Тег 1: <u>{tags_1}</u> </b>
<b>🔹 Тег 2: <u>{tags_2}</u> </b>
                             ''')
        await message.answer('⚠️ Выполняется обработка. Ожидайте выполнения.')
        await message.answer(f'{await add_to_zabbix_and_zywall(ip, ip_zywall, name, tags_1, tags_2, latin_name, mac, request_interval, descript)}')


async def add_to_zabbix_and_zywall(ip, ip_zywall, name, tags_1, tags_2, latin_name, mac, request_interval, descript):
    global zkt_result
    zabbix_cmd = ['python', 'handlers/zywall/zabbix_api.py', str(ip), name, tags_1, str(tags_2)]
    zywall_cmd = ['python', 'handlers/zywall/zywall_ssh.py', str(ip), ip_zywall, latin_name, mac]
    if request_interval == "5min" or request_interval == 'realtime':
        zkt_cmd = ['python', 'handlers/zywall/zkt_add_device.py', str(descript), ip, latin_name, request_interval]
        zkt_process = await asyncio.create_subprocess_exec(*zkt_cmd, stdout=subprocess.PIPE)
        zkt_output = await zkt_process.stdout.read()
        zkt_result = zkt_output.decode()

    # Запуск процессов и ожидание их завершения
    zabbix_process = await asyncio.create_subprocess_exec(*zabbix_cmd, stdout=subprocess.PIPE)
    zywall_process = await asyncio.create_subprocess_exec(*zywall_cmd, stdout=subprocess.PIPE)


    # Получение вывода от процессов
    zabbix_output = await zabbix_process.stdout.read()
    zywall_output = await zywall_process.stdout.read()

    reply_message = zabbix_output.decode() + '\n' + zywall_output.decode() + '\n' + zkt_result
    return reply_message


def translate(name):
    try:
        form_name = translit(name, reversed=True)
        return form_name
    except transliterate.exceptions.LanguageDetectionError as err:
        return name


def register_handler_zywall(dp: Dispatcher):
    dp.register_message_handler(zywall_ip, filters.Text(equals='📟 Поиск по MAC'))
    dp.register_message_handler(web_appdata, content_types='web_app_data')
