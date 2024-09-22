import phonenumbers
from phonenumbers import geocoder, carrier

numero = input('Número: ')  # Prompt for the phone number
celular = phonenumbers.parse(numero)  # Parse the phone number
operadora = carrier.name_for_number(celular, 'pt-br')  # Get the carrier name in Portuguese
estado = geocoder.description_for_number(celular, 'pt-br')  # Get the state description in Portuguese

print("A operadora é: " + operadora)  # Print the carrier
print("O estado é: " + estado)  # Print the state
