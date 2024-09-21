import qrcode

conteudo_qr = 'https://github.com/GustavoCartola/Bolsa-Jovem'  # QR code content
qr = qrcode.QRCode(version=2,
                    box_size=20,
                    border=1)  # initialize QR code with parameters
qr.add_data(conteudo_qr)  # add data to the QR code
qr.make(fit=True)  # fit the QR code
img = qr.make_image(fill_color='black',
                    back_color='white')  # create the QR code image

img.save('qrcode.png')  # save the image as 'qrcode.png'
