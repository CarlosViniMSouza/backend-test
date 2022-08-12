from fastapi import FastAPI
from app.models import Investor


app = FastAPI()


# for start-up application
@app.get("/")
async def apiRoot():
    return {"message": "API working"}


# functions requisited
@app.post("/create")
async def create(user: Investor):
    return user


@app.get("/view")
async def view(user: Investor):
    return user


@app.get("withdrawal/{name}")
async def withdrawal(user: Investor):
    name = user.proprietor

    while user.proprietor == name:
        return user


@app.get("list/{name}")
async def pagination(user: Investor):
    name: user.proprietor

    while user.proprietor == name:
        return user
