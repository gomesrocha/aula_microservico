from fastapi import APIRouter

from domain.InfDolar import inf_dolar
from schemas.outDate import dolar

router = APIRouter()

@router.get("/")
async def raiz():
    return {"message": "Seja bem vindo ao sistema de cotação"}

@router.get("/cotacao", response_model=dolar)
async def cotacao():
    return inf_dolar()