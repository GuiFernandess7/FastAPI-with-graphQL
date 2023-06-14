from typing import Optional
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import strawberry

engine = sqlalchemy.create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)

Base = sqlalchemy.ext.declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    age = sqlalchemy.Column(sqlalchemy.Integer)

@strawberry.type
class Person:
    id: Optional[int]
    name: str
    age: int

@strawberry.type
class Query:

    @strawberry.field
    def all_people(self) -> list[Person]:
        with Session() as session:
            result = session.query(Pessoa).all()
            return result

schema = strawberry.Schema(query=Query)
# send it with: http :8000/graphl query="{ allPeople { age }}"
