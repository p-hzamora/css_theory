from app.extensions.orm import (
    Column,
    Table,
    BaseModel,
    IRepositoryBase,
)

from datetime import datetime


class Country(Table):
    __table_name__ = "country"

    country_id: int = Column[int](is_primary_key=True)
    country: str
    last_update: datetime


class CountryModel(BaseModel[Country]):
    def __new__[TRepo](cls, repository: IRepositoryBase[TRepo]):
        return super().__new__(cls, Country, repository=repository)
