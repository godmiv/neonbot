import asyncio
import os

from aiogram import Bot, Dispatcher
#Диспетчер из файла handlers.py
from app.handlers import router
from app.calendar import calendar_router

# Объект бота
bot = Bot(token=os.environ["NEON_BOT_TOKEN"])
# Диспетчер
dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(router)
    # Подключаем роутер календаря
    dp.include_router(calendar_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')