from captcha.image import ImageCaptcha
image = ImageCaptcha(width=280, height=90)
text = input("Digite seu captcha:")  # prompt for captcha input
generate = image.generate(text)  # generate the captcha image
image.write(text, 'captcha.png')  # save the captcha image as 'captcha.png'
