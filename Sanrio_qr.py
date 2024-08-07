import qrcode

website_link = 'https://www.sanrio.com'

qr = qrcode.QRCode(version = 2, box_size = 10,  border = 5)
qr.add_data(website_link)
qr.make(fit = True)

img = qr.make_image(fill_color = "lightblue",back_color="blue")

img.save('sanrio_qrcode.png')



