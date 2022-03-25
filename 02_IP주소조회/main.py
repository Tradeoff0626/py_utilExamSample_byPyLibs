from cgitb import text
import socket
import requests
import re


# 내부 IP
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # socket 연결
in_addr.connect(("www.google.co.kr", 443))                      # 외부(여기선 google.co.kr)와 연결
print("내부 IP : ", in_addr.getsockname()[0])                   # 외부와 접속된 소켓의 정보로 내부 IP 조회

# 외부 IP
req = requests.get("http://ipconfig.kr")                        # ipconfig.kr에 조회된 외부 IP 확인. 결과 페이지 리턴 
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]     
    # 리턴된 페이지의 텍스트에서 정규식으로 'IP Adresss :' 뒤에 값 추출
    # raw string - 문자열 앞에 r이 붙으면 해당 문자열이 구성된 그대로 문자열로 반환
print("외부 IP : ", out_addr)

