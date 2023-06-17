from models import Owner, Book, engine
from sqlmodel import Session, select
from sqlalchemy.orm import joinedload

def add_owner(age: int, name: str):
    person = Owner(name=name, age=age)

    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)
    
    return person

def get_owners() -> list[Owner]:
    query = select(Owner)
    with Session(engine) as session:
        result = session.execute(query).scalars().all()
    return result

def get_books():
    query = select(Book).options(joinedload('*'))
    #query = query.subquery()

    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()
    return result

def add_book(title: str, owner_id: int):
    book = Book(title=title, owner_id=owner_id)

    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)

    return book

def filter_owners_by(id: int = None, age: int = None, limit: int = 5):
    query = select(Owner)

    if id is not None:
        query = query.where(Owner.id == id)
    if age is not None:
        query = query.where(Owner.age == age)
    if limit is not None:
        query = query.limit(limit)

    with Session(engine) as session:
        result = session.execute(query).scalars().all()

    return result

