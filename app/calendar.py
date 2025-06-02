from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram_calendar import SimpleCalendar
from aiogram_calendar.schemas import SimpleCalendarCallback

calendar_router = Router()

@calendar_router.message(Command("calendar"))
async def cmd_calendar(message: Message):
    await message.answer(
        "Выберите дату:",
        reply_markup=await SimpleCalendar().start_calendar()
    )

@calendar_router.callback_query(SimpleCalendarCallback.filter())
async def process_calendar(callback_query: CallbackQuery, callback_data: SimpleCalendarCallback):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.answer(
            f'Вы выбрали: {date.strftime("%d.%m.%Y")}'
        )