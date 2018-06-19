from bs4 import BeautifulSoup
import requests
import urllib.parse as rep #한글을 유니코트로 바꾸기 위한 매서드
import sys
import io
import os


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding ='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding ='utf-8')

# savePath = "C:/kookmin/python/lecture/"
base="http://doc.mindscale.kr/km/python/"
quote = rep.quote_plus("py01.pdf")
url = base + quote
r = requests.get(url, stream=True)
with open('c:/kookmin/python/lecture1.pdf', 'wb') as f:
    f.write(r.content)
