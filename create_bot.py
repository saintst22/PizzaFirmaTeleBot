from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot('6158555565:AAFPAxTm5zyM8d-nv9KrMfDKakaaoVh58BI')
dp = Dispatcher(bot, storage=storage)
