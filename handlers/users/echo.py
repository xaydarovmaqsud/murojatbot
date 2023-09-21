from aiogram import types

from loader import dp


# Echo bot
async def bot_echo(message: types.Message):
    await message.answer(message.text)
