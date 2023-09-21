from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware as BaseI18nMiddleware

from service.repo.repository import SQLAlchemyRepos
from service.repo.user_repo import UserRepo


class I18nMiddleware(BaseI18nMiddleware):

    async def get_user_locale(self, action, data):
        repo: SQLAlchemyRepos = data[-1].get('repo')
        user = types.User.get_current()
        users = repo.get_repo(UserRepo)
        try:
            language='uz'
        except:
            language='ru'

        if language:
            return language
        else:
            return user.locale
