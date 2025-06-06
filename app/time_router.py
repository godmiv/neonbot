from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from app.timepicker import TimePicker

# Создаем роутер
time_router = Router()

class TimeStates(StatesGroup):
    selecting_time = State()


@time_router.message(Command("time"))
async def cmd_time(message: Message, state: FSMContext):
    time_picker = TimePicker()
    await state.update_data(time_picker=time_picker)
    await message.answer(
        "Выберите время:",
        reply_markup=time_picker.create_time_keyboard()
    )
    await state.set_state(TimeStates.selecting_time)


@time_router.callback_query(
    TimeStates.selecting_time,
    F.data.in_(["hour_up", "hour_down", "minute_up", "minute_down", "time_confirm"])
)
async def process_time_callback(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    time_picker: TimePicker = data.get("time_picker")

    if not time_picker:
        await callback.answer("Ошибка: время не выбрано")
        return

    match callback.data:
        case "hour_up":
            time_picker.update_hour(increment=True)
        case "hour_down":
            time_picker.update_hour(increment=False)
        case "minute_up":
            time_picker.update_minute(increment=True)
        case "minute_down":
            time_picker.update_minute(increment=False)
        case "time_confirm":
            await callback.answer(f"Выбрано время: {time_picker.get_time()}")
            await state.clear()
            return

    await state.update_data(time_picker=time_picker)

    await callback.message.edit_reply_markup(
        reply_markup=time_picker.create_time_keyboard()
    )
    await callback.answer()