from check_functions import check_phone
from database import get_session
from fastapi import APIRouter, Depends, HTTPException
from services import AntispamService
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

router = APIRouter(prefix="/antispam", tags=["Antispam"])


@router.post("/", response_model=dict)
async def create_antispam(phone: str, session: AsyncSession = Depends(get_session)):  # Надо проверку
    phone_error = await check_phone(phone)  # Проверка телефона
    if phone_error:
        return phone_error

    check = await AntispamService.get_phone(phone, session)
    if check:
        return {"error": f"""The phone number {phone} already exists in Antispam list"""}
    antispam = await AntispamService.add_phone_in_list(phone, session)
    return {"phone": antispam.phone}


@router.get("/", response_model=dict)
async def get_phone(phone: str, session: AsyncSession = Depends(get_session)):
    antispam = await AntispamService.get_phone(phone, session)
    if antispam:
        return {"phone": antispam.phone}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"""The phone number {phone} not found in Antispam list""")


@router.delete("/", response_model=dict)
async def delete_phone(phone: str, session: AsyncSession = Depends(get_session)):
    antispam = await AntispamService.get_phone(phone, session)
    if antispam:
        await session.delete(antispam)
        await session.commit()
        return {"status": "OK"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"""The phone number {phone} not found in Antispam list""")
