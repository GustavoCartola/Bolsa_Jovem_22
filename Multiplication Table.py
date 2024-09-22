number = int(input('Informe o número : '))  # Prompt for the number

print('\n Tabuada do', number, ':')

for i in range(1, 11):
    print(number, 'X', i, '=', (number * i))  # Print the multiplication table
