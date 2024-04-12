from database import History
from model import HistoryIn
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class HistoryService:
    @staticmethod
    async def create_history(history_dto: HistoryIn, session: AsyncSession) -> History:
        history = History(**history_dto.model_dump())
        session.add(history)
        await session.commit()
        return history

    @staticmethod
    async def get_history_by_user_id(user_id: int, session: AsyncSession) -> History:
        query = await session.execute(select(History).where(History.user_id == user_id))
        history = query.scalars().first()
        return history
