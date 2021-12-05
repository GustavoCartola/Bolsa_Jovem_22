loop = "0"
string = int(0)
while loop == "0":
    mensagem = input().split()
    if mensagem == ["0"]:
        break
    vetor = []
    for a in mensagem:
        z = len(a)
        vetor.append(str(z))
        if z >= 1 and z <= 100:
            if string <= z:
                maior = a
                string = z
    maiorintervalo = "-".join(vetor)
    print("{}".format(maiorintervalo))
print("\nThe biggest word: {}".format(maior))
