from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class TimePicker:
    def __init__(self):
        self.hour = 0
        self.minute = 0

    def get_time(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def create_time_keyboard(self):
        # Сначала создаем список кнопок
        buttons = [
            [
                InlineKeyboardButton(text="↑ Час", callback_data="hour_up"),
                InlineKeyboardButton(text="↓ Час", callback_data="hour_down"),
                InlineKeyboardButton(text="↑ Мин", callback_data="minute_up"),
                InlineKeyboardButton(text="↓ Мин", callback_data="minute_down")
            ],
            [
                InlineKeyboardButton(text=self.get_time(), callback_data="time_display")
            ],
            [
                InlineKeyboardButton(text="✅ Подтвердить", callback_data="time_confirm")
            ]
        ]

        # Затем создаем клавиатуру с этими кнопками
        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboard

    def update_hour(self, increment: bool):
        if increment:
            self.hour = (self.hour + 1) % 24
        else:
            self.hour = (self.hour - 1) % 24

    def update_minute(self, increment: bool):
        if increment:
            self.minute = (self.minute + 5) % 60
        else:
            self.minute = (self.minute - 5) % 60