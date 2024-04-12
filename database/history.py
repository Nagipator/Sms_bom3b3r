from database.base_meta import BaseSQLAlchemyModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class History(BaseSQLAlchemyModel):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    time = Column(String, nullable=True)
    last_phone = Column(String, nullable=True)

    user = relationship("User", back_populates="stories")

    def __repr__(self):
        return str(self)
