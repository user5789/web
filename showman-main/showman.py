import qrcode 
data = " https://amar673.github.io/showman_/" 
qr = qrcode.make(data) 
qr.save('showman.png') 
qr.show()