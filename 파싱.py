import webbrowser
import urllib.parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

while 1:
    try:
        search = input("검색어를 입력하세요 : " ) 
        search = urllib.parse.quote(search) #URL Encoding
        req = Request('https://torrentwal.net/bbs/s.php?k='+str(search)+'&q=', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage,"lxml")
        num = 0  #num 초기값
        for link1 in soup.find_all(name="td",attrs={"class":"subject"}):
            title = link1.select('a')[1] #a태그중 0다음인 1번째 데이터 가져오기
            num = num+1
            print(str(num)+"번, "+title.get_text().strip()) #문자열만 가져오기
        mglist = [] * num #리스트 생성

        for link2 in soup.find_all(name="td",attrs={"class":"num"}):
            try:
                mgnet = link2.select('a')[0]['href'] #a 태그에서 href만 가져오기
            except:
                pass
                #print("href 없음")
            mgnet = mgnet.strip("javascript:Mag_dn('')") #문자열 자르기
            mglist.append(str(mgnet)) #리스트에 넣기

        mgnum = int(input("번호를 선택하세요 (0을 입력하면 처음으로) : " ))
        if mgnum == 0:
            print("=================================")
        else:
            mglink = mglist[mgnum]
            webbrowser.open("magnet:?xt=urn:btih:"+mglink) 
    except:
         print("검색된 파일이 없거나 불러오는데 오류가 발생했습니다.")
         print("검색어를 정확히 입력해주세요.")
	
