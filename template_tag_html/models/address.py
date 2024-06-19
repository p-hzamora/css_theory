from datetime import datetime
from extension.fluent_validation import AbstractValidator

from extension.orm import (
    Column,
    Table,
    ModelBase,
    IRepositoryBase,
    ForeignKey,
)

from .city import City


class Address(Table):
    __table_name__ = "address"

    address_id: int = Column[int](is_primary_key=True)
    address: str
    address2: str
    district: str
    city_id: int
    postal_code: str
    phone: str
    location: bytes | str
    last_update: datetime = Column[datetime](is_auto_generated=True)

    City = ForeignKey["Address", City](
        __table_name__, City, lambda a, c: a.city_id == c.city_id
    )


class AddressModel(ModelBase[Address]):
    def __init__(self, repository: IRepositoryBase):
        super().__init__(Address, repository=repository)


class AddressValidator(AbstractValidator[Address]):
    def __init__(self) -> None:
        super().__init__()
        self.rule_for(lambda a: a.address_id).not_null().must(
            lambda a: isinstance(a, int)
        )
        self.rule_for(lambda a: a.address).not_null().must(lambda a: isinstance(a, str))
        self.rule_for(lambda a: a.address2).not_null().must(
            lambda a: isinstance(a, str)
        )
        self.rule_for(lambda a: a.district).not_null().must(
            lambda a: isinstance(a, str)
        )
        self.rule_for(lambda a: a.city_id).not_null().must(lambda a: isinstance(a, int))
        self.rule_for(lambda a: a.postal_code).not_null().must(
            lambda a: isinstance(a, str)
        )
        self.rule_for(lambda a: a.phone).not_null().must(lambda a: isinstance(a, str))
        self.rule_for(lambda a: a.location).not_null().must(
            lambda a: isinstance(a, bytes | str)
        )
        self.rule_for(lambda a: a.last_update).not_null().must(
            lambda a: isinstance(a, datetime)
        )
