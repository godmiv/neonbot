import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Объект бота
bot = Bot(token=os.environ["NEON_BOT_TOKEN"])
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
