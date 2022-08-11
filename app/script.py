from datetime import date, datetime
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# our user
class Investor(BaseModel):
    proprietor: str
    capital: float
    data_initial: str = datetime.now()
    data_end: str = date(2023, 1, 1)
    amount: float


# for start-up application
@app.get("/")
async def apiRoot():
    return {"message": "API working"}


# functions requisited
@app.post("/create")
async def create():
    pass


@app.get("/view")
async def view():
    pass


@app.get("withdrawal/")
async def withdrawal():
    pass


@app.get("list")
async def pagination():
    pass


# others functions necessary
def gainCalculation():
    pass


def taxation():
    pass
