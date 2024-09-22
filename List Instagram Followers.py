import instaloader

login = instaloader.Instaloader()
login.login('**USERNAME**', '**SENHA**')

followers = instaloader.Profile.from_username(login.context, "gusta.cartola").get_followers()
following = instaloader.Profile.from_username(login.context, "gusta.cartola").get_followees()

print('\n')
print('Seguidores: ' + str(followers._data['count']))  # Number of followers
print('Seguindo: ' + str(following._data['count']))  # Number of followees
print('\n\n')
print('Lista e informações de Seguidores:')  # List and information of followers
print('\n')
print(followers._data['edges'])  # Details of each follower
