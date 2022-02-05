import pyshorteners
url = input('Sua url:')
carregar = pyshorteners.Shortener()
novaurl = carregar.tinyurl.short(url)
print(f'Sua Url encurtada: {novaurl}')
