import pyqrcode

def qr_code():
    data = input('Enter any link/info : ')
    a=pyqrcode.create(data)
    a.png('text.png',scale=8)
    print('QR Ready!!')

if __name__ == '__main__':
    qr_code()
