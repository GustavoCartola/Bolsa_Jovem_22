import socket as s
site = input('Site: ')  # prompt for the site URL
ip = s.gethostbyname(site)  # get the IP address of the site
print('O IP do Site "' + site + '" é: ' + ip)
