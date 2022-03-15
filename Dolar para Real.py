from forex_python.converter import CurrencyRates
conversor = CurrencyRates()
dolar = float(input('Valor em Dólar: '))
real =round(conversor.convert("USD", "BRL", dolar), 2)
print(f"${dolar} = R$ {real}")
