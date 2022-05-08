from num2words import num2words

num = int(input('Número: '))
num_normal = num2words(num, lang='pt-br')
num_ordinal = num2words(num, lang='pt-br', to='ordinal')

print('Normal: ', num_normal)
print('Ordinal: ', num_ordinal)
