from model.user.user_in import UserIn


class UserOut(UserIn):
    id: int
    role: str

    class Config:
        orm_mode: True
