from model.history.history_in import HistoryIn


class HistoryOut(HistoryIn):
    id: int

    class Config:
        orm_mode: True
