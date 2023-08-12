import logging
from aiogram import Bot, Dispatcher, types
import os
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv()
storage = MemoryStorage()
API_TOKEN = os.getenv('TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Initialize bot with os and dispatcher
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)