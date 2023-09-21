from aiogram import executor
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from config import load_config
from handlers.users import *
# from tgbot.handlers.query_handlers import *
from middlewares import register_middlewares
from misc.req_func import make_connection_string

logger = logging.getLogger(__name__)
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):

    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")
    config = load_config("bot.ini")
    engine = create_async_engine(
        make_connection_string(config.db), future=True, echo=False
    )

    session_fabric = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    if config.tg_bot.use_redis:
        storage = RedisStorage()
    else:
        storage = MemoryStorage()

    register_middlewares(dp, session_fabric)
    register_commands(dp)
    # register_echo(dp)





if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
