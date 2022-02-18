from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startKeyboard import menuStart
from loader import dp
import logging

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # logging.info(message)
    # logging.info(f"{message.from_user.username=}")
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=menuStart)
