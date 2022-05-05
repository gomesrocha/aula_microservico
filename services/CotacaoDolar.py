import requests

def cotacao():
    dolar = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
    return dolar.json()
