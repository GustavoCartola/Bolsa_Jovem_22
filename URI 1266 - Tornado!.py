loop="0"
while"0"==loop:
    comec=poste=auxi=calc=int(0)
    casosteste=input()
    if "0"==casosteste:
        break
    estadoposte=input().split()
    for a in range(int(casosteste)):
        if comec==0 and estadoposte[a]=="0":
            poste=poste+1
            auxi = auxi + 1
        elif 1==comec and estadoposte[a]=="0":
            poste=poste+1
        else:
            comec=1
            calc=calc+int(poste/2)
            poste=0
    z=int(auxi/2)
    if 0<=poste:
        calc=calc-z
        poste=poste+auxi
        calc=calc+int(poste/2)
    result=int(calc)
    print("{}".format(result))