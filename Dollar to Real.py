from forex_python.converter import CurrencyRates
converter = CurrencyRates()  # initialize the currency converter
dollar = float(input('Valor em Dólar: '))  # prompt for the amount in dollars
real = round(converter.convert("USD", "BRL", dollar), 2)  # convert dollars to Brazilian reais
print(f"${dollar} = R$ {real}")  # display the conversion result
