import pyodbc
from datetime import datetime
from sys import platform
import os
from dotenv import load_dotenv
load_dotenv()


driver = 'DRIVER={ODBC Driver 17 for SQL Server}'
if platform == "linux" or platform == "linux2":
    driver = 'DRIVER={ODBC Driver 17 for SQL Server}'
elif platform == "win32":
    driver = 'DRIVER={SQL Server}'

server = 'SERVER=192.168.201.40'
port = os.getenv('PORT')
db = os.getenv('DB')
user = os.getenv('USER_DB')
pw = os.getenv('PW_DB')
conn_str = ';'.join([driver, server, port, db, user, pw])

conn = pyodbc.connect(conn_str)
conn.timeout = 60
cursor = conn.cursor()


async def sql_inject(id_zkt, id_user) -> None:
    try:
        cursor.execute('''
            INSERT INTO "dbo"."EXP_Events"
            VALUES (?, ?, ?, ?) ''', (id_zkt, datetime.now(), id_user, 0))
        conn.commit()
        print(f'{datetime.now().strftime("%m/%d/%Y %H:%M:%S")} Запрос ID = {id_zkt}, User = {id_user} выполнен успешно!')
    except pyodbc.Error as err:
        print(datetime.now().strftime("%m/%d/%Y %H:%M:%S"), 'Error', err)
    # finally:
    #     cursor.close()
    #     conn.close()