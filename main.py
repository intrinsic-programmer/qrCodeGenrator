import qrcode

img = qrcode.make(input("Enter the link you wanna generate QR Code:"))
img.save(input("Name of the QR Code File: ") + ".jpg")