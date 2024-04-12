from typing import Optional

from database import User
from model import UserIn
from services.auth_service import AuthService
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    @staticmethod
    async def create_user(user_dto: UserIn, session: AsyncSession) -> User:
        user = User(**user_dto.model_dump())
        new_password = AuthService.get_password_hash(user.password)
        user.password = new_password
        user.role = "main_user"
        session.add(user)
        await session.commit()
        return user

    @staticmethod
    async def get_user_by_id(user_id: int, session: AsyncSession) -> Optional[User]:
        query = await session.execute(select(User).where(User.id == user_id))
        user = query.scalars().first()
        return user

    @staticmethod
    async def get_user_by_nikname(user_nikname: str, session: AsyncSession) -> Optional[User]:
        query = await session.execute(select(User).where(User.nikname == user_nikname))
        user = query.scalars().first()
        return user

    @staticmethod
    async def get_user_by_phone(user_phone: str, session: AsyncSession) -> Optional[User]:
        query = await session.execute(select(User).where(User.phone == user_phone))
        user = query.scalars().first()
        return user
