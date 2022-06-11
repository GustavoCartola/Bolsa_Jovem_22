import math
valores = input().split(' ')
a, b, c = valores
a = int(a)
b = int(b)
c = int(c)
maior = (a + b + abs(a - b)) / 2
resultado = (maior + c + abs(maior - c))/2
print('%d eh o maior' %resultado)
