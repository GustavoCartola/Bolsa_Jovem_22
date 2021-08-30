mens = input()
decodif = ''
i = 0
while i<len (mens):
    if mens[i]==' ':
        decodif = decodif + ' '
    else:
        i = i + 1
        decodif = decodif + mens[i]
    i = i + 1
print(decodif)