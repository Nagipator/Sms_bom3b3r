from database.base_meta import BaseSQLAlchemyModel
from sqlalchemy import Column, String


class Antispam(BaseSQLAlchemyModel):
    __tablename__ = "antispam"

    phone = Column(String, nullable=False, primary_key=True)

    def __repr__(self):
        return str(self)
