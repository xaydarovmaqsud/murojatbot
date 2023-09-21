from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware

from aiogram import Dispatcher
from sqlalchemy.orm import sessionmaker
from .db import DbSessionMiddleware
from .language import I18nMiddleware


def register_middlewares(dp: Dispatcher, session_fabric: sessionmaker) -> None:
    dp.middleware.setup(DbSessionMiddleware(session_pool=session_fabric))
    # dp.middleware.setup(I18nMiddleware(domain="messages", path="locales", default="uz"))
    dp.middleware.setup(ThrottlingMiddleware())
