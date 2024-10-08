from typing import Self
from app.extensions.orm import (
    Column,
    Table,
    BaseModel,
    IRepositoryBase,
    ForeignKey,
)

from datetime import datetime

from .country import Country


class City(Table):
    __table_name__ = "city"

    city_id: int = Column[int](is_primary_key=True)
    city: str
    country_id: str
    last_update: datetime

    Country = ForeignKey[Self, Country](__table_name__, Country, lambda ci, co: ci.country_id == co.country_id)


class CityModel(BaseModel[City]):
    def __new__[TRepo](cls, repository: IRepositoryBase[TRepo]):
        return super().__new__(cls, City, repository=repository)
