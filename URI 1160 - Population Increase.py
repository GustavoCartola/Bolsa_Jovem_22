inteiroT = int(input())
inteiroPA = int()
inteiroPB = int()
numG1 = float()
numG2 = float()
ANOS = int()
SECULO = 'Mais de 1 seculo.'
for i in range(0, inteiroT):
    inteiroPA, inteiroPB, numG1, numG2 = input().split()
    inteiroPA = int(inteiroPA)
    inteiroPB = int(inteiroPB)
    numG1 = float(numG1)
    numG2 = float(numG2)
    ANOS = 0
    while (inteiroPB >= inteiroPA):
        inteiroPB = int(inteiroPB * (1+ numG2 /100 ))
        inteiroPA = int(inteiroPA * (1+ numG1 /100 ))
        ANOS += 1
        if ANOS >= 101:
            print(SECULO)
            break
    if ANOS <= 100:
        print((ANOS),'anos.')