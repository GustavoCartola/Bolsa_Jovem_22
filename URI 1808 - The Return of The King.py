def x(d, q):
    si = []
    z = ''
    c = 0
    for i in d:
        i = int(i)
        if z == 1 and i == 0:
            si.append(9)
            q += -1
        si.append(i)
        z = i
    for a in si:
        c += a
    return c, q
S = input()
y = len(S)
w, r = x(S, y)
result = w / r
print('{:.2f}'.format(result))