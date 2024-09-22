from PIL import Image
from pyzbar.pyzbar import decode

# Decode the QR code from the image
read = decode(Image.open('qrcode.png'))

# Print the decoded data from the QR code
print(read[0].data)
