C = int(input())

for i in range(0,C):
    num1,oper,num2,V,resposta = input().split()
    num1 = int(num1)
    num2 = int(num2)
    resposta = int(resposta)

    if oper == '+':
        resultado = num1 + num2
    if oper == '-':
        resultado = num1 - num2
    if oper == 'x':
        resultado = num1 * num2

    resultado = abs(resposta - resultado)

    Z=[]
    Z.append('E')
    Z.append('r'*resultado)
    Z.append('o')
    Z.append('u')
    Z.append('!')
    X=''
    for i in Z:
        X+=i
    print(X)