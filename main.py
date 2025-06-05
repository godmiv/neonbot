import asyncio
import os

from aiogram import Bot, Dispatcher, types
#Диспетчер из файла handlers.py
from app.handlers import router
from app.calendar import calendar_router
from app.time_router import time_router
from app.command_list import commands_list
# Объект бота
bot = Bot(token=os.environ["NEON_BOT_TOKEN"])
# Диспетчер
dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(router)
    # Подключаем роутер календаря
    dp.include_router(calendar_router)
    dp.include_router(time_router)
    await bot.set_my_commands(commands=commands_list, scope=types.BotCommandScopeAllPrivateChats()) # Показывает меню, даееые берет из файла commands_list
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')