from typing import Optional, List
from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    Relationship
)

engine = create_engine('sqlite:///database.db')


class Owner(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int

    books: List['Book'] = Relationship(back_populates='owner')


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str

    owner_id: Optional[int] = Field(default=None, foreign_key='owner.id')
    owner: Optional[Owner] = Relationship(back_populates='books')


SQLModel.metadata.create_all(engine)