import instaloader

login = instaloader.Instaloader()
login.login('**USERNAME**','**SENHA**')

seguidores = instaloader.Profile.from_username(login.context, "gusta.cartola").get_followers()
seguindo = instaloader.Profile.from_username(login.context, "gusta.cartola").get_followees()

print('\n')
print('Seguidores: ' + str(seguidores._data['count']))
print('Seguindo: ' + str(seguindo._data['count']))
print('\n\n')
print('Lista e informações de Seguidores:')
print('\n')
print(seguidores._data['edges'])
