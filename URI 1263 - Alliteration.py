while True:
    try:
        casoteste = input().lower().split()
        numpalavra = int(0)
        palavra1 = []
        palavra2 = []
        for i in casoteste:
            if palavra1 == i[0]:
                if palavra2 != i[0]:
                    numpalavra = (numpalavra + 1)
            palavra2 = palavra1
            palavra1 = i[0]
        print('{}'.format(numpalavra))
    except EOFError:
        break