#왜 크롤링을 배워야 하는가?
# 내가 원하는 데이터가 알맞게 찾아지지 않으므로 내가 데이터를 수집해야 하는 일이 발생할 수 있다.

#jupiter notebook 사용
# 1. 모듈 설치 필요
# pip 명령어가 영 안먹어서 시간을 많이 소요했다
# 여전히 해결됐는지는 의문?.?
# 일단 구글 드라이브는 따로 검색하여 받아주었다. 경로 설정이 잘못되었는지 잘못된 경로라고 자꾸 떴음
# 나는 파이썬 3.10을 사용하는데 자꾸 쓰지도 않는 3.97을 이용하라는 것이었다
# 문제 해결인지 모르겠지만 아나콘다 가상환경을 바꾸고 언어를 3.97로 변경해주었다

#어쨌든 주피터 노트북에서
#첫번째로 모듈을 설치
!pip install selenium
!pip install webdriver-manager #이것도 속썩였다 web-driver-manager인지 _인지뭔지 일단 -한번으로 됐다
#pip 명령어도 안먹어서 자꾸 instax? 정의되지 않은 변수라고 떠서 !를 앞에 넣어 강제로 실행해주었다

#두번째는 모듈 불러오기
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

#추가적 설치
from selenium.common.exceptions import NoSuchElementException #exception 구문 써서인지 오류나서 넣었다
from selenium.webdriver.common.by import By #find_element_by 함수가 자꾸 error나서 불가피하게 find_element사용했다

#세번째는 창 띄우고 주소 삽입하기
#일단 driver 구문까지는 어떤 크롤링을 하든 쓰는 것 같으니 외워두도록 하자
driver=webdriver.Chrome(ChromeDriverManager().install())
url="https://www.instagram.com"
driver.get(url)
#get 함수를 사용해 크롤링할 url에 접근한다.


#네번째는 아이디 비밀번호 넣고 로그인하기
email="내아이디"
input_id=driver.find_elements_by_css_selector("input._2hvTZ.pexuQ.zyHYP")[0]
input_id.send_keys(email)
password='내비밀번호'
input_pw=driver.find_elements_by_css_selector("input._2hvTZ.pexuQ.zyHYP")[1]
input_pw.send_keys(password)
input_pw.submit() #입력
time.sleep(2) #대기

#셀레니움 크롤링을 위해서는 HTML의 요소(element)에 접근할 수 있어야 한다
#<p class ="foo"> this  is a paragraph</p>
#전체를 element, p시작부분을 start tag, 내용부를 content, 끝태그를 end tag라 한다

#요소에 접근하는 메서드들은 다음과 같다
#find_element_by
#앞부분은 모두 동일하고 _id/_name/_xpath/_link_text/_partial_link_text/_tag_name/_class_name/_css_selector
#등이 있다. f12로 개발자 도구를 열어 가져오기 원하는 부분을 카피해오면 편리하다

# 다만, 나처럼 find_element_by가 작동하지 않을 경우가 있을 수 있는데
# 앞서 서술한 것처럼 모듈을 설치하고
from selenium.webdriver.common.by import By #find_element_by
#변수 = driver.find_element(By.CSS_SELECTOR, "찾을경로")
#등으로 사용할 수 있다. By.부분만 바꿔주면 다른 메서드로 사용가능

#다섯번째로, 검색해야함
word='서울근교카페' #원하는 검색에 넣고
driver.get("https://www.instagram.com/explore/tags/"+word)
time.sleep(5)
#첫번째 게시글 열기
first=driver.find_element_by_css_selector("div._9AhH0")
first.click()
time.sleep(2)

#같은 과정을 여러번 반복해줌
all_data=[]
for i in range(0,5):
    html=driver.page_source
    soup=BeautifulSoup(html, 'html.parser')
    time.sleep(3)
    try:
        content=soup.select("div.C4VMK > span")[0].text #본문
    except:
        content=" "
    try:
        like=soup.select("a.zV_Nj>span")[0].text #좋아요

    except:
        like=" "
    try:
        date=soup.select_one("a.c-Yi7").text #날짜
    except:
        date=" "
    try:
        location=soup.select_one("a.O4GlU").text #위치
    except:
        location=" "
    data=[content, like, date, location]
    all_data.append(data)
    #right=driver.find_element_by_css_selector("div.l8mY4.feth3") #자꾸오류남ㅜㅜ
    right = driver.find_element(By.CSS_SELECTOR, "div.l8mY4.feth3")
    right.click()
    time.sleep(2)

cafeOfseoul=pd.DataFrame(all_data,columns=['내용','좋아요','날짜','장소'])
cafeOfseoul.to_excel("seoulcafe.xlsx", index=False)

#이상 인스타그램에서 정보를 크롤링해오는 방법이었다.

#another





