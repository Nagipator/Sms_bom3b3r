from typing import Optional

from pydantic import BaseModel


class HistoryIn(BaseModel):
    user_id: int
    time: Optional[str]
    last_phone: Optional[str]

    class Config:
        orm_mode: True
        arbitrary_types_allowed: True
