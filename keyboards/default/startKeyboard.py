from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Maxsulotlar"),
            KeyboardButton(text="Qo'llanma")
        ],
    ],
    resize_keyboard=True 
)