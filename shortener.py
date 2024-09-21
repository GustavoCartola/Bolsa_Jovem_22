import pyshorteners
url = input('Sua url:')  # prompt for the URL
shortener = pyshorteners.Shortener()  # initialize the URL shortener
short_url = shortener.tinyurl.short(url)  # shorten the URL using TinyURL
print(f'Sua Url encurtada: {short_url}')  # display the shortened URL
