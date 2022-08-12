from pydantic import BaseModel
from datetime import date


class Investor(BaseModel):
    proprietor: str
    investiment: list = [
        {
            "name": str,
            "capital": float,
            "data_initial": date(2022, 1, 1),
            "data_end": date(2023, 1, 1),
            "amount": float
        }
    ]

    def gainCalculation():
        timeDifference = Investor.investiment[2] - Investor.investiment[3]

        for i in timeDifference:
            gain += Investor.investiment[1] * 0.52

        return gain

    def taxation():
        tax = (Investor.investiment[4] - Investor.investiment[1]) * 0.2

        return tax


"""
dataExample = {
    "proprietor": "Carlos Souza"
    "investiment": [
        {
            "name": "Brazil Bank",
            "capital": 2050.55,
            "data_initial": datetime.now(),
            "data_end": date(2023, 1, 1),
            "amount": 5000.95
        },
        {
            "name": "NuBank",
            "capital": 2100.55,
            "data_initial": datetime.now(),
            "data_end": date(2023, 1, 1),
            "amount": 4000.95
        }
    ]
}
"""
