from fastapi import FastAPI
from typing import Optional
from sqlmodel import (
    SQLModel, 
    Field, 
    create_engine,
    select,
    Session
)

engine = create_engine('sqlite:///database.db')

class Pessoa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    idade: int

SQLModel.metadata.create_all(engine)
    
app = FastAPI()

@app.get('/')
def home():
    return {"msg": "Deu bom"}

@app.get("/pessoa")
def people():
    query = select(Pessoa)
    with Session(engine) as session:
        result = session.execute(query).scalars().all()
    if not result:
        return {"message": "No data"}
    return result
