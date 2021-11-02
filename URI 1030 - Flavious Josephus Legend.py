casoteste = int(input())

if casoteste >= 1 and casoteste <= 30:
    for i in range(0, casoteste):
        npessoas, ktamanho = input().split()
        npessoas = int(npessoas)
        ktamanho = int(ktamanho)
        ultimo= 0

        if npessoas >= 1 and npessoas <= 10000:
            if ktamanho >= 1 and ktamanho <= 1000:
                for J in range (1, (1+npessoas)):
                    ultimo = ((ktamanho+ultimo) % J)
                ultimo = ultimo + 1

                print('Case {}: {}'.format(1 + i, ultimo))