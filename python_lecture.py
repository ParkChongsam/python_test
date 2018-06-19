from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep #한글을 유니코트로 바꾸기 위한 매서드
import sys
import io
import os


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding ='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding ='utf-8')

url = "http://doc.mindscale.kr/km/python/"
# print(url)

res = req.urlopen(url).read()
print(res)
savePath = "C:/kookmin/python/lecture/"

#예외처리하기(정석정인 폴더만들기 공식)
try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))

except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise
soup = BeautifulSoup(res, "html.parser") #soup라는 메모리에 html을 담았다
# print(soup)

# lecture = soup.select("#write tr>td:nth-of-type(3)>a")
links = soup.find_all("a")
print(links)
for a in lecture:
    # href = a.attrs['href']
    # title = a.string
    print(a)
for b in links:
    # print('k',type(b),b)
    href = b.attrs['href'] #b의 속성, key값인 href를 넣어 준다attrs 는 사전형태로 표기[]
    text = b.string
    print(text, ">", href)


# res = req.urlopen(url).read() soup로 발췌한놈을 다시 ul.slides[0] ul.slides의 첫번째만 발췌한다
links =lecture.findall('a')['href']
print(link)
for i,e in enumerate(lecture,1):
    with open(savePath+"lecture_"+str(i)+".txt", "wt") as f: # 폴더이름과 파일이름 지정하기 #wt txt로 써라
        f.write(e.select_one("div#write > tr> td> a ").string) #폴더이름과 파일이름 지정한 곳에 쓰기
    fullfilename = os.path.join(savePath, savePath+'python_'+str(i)+'.pdf') #이미지를 저장할 폴더와 파일이름형식 지정함
    req.urlretrieve(e.select_one("tr > td > a")['href'],fullfilename) #속성값이 src인것의 이미지를 저장하라

import urllib2
#시도하기
def main():
    download_file("http://mensenhandel.nl/files/pdftest2.pdf")

def download_file(download_url):
    response = urllib2.urlopen(download_url)
    file = open("document.pdf", 'w')
    file.write(response.read())
    file.close()
    print("Completed")

if __name__ == "__main__":
    main()
#시도 끝

#--------------
import requests
url="https://Hostname/saveReport/file_name.pdf"    #Note: It's https
r = requests.get(url, auth=('usrname', 'password'), verify=False,stream=True)
r.raw.decode_content = True
with open("file_name.pdf", 'wb') as f:
        shutil.copyfileobj(r.raw, f)
#----------------

print("파이썬강의 다운로드 완료!")
