from pydantic import BaseModel
from datetime import date


class Investor(BaseModel):
    proprietor: str
    invest: dict = {
        "name": str,
        "capital": float,
        "data_initial": date,
        "data_end": date,
    }

    def gainCalculation():
        timeDifference = Investor.invest.get(
            "data_end") - Investor.invest.get("data_initial")

        for i in timeDifference:
            gain += Investor.invest.get("capital") * 0.52

        Investor.invest.update({"amount": gain})

    def taxation():
        tax = (Investor.invest.get("amount") -
               Investor.invest.get("capital")) * 0.2

        Investor.invest.update({"tax": tax})


"""
dataExample = {
    "proprietor": "Carlos Souza",
    "investiment": {
        "name": "Brazil Bank",
        "capital": 2050.55,
        "data_initial": date,
        "data_end": date,
        "amount": 5000.95
        "tax": 610.8
    }
}
"""
