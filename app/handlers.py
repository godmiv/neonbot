from aiogram import F, Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("Привет!!!", reply_markup=kb.menu)

@router.message(Command("info"))
async def cmd_info(message: Message):
    await message.answer(f"ID этого чата: {message.chat.id}\nТип чата: {message.chat.type}")



"""
Здесь нельзя перехватывать все не подходящие под вышестоящие правила сообщения, т.к. в main.py подключаются еще 
роутеры, которые будут ждать сообщений
"""

"""
@router.message(F.text)
async def cmd_info(message: Message):
    await message.reply(f"Эхо: {message.text}")
"""