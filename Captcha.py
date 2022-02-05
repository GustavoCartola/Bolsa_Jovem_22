from captcha.image import ImageCaptcha
imagem = ImageCaptcha(width=280, height=90)
texto = input("Digite seu captcha:")
gerar = imagem.generate(texto)
imagem.write(texto, 'captcha.png')