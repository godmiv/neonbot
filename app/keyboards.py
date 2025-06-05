from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Забанить"),KeyboardButton(text="Разбанить")],
    [KeyboardButton(text="Расписание")]
],one_time_keyboard=True)

menu1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Кнопка 1"), KeyboardButton(text="Кнопка 2")],
    [KeyboardButton(text="Кнопка 3"), KeyboardButton(text="Кнопка 4")],
    [KeyboardButton(text="Кнопка 5"), KeyboardButton(text="Кнопка 6")],
])

