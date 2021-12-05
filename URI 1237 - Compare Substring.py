def gtls(str1):
    substr0=str1[0]
    c1=len(substr0)
    l=""
    ncsubstr=set()
    for a in range(0,c1):
        m=len(l)
        n=len(substr0[a:])
        if n<m:
            break
        substr=""
        substrin=True
        for b in range(a,c1):
            if substrin==False:
                break
            substr=substr0[a:b+1]
            if substr in ncsubstr:
                break
            o=len(substr)
            if m>o:
                continue
            for str0 in str1[1:]:
                if substr not in str0:
                    ncsubstr.add(substr)
                    substrin=False
                    break
                else:
                    continue
            if substrin==True:
                if m<o:
                    l=substr
    return l
while True:
    try:
        z=[]
        string0=input()
        string1=input()
        z.extend((string0,string1))
        y=gtls(z)
        x=len(y)
        print('{}'.format(x))
    except EOFError:
        break