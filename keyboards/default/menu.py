from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pasha"),
        ],
        [
            KeyboardButton(text="Dublin"),
        ],
[
            KeyboardButton(text="Cheezy"),
        ],
    ],
    resize_keyboard=True
)