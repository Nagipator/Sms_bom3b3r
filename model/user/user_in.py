from pydantic import BaseModel


class UserIn(BaseModel):
    nikname: str
    phone: str
    password: str

    class Config:
        orm_mode: True
