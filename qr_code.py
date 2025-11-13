import qrcode

data=input("Enter data to encode in QR code: ").strip()
file_name=input("Enter file name to save QR code: ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(file_name)
print(f"QR code saved as {file_name}")