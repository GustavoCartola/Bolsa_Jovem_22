avariavel = float(input("Valor de A: "))
bvariavel = float(input("Valor de B: "))
cvariavel = float(input("Valor de C: "))
delta = ((bvariavel**2) - (4*avariavel*cvariavel))
x1 = ((-bvariavel +delta **(1/2)) / (2*avariavel))
x2 = ((-bvariavel -delta **(1/2)) / (2*avariavel))
if delta<0:
    print('Delta Inválido')
if delta >=0:
    print("Resultado de x1: ",(x1))
    print("Resultado de x2: ",(x2))