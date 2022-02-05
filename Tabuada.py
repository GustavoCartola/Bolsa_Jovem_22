numero = int(input('Informe o número : '))

print('\n Tabuada do', numero, ':')

for i in range(1, 11):
    print(numero, 'X', i, '=', (numero * i))