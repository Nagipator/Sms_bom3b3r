from database.base_meta import BaseSQLAlchemyModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(BaseSQLAlchemyModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nikname = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

    stories = relationship("History", back_populates="user")

    def __repr__(self):
        return str(self)
