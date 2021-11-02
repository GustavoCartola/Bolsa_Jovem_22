Tcasosteste = input()
comparador = 0.75
for a in range (0,int(Tcasosteste)):
    numeroalunos = input()
    nomealunos = input().split()
    registro = input().split()
    reprovou = []
    frequencia = []
    auxiliar = 0
    Z = 0

    if int(numeroalunos) >= 0 and int(numeroalunos) <= 100 :
        for b in registro:
            frequencia.append(b.replace('M',''))

        for c in range (len(frequencia)):
            for d in frequencia[c]:
                if d == 'P':
                    auxiliar = auxiliar + 1

            if comparador <= (auxiliar / len(frequencia[c])):
                pass
            else:
                reprovou.append(str(nomealunos[c]))

            auxiliar = Z
        print(*reprovou, sep=' ')