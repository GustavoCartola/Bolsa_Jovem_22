import phonenumbers
from phonenumbers import geocoder, carrier
numero = input('Número: ')
celular = phonenumbers.parse(numero)
operadora = carrier.name_for_number(celular, 'pt-br')
estado = geocoder.description_for_number(celular, 'pt-br')
print("A operadora é: " + operadora)
print("O estado é: " + estado)