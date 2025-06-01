from aiogram import F, Router
from aiogram.filters.command import Command, CommandStart
from aiogram.types import Message

import app.keyboards as kb

router = Router()

# Хэндлер на команду /start
#@router.message(Command("start"))
#async def cmd_start(message: Message):
#    await message.answer("Привет!")

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("Привет!!!", reply_markup=kb.main)


@router.message(Command("info"))
async def cmd_info(message: Message):
    await message.answer(f"ID этого чата: {message.chat.id}")