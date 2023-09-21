from aiogram import Dispatcher

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, ChatTypeFilter
from aiogram.types import ParseMode


from . import help
from . import start
from . import echo


from .start import *
from .echo import *

def register_commands(dp: Dispatcher) -> None:
    dp.register_message_handler(start_bot, commands=["start"], state="*")
    dp.register_message_handler(ism, state=ChatState.Ism)
    dp.register_message_handler(guruh, state=ChatState.Guruh)
    dp.register_message_handler(telefon,content_types=types.ContentType.CONTACT, state=ChatState.Tel)
    dp.register_message_handler(xabar, lambda message: message.text == '💬 Murojat yo\'llash', state='*')
    dp.register_message_handler(yubor, state=ChatState.Xabar)

#
# def register_echo(dp: Dispatcher) -> None:
#     dp.register_message_handler(bot_echo, state="*")