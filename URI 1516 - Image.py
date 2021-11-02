while True:
    naltura, mlargura = input().split()

    if int(naltura) == 0 and int(mlargura) == 0:
        break

    if int(naltura) >= 1 and int(mlargura) <= 50:
        resultlinhas = []

        for i in range(int(naltura)):
            resultlinhas.append(input())
        variavela,variavelb = input().split()
        variavela = int(int(variavela)/int(naltura))
        variavelb = int(int(variavelb)/int(mlargura))

        for j in resultlinhas:
            for k in range(variavela):
                for l in j:
                    result = (variavelb * l)
                    print((result), end="")
                print("\n", end="")
        print("")