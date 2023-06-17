from typing import Optional
import strawberry
from db_functions import (
    add_owner, get_owners, get_books, add_book, filter_owners_by)
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Owner:
    id: Optional[int]
    name: str
    age: int
    books: list['Book']

@strawberry.type
class Book:
    id: Optional[int]
    title: str
    owner: Owner

@strawberry.type
class Query:
    filter_owners_by: list[Owner] = strawberry.field(resolver=filter_owners_by)
    get_owners: list[Owner] = strawberry.field(resolver=get_owners)
    get_books: list[Book] = strawberry.field(resolver=get_books)

@strawberry.type
class Mutation:
    add_owner: Owner = strawberry.field(resolver=add_owner)
    add_book: Book = strawberry.field(resolver=add_book)

schema = strawberry.Schema(
    query=Query, 
    mutation=Mutation)

grapql_app = GraphQLRouter(schema)
# send it with: http :8000/graphl query="{ allPeople { age }}"