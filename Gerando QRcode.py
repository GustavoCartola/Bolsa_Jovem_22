import qrcode

conteudo_qr = 'https://github.com/GustavoCartola/Bolsa-Jovem'
qr = qrcode.QRCode(version=2,
                   box_size=20,
                   border=1)
qr.add_data(conteudo_qr)
qr.make(fit=True)
img = qr.make_image(fill_color='black',
                    back_color='white')

img.save('qrcode.png')
