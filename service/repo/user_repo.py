from sqlalchemy import insert, select, update
from models.user import User
from service.repo.base_repo import BaseSQLAlchemyRepo


class UserRepo(BaseSQLAlchemyRepo):
    model = User

    async def add_user(self, user_id: int, name: str, guruh: str,number: str) -> None:
        sql = insert(self.model).values(user_id=user_id, name=name,guruh=guruh,number=number)
        await self._session.execute(sql)
        await self._session.commit()

    async def get_user(self, user_id: int) -> None:
        sql = select(self.model).where(self.model.user_id == user_id)
        request = await self._session.execute(sql)
        user = request.scalar()
        return user

    async def get_guruh(self, user_id: int) -> model.guruh:
        sql = select(self.model.guruh).filter(self.model.user_id == user_id)
        request = await self._session.execute(sql)
        return request.scalar()

    async def get_number(self, user_id: int) -> model.number:
        sql = select(self.model.number).filter(self.model.user_id == user_id)
        request = await self._session.execute(sql)
        return request.scalar()

    async def get_name(self, user_id: int) -> model.name:
        sql = select(self.model.name).filter(self.model.user_id == user_id)
        request = await self._session.execute(sql)
        return request.scalar()

    async def update_number(self, user_id: int, number: str) -> None:
        sql = update(self.model).where(self.model.user_id == user_id).values({'number': number})
        await self._session.execute(sql)
        await self._session.commit()

    async def update_name(self, user_id: int, name: str) -> None:
        sql = update(self.model).where(self.model.user_id == user_id).values({'name': name})
        await self._session.execute(sql)
        await self._session.commit()

    async def update_guruh(self, user_id: int, guruh: str) -> None:
        sql = update(self.model).where(self.model.user_id == user_id).values({'guruh': guruh})
        await self._session.execute(sql)
        await self._session.commit()






