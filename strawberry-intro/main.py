from __future__ import annotations
from typing import Optional
from sqlmodel import (
    SQLModel, 
    Field, 
    create_engine,
    select,
    Session
)
import strawberry

engine = create_engine('sqlite:///database.db')

class Pessoa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int

SQLModel.metadata.create_all(engine)

@strawberry.type
class Person:
    id: Optional[int]
    name: str
    age: int

def create_app(age: int, name: str):
    person = Person(name=name, age=age)

    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh()
    
    return person

@strawberry.type
class Mutation:
    create_app: Person = strawberry.field(resolver=create_app)

@strawberry.type
class Query:

    @strawberry.field
    def all_people(self) -> list[Person]:
        query = select(Pessoa)
        with Session(engine) as session:
            result = session.execute(query).scalars().all()
        return result

schema = strawberry.Schema(query=Query)
# send it with: http :8000/graphl query="{ allPeople { idade }}"