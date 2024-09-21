avariable = float(input("Valor de A: "))
bvariable = float(input("Valor de B: "))
cvariable = float(input("Valor de C: "))
delta = ((bvariable**2) - (4*avariable*cvariable))  # calculate delta
x1 = ((-bvariable + delta ** (1/2)) / (2*avariable))  # calculate x1
x2 = ((-bvariable - delta ** (1/2)) / (2*avariable))  # calculate x2
if delta < 0:
    print('Delta Inválido')
if delta >= 0:
    print("Resultado de x1: ", x1)
    print("Resultado de x2: ", x2)
