# FastAPI with GraphQL

This is an example application that combines the powerful FastAPI framework with the flexibility of GraphQL. FastAPI is a fast and easy-to-use web framework for building APIs with Python 3.7+ based on standard Python type hints. GraphQL is a query language and data manipulation language for APIs that gives clients the ability to request exactly the data they need and nothing more.

## Previews

### Get book owners and books:

https://github.com/GuiFernandess7/FastAPI-with-graphQL/assets/63022500/2ce9f678-05e2-4282-ac24-914bf7ad0618

https://github.com/GuiFernandess7/FastAPI-with-graphQL/assets/63022500/1a2ab34b-d98c-437b-8282-95f1d3c49a2a

### Make mutations (Add books and owners):

https://github.com/GuiFernandess7/FastAPI-with-graphQL/assets/63022500/9756f806-86bf-4573-9912-f93065cd8371

https://github.com/GuiFernandess7/FastAPI-with-graphQL/assets/63022500/b673e97d-b622-48bf-93fa-908f3a13de95

### Filter owners by age, name and limit:

https://github.com/GuiFernandess7/FastAPI-with-graphQL/assets/63022500/2a29f57f-5211-474d-8c90-50a5b9eec3cf

## Features
* **Fast and efficient**: FastAPI is built on top of Starlette, a high-performance asynchronous framework. This allows for high-speed API processing and efficient handling of requests.
* **Type safety**: FastAPI leverages Python type hints to provide type checking and validation. This helps catch errors early and makes the code more robust.
* **GraphQL support**: FastAPI seamlessly integrates with GraphQL using the Strawberry library. GraphQL allows clients to specify the exact data they need, reducing over-fetching and under-fetching of data.
* **Flexible data querying**: With GraphQL, clients can query multiple related resources in a single request and receive only the fields they are interested in. This reduces the number of round-trips to the server and improves overall performance.
* **Mutation support**: GraphQL provides mutation operations to create, update, and delete data. FastAPI allows defining mutation resolvers to handle these operations and interact with the underlying data storage.
* **Easy-to-use**: FastAPI's intuitive syntax and automatic validation make it easy to build robust APIs. The combination of FastAPI and GraphQL provides a powerful and flexible development.

## Getting Started
To get started with FastAPI and GraphQL:
* Install the necessary dependencies: FastAPI, Strawberry, and any other libraries you may need.
```
pip install fastapi strawberry-graphql sqlmodel
```
or 
```
pip install fastapi strawberry-graphql sqlalchemy
```

* Define your data models using Python classes and SQLModel or any other ORM you prefer.
```
from typing import Optional
from sqlmodel import (
    SQLModel, 
    Field, 
    create_engine,
    select,
    Session
)

engine = create_engine('sqlite:///database.db')

class PersonModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int

SQLModel.metadata.create_all(engine)
```
* Create resolvers for your GraphQL schema, which define how to fetch and manipulate the data.
```
@strawberry.type
class Person:
    id: Optional[int]
    name: str
    age: int

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
```
* Use FastAPI to create API endpoints for GraphQL queries and mutations.
* Test and explore your API using the interactive documentation generated by FastAPI.

## Conclusion
FastAPI with GraphQL is a powerful combination for building high-performance APIs with a flexible data querying language. It provides the benefits of type safety, automatic documentation, and efficient data retrieval. By leveraging FastAPI's speed and scalability and GraphQL's flexibility and efficiency, developers can create robust and user-friendly APIs.
