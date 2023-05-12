from aiogram import types, Dispatcher
import json, string
from create_bot import dp


@dp.message_handler()
async def echo_send(message: types.Message):
    if {i_word.lower().translate(str.maketrans('', '', string.punctuation)) for i_word in
        message.text.split(' ')}.intersection(set(json.load(open('censorship.json')))) != set():
        await message.reply('Ругаться матом нельзя!')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)

