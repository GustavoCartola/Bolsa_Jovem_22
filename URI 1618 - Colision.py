NumTest = input()
for i in range (0,int(NumTest)):
    Ax,Ay,Bx,By,Cx,Cy,Dx,Dy,Rx,Ry = input().split()
    Ax = int(Ax)
    Ay = int(Ay)
    Bx = int(Bx)
    By = int(By)
    Cx = int(Cx)
    Cy = int(Cy)
    Dx = int(Dx)
    Dy = int(Dy)
    Rx = int(Rx)
    Ry = int(Ry)
    if ((Rx <= Bx and Rx >= Ax and Ry <= Dy and Ry >= Ay )) or ((Rx >= Bx and Rx <= Ax and Ry >= Dy and Ry <= Ay )):
        print('1')
    else:
        print('0')