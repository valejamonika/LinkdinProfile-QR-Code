import qrcode

data = "https://www.linkedin.com/in/monika-valeja-ba570020b/"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # QR code version (adjust as needed)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box (adjust as needed)
    border=2,  # Border size (adjust as needed)
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="pink")

img.save("my_qr_code.png")

img.show()