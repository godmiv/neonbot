import asyncio
import os

from aiogram import Bot, Dispatcher
#Диспетчер из файла handlers.py
from app.handlers import router

# Объект бота
bot = Bot(token=os.environ["NEON_BOT_TOKEN"])
# Диспетчер
dp = Dispatcher()

# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')