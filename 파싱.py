import urllib.parse
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import webbrowser

while 1:
    try:
        search = input("검색어를 입력하세요 : " ) 
        search = urllib.parse.quote(search) #URL Encoding       
        url = 'https://torrentube.net/kt/search?p&q='+str(search)
         
        options = webdriver.ChromeOptions()
        options.add_argument('headless') 
        driver = webdriver.Chrome(options=options)

        driver.get(url)
        driver.implicitly_wait(2)
        pageString = driver.page_source
        driver.quit()
        soup = BeautifulSoup(pageString, "lxml")
        num = 0  #num 초기값
        for link1 in soup.find_all(name="div",attrs={"class":"title"}):
            try:
                title = link1.select('a')[0]
                num = num+1
                print(f"{num}번 {title.get_text()}")
            except:
                pass
        mglist = [] * num #리스트 생성
        for link2 in soup.find_all(name="div",attrs={"class":"magnet"}):
            try:
                mgnet = link2.select('a')[0]['href'] #a 태그에서 href만 가져오기
                mglist.append(str(mgnet)) #리스트에 넣기
            except:
                pass
            
        
        mgnum = int(input("번호를 선택하세요 (99 입력하면 처음으로) : " ))
        if mgnum == 99:
            print("=================================")
            continue
        else:
            mglink = mglist[mgnum]
            webbrowser.open(mglink)
            continue 
    except:
         print("검색된 파일이 없거나 불러오는데 오류가 발생했습니다.")
         print("검색어를 정확히 입력해주세요.")
	
