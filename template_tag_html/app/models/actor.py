from app.extensions.orm import (
    Column,
    Table,
    BaseModel,
    IRepositoryBase,
)

from datetime import datetime


class Actor(Table):
    __table_name__ = "actor"

    actor_id: int = Column[int](is_primary_key=True)
    first_name: str
    last_name: str
    last_update: datetime


class ActorModel(BaseModel[Actor]):
    def __new__[TRepo](cls, repository: IRepositoryBase[TRepo]):
        return super().__new__(cls, Actor, repository=repository)
