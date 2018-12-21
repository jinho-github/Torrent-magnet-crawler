from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

search = input("검색어를 입력하세요 : " ) 

req = Request('https://torrentwal.net/bbs/s.php?k='+str(search)+'&q=', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage,"lxml")
num = 0
print(req)
for link1 in soup.find_all(name="td",attrs={"class":"subject"}):
    title = link1.select('a')[1] #a태그중 0다음인 1번째 데이터 가져오기
    num = num+1
    #print(link1.find('a').text)
    
    print(str(num)+"번, "+title.get_text().strip()) #문자열만 가져오기

##유니코드 문제 해결

##마그넷 형식 magnet:?xt=urn:btih:68375FAE44313634251CD075EF617E8859319F63
