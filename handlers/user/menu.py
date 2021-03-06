from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu

@dp.message_handler(Command("menu"))
async def shoew_menu(message: Message):
    await message.answer("choose one", reply_markup=menu)

@dp.message_handler(Text(equals=["Dublin", "Pasha", "Cheezy"]))
async def get_food(message: Message):
    await message.answer(f"Choosen {message.text}. Thanks.  Please make order", reply_markup=ReplyKeyboardRemove())