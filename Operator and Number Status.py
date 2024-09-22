import phonenumbers
from phonenumbers import geocoder, carrier

number = input('Número: ')  # Prompt for the phone number
cellphone = phonenumbers.parse(number)  # Parse the phone number
carrier_name = carrier.name_for_number(cellphone, 'pt-br')  # Get the carrier name in Portuguese
state = geocoder.description_for_number(cellphone, 'pt-br')  # Get the state description in Portuguese

print("A operadora é: " + carrier_name)  # Print the carrier
print("O estado é: " + state)  # Print the state
