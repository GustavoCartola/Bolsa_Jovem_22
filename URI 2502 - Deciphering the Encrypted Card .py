loop="0"
while("0"==loop):
    try:
        fim=""
        numl,numf=map(int, input().split())
        let0=input()
        let1=input()
        let1=let1.lower()
        let0=let0.lower()
        auxilet0=let0.upper()
        auxilet1=let1.upper()
        for a in range(0,numf):
            frasecrip=input()
            frasecriplist=list(frasecrip)
            for b in range(0,len(frasecriplist)):
                for c in range(0,numl):
                    if let0[c]==frasecriplist[b]:
                        frasecriplist[b]=let1[c]
                    elif let1[c]==frasecriplist[b]:
                        frasecriplist[b]=let0[c]
                    elif auxilet0[c]==frasecriplist[b]:
                        frasecriplist[b] = auxilet1[c]
                    elif auxilet1[c]==frasecriplist[b]:
                        frasecriplist[b] = auxilet0[c]
                fim=fim+frasecriplist[b]
            print("{}".format(fim))
            fim=""
        print()
    except:
        break