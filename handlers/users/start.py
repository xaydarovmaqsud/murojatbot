from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from service.repo.repository import SQLAlchemyRepos
from service.repo.user_repo import UserRepo
from loader import dp,bot
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode,ReplyKeyboardRemove
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
# import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InputFile
logging.basicConfig(level=logging.INFO)
from aiogram.dispatcher.filters.state import StatesGroup,State

class ChatState(StatesGroup):
    Ism=State()
    Guruh=State()
    Tel=State()
    Xabar=State()

async def start_bot(message: types.Message,repo: SQLAlchemyRepos,state: FSMContext):
    user = repo.get_repo(UserRepo)
    if await user.get_user(user_id=message.from_user.id) is None:
        await user.add_user(
            user_id=message.from_user.id,
            name=message.from_user.first_name,
            guruh='guruh',
            number='number'
        )
        await message.answer('Ism familyangizni kiriting:')
        await ChatState.Ism.set()
    else:
        keypad = ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = KeyboardButton('💬 Murojat yo\'llash')
        keypad.add(button1)
        await message.answer("👇 Marhamat <b>'💬 Murojat yo\'llash'</b> tugmasini bosib murojatingizni yo\'llang.",parse_mode=ParseMode.HTML,reply_markup=keypad)



async def ism(message: types.Message, repo: SQLAlchemyRepos,state: FSMContext):
    user = repo.get_repo(UserRepo)
    await user.update_name(user_id=message.from_user.id,name=message.text)
    await message.answer('Guruhingizni kiriting:')
    await ChatState.Guruh.set()


async def guruh(message: types.Message, repo: SQLAlchemyRepos):
    user = repo.get_repo(UserRepo)
    await user.update_guruh(user_id=message.from_user.id,guruh=message.text)
    contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    share_button = KeyboardButton(text="📞 Contact", request_contact=True, resize_keyboard=True, one_time_keyboard=True)
    contact_keyboard.add(share_button)
    await message.answer("👇 Telefon raqamingizni <b>'📞 Contact'</b> tugmasini bosish orqali yuboring",reply_markup=contact_keyboard)
    await ChatState.Tel.set()


async def telefon(message: types.Message, repo: SQLAlchemyRepos,state: FSMContext):
    user = repo.get_repo(UserRepo)
    print(message.contact.phone_number)
    if message.contact:
        await user.update_number(user_id=message.from_user.id, number=str(message.contact.phone_number))
        keypad = ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = KeyboardButton('💬 Murojat yo\'llash')
        keypad.add(button1)
        await message.answer("👇 Marhamat <b>'💬 Murojat yo\'llash'</b> tugmasini bosib murojatingizni yo\'llang.",parse_mode=ParseMode.HTML,reply_markup=keypad)
        await state.finish()


async def xabar(message: types.Message, repo: SQLAlchemyRepos,state: FSMContext):
    await message.answer('💬 Murojatingizni yuboring:',reply_markup=ReplyKeyboardRemove())
    await ChatState.Xabar.set()



async def yubor(message: types.Message, repo: SQLAlchemyRepos,state: FSMContext):
    user = repo.get_repo(UserRepo)
    name = await user.get_name(user_id=message.from_user.id)
    guruh = await user.get_guruh(user_id=message.from_user.id)
    contact = await user.get_number(user_id=message.from_user.id)
    keypad = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('💬 Murojat yo\'llash')
    keypad.add(button1)
    print(contact)
    await bot.send_contact(chat_id='@ksdjbdsbvhsuy', phone_number=int(contact), first_name=message.from_user.first_name)
    await bot.send_message(chat_id='@ksdjbdsbvhsuy',text=f'<b>{name} {guruh}:</b>\n\n{message.text}',parse_mode=ParseMode.HTML)
    await message.answer('✅ Murojatingiz yuborildi.',reply_markup=keypad)
    await state.finish()