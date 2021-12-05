while True:
    nro = int(input())
    if nro == 0:
        break
    ing, uil, rita = 0, 0, 0
    for a in range(nro):
        num = input().split()
        uil0, rita1, ing2 = int(num[0]), int(num[1]), int(num[2])
        y = 0
        if uil0 > y:
            y = uil0
        if rita1 > y:
            y = rita1
        if ing2 > y:
            y = ing2
        if rita1 and (not (rita1 & (rita1 - 1))):
            rita += 1
            if y == rita1:
                rita += 1
        if ing2 and (not (ing2 & (ing2 - 1))):
            ing += 1
            if y == ing2:
                ing += 1
        if uil0 and (not (uil0 & (uil0 - 1))):
            uil += 1
            if y == uil0:
                uil += 1
    if ing < rita and uil < rita:
        print("Rita")
    elif rita < ing and uil < ing:
        print("Ingred")
    elif ing < uil and rita < uil:
        print("Uilton")
    else:
        print("URI")
