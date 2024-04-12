from typing import Optional

from database import Antispam
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class AntispamService:
    @staticmethod
    async def add_phone_in_list(phone: str, session: AsyncSession) -> Antispam:
        antispam = Antispam()
        antispam.phone = phone
        session.add(antispam)
        await session.commit()
        return antispam

    @staticmethod
    async def get_phone(phone: str, session: AsyncSession) -> Optional[Antispam]:
        query = await session.execute(select(Antispam).where(Antispam.phone == phone))
        phone = query.scalars().first()
        return phone
