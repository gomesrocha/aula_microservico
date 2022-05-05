from services.CotacaoDolar import cotacao
from schemas.outDate import dolar

def inf_dolar():
    valor_dolar = cotacao()
    alta = float(valor_dolar["USDBRL"]["high"])
    baixa = float(valor_dolar["USDBRL"]["low"])
    venda = float(valor_dolar["USDBRL"]["bid"])
    return dolar(high=alta, low=baixa, bid=venda)


