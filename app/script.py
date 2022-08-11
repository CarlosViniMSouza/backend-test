from datetime import date, datetime
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# our user
class Investor(BaseModel):
    name: str
    capital: float
    data_initial: str = datetime.now()
    data_end: str = date(2023, 1, 1)
    amount: float


fakeDatas = {
    "name": "Carlos",
    "capital": 1000.5,
    "data_initial": "2021-01-01",
    "data_end": "2022-11-11",
    "amount": 1520.76
}


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
    return user


@app.get("list/{name}")
async def pagination(user: Investor):
    return user

# others functions necessary


def gainCalculation():
    pass


def taxation():
    pass
