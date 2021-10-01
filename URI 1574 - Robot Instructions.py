casosteste = int(input())
posicao = int(0)
for i in range(0, casosteste):
    vetorposicao = []
    posicao = 0
    ninstrucoes = int(input())
    for j in range(0,ninstrucoes):
        instrucao = input().split()
        if instrucao[0] == 'LEFT':
            posicao += -1
            vetorposicao.append(-1)
        if instrucao[0] == 'RIGHT':
            posicao += 1
            vetorposicao.append(1)
        if instrucao[0] == 'SAME' and instrucao[1] == 'AS':
            ilovedogs = int(instrucao[2])
            if vetorposicao[ilovedogs-1] == 1:
                posicao += 1
                vetorposicao.append(1)
            if vetorposicao[ilovedogs-1] == -1:
                posicao += -1
                vetorposicao.append(-1)
    print(posicao)