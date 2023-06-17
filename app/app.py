from fastapi import FastAPI
from schemas import grapql_app

app = FastAPI()
app.include_router(grapql_app, prefix='/graphql')
