
import pyqrcode 
from pyqrcode import QRCode 


qrn=input("Enetr Your QRname:")
s = input("Enter Your URL: ")


url = pyqrcode.create(s)


url.svg(f'{qrn}.svg', scale=8)


url.png(f'{qrn}.png', scale=8)
