from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_1 = KeyboardButton('/Режим_работы')
button_2 = KeyboardButton('/Адрес')
button_3 = KeyboardButton('/Меню')
button_4 = KeyboardButton('/Поделиться номером телефона', request_contact=True)
button_5 = KeyboardButton('/Поделиться геопозицией', request_location=True)


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.row(button_1, button_2, button_3, button_4, button_5)