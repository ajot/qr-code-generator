# Import QRCode from pyqrcode
import pyqrcode
import png
  
# String which represents the QR code
str = "https://ajot.me/python-for-everyday-things/"
  
# Generate QR code
url = pyqrcode.create(str)
print(url)
  
# Create and save the svg file naming "my_qr_code.svg"
url.svg("my_qr_code.svg", scale = 8)
  
# Create and save the png file naming "my_qr_code.png"
url.png('my_qr_code.png', scale = 6)
