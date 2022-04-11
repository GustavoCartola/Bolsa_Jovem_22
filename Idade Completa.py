from datetime import datetime

ano = int(input("Ano de nascimento? "))
mes = int(input("Mês de nascimento? "))
dia = int(input("Dia de nascimento? "))

data = datetime(ano, mes, dia)
dataatual = datetime.now()

diferenca = dataatual - data

dias = diferenca.days
anos, dias = dias // 365, dias % 365
meses, dias = dias // 30, dias % 30

print(f'Você tem {anos} anos, {meses} meses e {dias} dias')
