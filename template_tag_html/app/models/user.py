from app.extensions.orm import (
    Column,
    Table,
    BaseModel,
    IRepositoryBase,
)


class User(Table):
    __table_name__ = "user"

    user_id: int = Column[int](is_primary_key=True, is_auto_increment=True)
    first_name: str
    last_name: str
    password: str
    email: str = Column[str](is_unique=True)


class UserModel(BaseModel[User]):
    def __new__[TRepo](cls, repository: IRepositoryBase[TRepo]):
        return super().__new__(cls, User, repository=repository)
