from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep #한글을 유니코트로 바꾸기 위한 매서드
import requests
import sys
import io
import os


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding ='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding ='utf-8')

base = "http://doc.mindscale.kr/km/python/"
# print(url)

res = req.urlopen(base).read()
# print(res)
savePath = "C:/kookmin/python/lecture/"
#예외처리하기(정석정인 폴더만들기 공식)
try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))

except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise
soup = BeautifulSoup(res, "html.parser")
# print('soup', soup.prettify())

links = soup.select("#write tr td a[href^="py"]")
# print(links)

for i, b in enumerate(links, 1):
    href = b.attrs['href'] #b의 속성, key값인 href를 넣어 준다attrs 는 사전형태로 표기[]
    title = b.string
    url = base + href
    print(url)
    r = requests.get(url, stream=True)
    # with open(savePath, "Python_"+str(i)+"".txt",  'wt') as f:
    #     f.write(url)
    fullfilename = os.path.join(savePath, savePath+b.string+'.pdf')
    req.urlretrieve(url,fullfilename)

print("파이썬강의 다운로드 완료!")
