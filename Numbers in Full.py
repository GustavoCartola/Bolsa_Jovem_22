from num2words import num2words

num = int(input('Número: '))  # Prompt for a number
num_normal = num2words(num, lang='pt-br')  # Convert number to words in Portuguese
num_ordinal = num2words(num, lang='pt-br', to='ordinal')  # Convert number to ordinal words in Portuguese

print('Normal: ', num_normal)  # Print the number in words
print('Ordinal: ', num_ordinal)  # Print the number in ordinal form
