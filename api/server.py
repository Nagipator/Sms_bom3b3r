from typing import Annotated

from database import get_session
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from model import Token
from services import UserService, AuthService
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from .controllers import user_router, history_router, antispam_router

app = FastAPI(docs_url="/")
app.include_router(user_router)
app.include_router(history_router)
app.include_router(antispam_router)


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                session: AsyncSession = Depends(get_session)):
    user = await UserService.get_user_by_nikname(form_data.username, session)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect username or password")
    if not AuthService.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect username or password")
    access_token = AuthService.create_access_token_by_user(user)
    return Token(access_token=access_token, token_type="Bearer")
