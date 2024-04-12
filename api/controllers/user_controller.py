from bomder import send_sms
from check_functions import check_phone, check_time
from database import get_session
from fastapi import APIRouter, Depends, HTTPException
from model import UserOut, UserIn, HistoryIn
from services import UserService, AntispamService
from services.history_service import HistoryService
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from datetime import datetime

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", response_model=UserOut)
async def create_user(user_dto: UserIn, session: AsyncSession = Depends(get_session)):
    nikname_error = await UserService.get_user_by_nikname(user_dto.nikname, session)  # Проверка никнейма
    if nikname_error:
        return {"error": f"This nickname {user_dto.nikname} is already occupied"}

    phone_error = await check_phone(user_dto.phone)  # Проверка телефона
    if phone_error:
        return phone_error
    else:
        phone_re_checking = await UserService.get_user_by_phone(user_dto.phone, session)
        if phone_re_checking:
            return {"error": f"""User with this phone number {user_dto.phone} already exists"""}

    user = await UserService.create_user(user_dto, session)
    await HistoryService.create_history(HistoryIn(user_id=user.id, time=None, last_phone=None), session)
    return UserOut(**user.to_dict())


@router.put("/{id}&{role}", response_model=UserOut)
async def update_role(user_id: int, user_role: str, session: AsyncSession = Depends(get_session)):
    user = await UserService.get_user_by_id(user_id, session)
    if user:
        user.update(
            {"id": user.id, "phone": user.phone, "password": user.password, "role": user_role, "nikname": user.nikname})
        await session.commit()
        return UserOut(**user.to_dict())

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"""User with id {user_id} not found!""")


@router.put("/{id}&{phone}", response_model=UserOut)
async def update_phone(user_id: int, user_phone: str,
                       session: AsyncSession = Depends(get_session)):
    phone_error = await check_phone(user_phone)  # Проверка телефона
    if phone_error:
        return phone_error
    else:
        phone_re_checking = await UserService.get_user_by_phone(user_phone, session)
        if phone_re_checking:
            return {"error": f"""User with this phone number {user_phone} already exists"""}

    user = await UserService.get_user_by_id(user_id, session)
    if user:
        user.update(
            {"id": user.id, "phone": user_phone, "password": user.password, "role": user.role, "nikname": user.nikname})
        await session.commit()
        return UserOut(**user.to_dict())

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"""User with id {user_id} not found!""")


@router.put("/{id}", response_model=UserOut)
async def update_nikname(user_id: int, user_nikname: str, session: AsyncSession = Depends(get_session)):
    nikname_error = await UserService.get_user_by_nikname(user_nikname, session)  # Проверка никнейма
    if nikname_error:
        return {"error": f"This nickname {user_nikname} is already occupied"}

    user = await UserService.get_user_by_id(user_id, session)
    if user:
        user.update(
            {"id": user.id, "nikname": user_nikname, "phone": user.phone, "password": user.password, "role": user.role})
        await session.commit()
        return UserOut(**user.to_dict())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"""User with id {user_id} not found!""")


@router.delete("/")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await UserService.get_user_by_id(user_id, session)
    history = await HistoryService.get_history_by_user_id(user_id, session)
    if user:
        await session.delete(user)
        await session.delete(history)
        await session.commit()
        return {"status": "OK"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"""User with id {user_id} not found!""")


@router.post("/send_sms", response_model=dict)
async def start_bomber(user_id: int, phone: str, session: AsyncSession = Depends(get_session)):
    phone_error = await check_phone(phone)  # Проверка телефона
    if phone_error:
        return phone_error
    else:
        phone_re_checking = await AntispamService.get_phone(phone, session)
        if phone_re_checking:
            return {"error": f"""This phone number {phone} is on the antispam list"""}

    user = await UserService.get_user_by_id(user_id, session)
    if user:
        history = await HistoryService.get_history_by_user_id(user_id, session)
        now_time = str(datetime.today())[:19:]
        if history.time:  # Проверка времени
            time_error = await check_time(now_time, history.time, user.role)
            if not time_error[0]:
                return {"error": f"The message can be sent in {time_error[1]} minutes"}
        await send_sms(phone, user.role)
        history.time = now_time
        history.last_phone = phone
        await session.commit()
        return {"status": "OK"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"""User with id {user_id} not found!""")
