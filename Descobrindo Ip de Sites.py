import socket as s
site = input('Site: ')
Ip = s.gethostbyname(site)
print('O IP do Site "' + site + '" é: ' + Ip)