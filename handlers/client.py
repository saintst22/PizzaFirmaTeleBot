from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботов через личне сообщения, напишите ему:\nhttps://t.me/pizzafirmabot')


@dp.message_handler(commands=['Режим_работы'])
async def command_pizza_open(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')


@dp.message_handler(commands=['Адрес'])
async def command_pizza_place(message: types.Message):
    await bot.send_message(message.from_user.id, 'Москва, ул. Новый Арбат, д. 23')


@dp.message_handler(commands=['Меню'])
async def command_pizza_menu(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_pizza_open, commands=['Режим_работы'])
    dp.register_message_handler(command_pizza_place, commands=['Адрес'])
    dp.register_message_handler(command_pizza_menu, commands=['Меню'])
