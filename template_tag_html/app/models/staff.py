from typing import Self
from app.extensions.orm import (
    Column,
    Table,
    BaseModel,
    IRepositoryBase,
    ForeignKey,
)

from app.extensions.fluent_validation import AbstractValidator, CascadeMode

from datetime import datetime

from .address import Address
from .store import Store


class Staff(Table):
    __table_name__ = "staff"

    staff_id: int = Column[int](is_primary_key=True, is_auto_increment=True)
    first_name: str
    last_name: str
    address_id: int
    picture: bytes
    email: str
    store_id: int
    active: int
    username: str
    password: str
    last_update: datetime

    Address = ForeignKey[Self, Address](__table_name__, Address, lambda s, a: s.address_id == a.address_id)
    Store = ForeignKey[Self, Store](__table_name__, Store, lambda staff, store: staff.store_id == store.store_id)


class StaffModel(BaseModel[Staff]):
    def __new__[TRepo](cls, repository: IRepositoryBase[TRepo]):
        return super().__new__(cls, Staff, repository=repository)


def return_msg(dtype: object) -> str:
    return "El tipo de dato {PropertyName} no es de tipo" + f"'{str(dtype)}'"


class StaffValidator(AbstractValidator[Staff]):
    def __init__(self) -> None:
        super().__init__()
        self.ClassLevelCascadeMode = CascadeMode.Continue
        self.rule_for(lambda s: s.staff_id).must(lambda value: isinstance(value, int)).with_message(return_msg(int)).not_null()
        self.rule_for(lambda s: s.first_name).must(lambda value: isinstance(value, str)).with_message(return_msg(str)).not_null().max_length(45)
        self.rule_for(lambda s: s.last_name).must(lambda value: isinstance(value, str)).with_message(return_msg(str)).not_null().max_length(45)
        self.rule_for(lambda s: s.address_id).must(lambda value: isinstance(value, int)).with_message(return_msg(int)).not_null()
        self.rule_for(lambda s: s.picture).must(lambda value: isinstance(value, bytes | None)).with_message(return_msg(bytes))
        self.rule_for(lambda s: s.email).must(lambda value: isinstance(value, str)).with_message(return_msg(str)).max_length(50).matches(r"^\S+@\S+\.\S+$").with_message("El campo introducido en la casilla de correo, no es un email valido").min_length(10)
        self.rule_for(lambda s: s.store_id).must(lambda value: isinstance(value, int)).with_message(return_msg(int)).not_null()
        self.rule_for(lambda s: s.active).must(lambda value: isinstance(value, int)).with_message(return_msg(int)).not_null().greater_than_or_equal_to(0).less_than_or_equal_to(10)
        self.rule_for(lambda s: s.username).must(lambda value: isinstance(value, str)).with_message(return_msg(str)).not_null().max_length(16)
        self.rule_for(lambda s: s.password).must(lambda value: isinstance(value, str)).with_message(return_msg(str)).max_length(40)
        self.rule_for(lambda s: s.last_update).must(lambda value: isinstance(value, datetime | str)).with_message(return_msg(datetime)).not_null()
