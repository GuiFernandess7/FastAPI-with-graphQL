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

class PersonModel(SQLModel, table=True):
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
    person = PersonModel(name=name, age=age)

    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)
    
    return person

@strawberry.type
class Query:

    @strawberry.field
    def all_people(self) -> list[Person]:
        query = select(PersonModel)
        with Session(engine) as session:
            result = session.execute(query).scalars().all()
        return result
    
@strawberry.type
class Mutation:
    create_app: Person = strawberry.field(resolver=create_app)

schema = strawberry.Schema(
    query=Query, 
    mutation=Mutation)
# send it with: http :8000/graphl query="{ allPeople { idade }}"