from pydantic import BaseModel

class dolar(BaseModel):
    high: float
    low: float
    bid: float