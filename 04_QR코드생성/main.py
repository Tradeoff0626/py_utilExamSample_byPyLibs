# QR코드 생성 라이브러리 필요 (pip install qrcode)

import qrcode

qr_data = 'www.naver.com'
qr_image = qrcode.make(qr_data)

save_path = qr_data + '.png'
qr_image.save(save_path)