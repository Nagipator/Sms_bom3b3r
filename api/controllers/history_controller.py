from check_functions import check_phone
from database import get_session
from fastapi import APIRouter, Depends, HTTPException
from model import HistoryOut
from services.history_service import HistoryService
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

router = APIRouter(prefix="/history", tags=["History"])


@router.put("/{user_id}&{time}", response_model=HistoryOut)
async def update_time_by_user_id(user_id: int, time: str, session: AsyncSession = Depends(get_session)):
    history = await HistoryService.get_history_by_user_id(user_id, session)
    if history:
        history.time = time
        await session.commit()
        return HistoryOut(**history.to_dict())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"""History with user id {user_id} not found!""")


@router.put("/{user_id}", response_model=HistoryOut)
async def update_last_phone_by_user_id(user_id: int, last_phone: str, session: AsyncSession = Depends(get_session)):
    phone_error = await check_phone(last_phone)  # Проверка телефона
    if phone_error:
        return phone_error

    history = await HistoryService.get_history_by_user_id(user_id, session)
    if history:
        history.last_phone = last_phone
        await session.commit()
        return HistoryOut(**history.to_dict())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"""History with user id {user_id} not found!""")
