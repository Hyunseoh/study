#왜 크롤링을 배워야 하는가?
# 내가 원하는 데이터가 알맞게 찾아지지 않으므로 내가 데이터를 수집해야 하는 일이 발생할 수 있다.

#웹 크롤링 관련 파이썬 패키지들
# 기본 패키지 urllib
# requests 주로 정적 페이지를 크롤링 할 때 이용한다
# selenium  주로 동적 페이지를 크롤링할 때 이용한다. Chromedriver와 함께 이용
# BeautifulSoup 파싱(html문서를 분류, 정리하여 다루기 쉽게 바꾸는 작업)을 할 때 사용한다.

#정적 페이지에서는 대체로 find함수 사용 find('태그',{'속성'=''}) #혹은 find_all
#select함수는 괄호 안에 바로 css선택자를 넣어 원하는 정보를 찾을 수 있다.


#셀레니움 웹 크롤링
#jupiter notebook 이용했다.
# 1. 모듈 설치 필요
# pip 으로 설치가 필수적
# 일단 구글 드라이브는 따로 검색하여 다운로드했다. 경로 설정이 잘못되었는지 잘못된 경로라고 자꾸 떴음
# 나는 파이썬 3.10을 사용하는데 자꾸 쓰지도 않는 3.97을 이용하라는 것이었다
# 아나콘다 가상환경을 바꾸고 언어를 3.97로 변경해주었다

#어쨌든 주피터 노트북에서
#첫번째로 모듈을 설치
!pip install selenium
!pip install webdriver-manager #web-driver-manager인지 _인지뭔지 일단 -한번으로 됐다
#pip 명령어도 안먹어서 자꾸 instax? 정의되지 않은 변수라고 떠서 !를 앞에 넣어 강제로 실행해주었다

#두번째는 모듈 불러오기
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from package import pandas as pd
import time
.common.keys

#추가적 설치

#세번째는 창 띄우고 주소 삽입하기
#인스타그램 크롤링을 해 보았다.
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
#보통 x-path, css_selector 둘이 가장 많이 사용된다



#다섯번째로, 검색
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

#try-except 예외 처리구문
#except [발생 오류 [as 오류 메시지 변수]]:


#another
#for문 대신 while문 이용하기

#앞부분은 동일
driver=webdriver.Chrome(ChromeDriverManager().install())
url="https://www.instagram.com"
driver.get(url)

email="내아이디"
input_id=driver.find_elements_by_css_selector("input._2hvTZ.pexuQ.zyHYP")[0]
input_id.send_keys(email)
password='내비밀번호'
input_pw=driver.find_elements_by_css_selector("input._2hvTZ.pexuQ.zyHYP")[1]
input_pw.send_keys(password)
input_pw.submit() #입력
time.sleep(2) #대기

word=input("검색어: ") #원하는 검색어 입력
driver.get("https://www.instagram.com/explore/tags/"+word)
time.sleep(5)
#첫번째 게시글 열기
first=driver.find_element_by_css_selector("div._9AhH0")
first.click()
time.sleep(2)

insta_dict = {'id':[],
            'date':[],
            'like':[],
            'text':[],
            'hashtag':[]}

#.find_element_by_css_name VS .find_elements_by_css_name
#단수와 복수 차이를 이해해야한다.
#동일한 css값이 있다면 복수의 함수를 이용해야 한다.(find_elements_)
#단 요소값이 여러개이므로 리스트 형태로 반환됨에 유의해야 한다. 리스트 형태를 바로 사용하기는 여러 error가 발생할 수 있기에
#인덱스 추출 방식으로 이용한다.

seq = 0
start = time.time()

while True:
    try:
        if driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow'):
            if seq % 20 == 0:
                print('{}번째 수집 중'.format(seq), time.time() - start, sep='\t')

            ## id 정보 수집
            try:
                info_id = driver.find_element_by_css_selector('h2._6lAjh').text
                insta_dict['id'].append(info_id)
            except:
                info_id = driver.find_element_by_css_selector('div.C4VMK').text.split()[0]
                insta_dict['id'].append(info_id)

            ## 시간정보 수집
            time_raw = driver.find_element_by_css_selector('time.FH9sR.Nzb55')
            time_info = pd.to_datetime(time_raw.get_attribute('datetime')).normalize()
            insta_dict['date'].append(time_info)

            ## like 정보 수집
            try:
                driver.find_element_by_css_selector('button.sqdOP.yWX7d._8A5w5')
                like = driver.find_element_by_css_selector('button.sqdOP.yWX7d._8A5w5').text
                insta_dict['like'].append(like)

            except:
                insta_dict['like'].append('영상')

            ##text 정보수집
            raw_info = driver.find_element_by_css_selector('div.C4VMK').text.split()
            text = []
            for i in range(len(raw_info)):
                ## 첫번째 text는 아이디니까 제외
                if i == 0:
                    pass
                ## 두번째부터 시작
                else:
                    if '#' in raw_info[i]:
                        pass
                    else:
                        text.append(raw_info[i])
            clean_text = ' '.join(text)
            insta_dict['text'].append(clean_text)

            ##hashtag 수집
            raw_tags = driver.find_elements_by_css_selector('a.xil3i')
            hash_tag = []
            for i in range(len(raw_tags)):
                if raw_tags[i].text == '':
                    pass
                else:
                    hash_tag.append(raw_tags[i].text)

            insta_dict['hashtag'].append(hash_tag)

            seq += 1

            if seq == 100:
                break

            driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()
            time.sleep(1.5)


        else:
            break

        except:
        driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()
        time.sleep(2)


#코드의 논리 핵심은 try-except이다
#dictionary 형태에서 dataframe형태로 전환 시 가장 중요한 값은 키에서 저장하는 밸류 값들의 길이가 모두 같아야 한다는 것
#그래서 원하는 정보가 없더라도 그냥 패스하면 안되고, null값 지정하거나 별도로 특정 값을 부여하여 value의 길이를 맞춰줘야 한다
#크롤링을 할 때 가장 중요한 것은
#지금 어느 정도의 단계인지 표시하고 성능을 테스트하는 것이다.
#안 할 시 로딩시간이 매우 길어질 수 있다.

#딕셔너리를 데이터프레임 형태로 정리하기
#pd.DataFrame.from_dict()


# 1. 모듈설치
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
# 주소 부여
# 1. 신문사 스크래핑
url = "https://www.hankyung.com/all-news/economy"
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


# 보기를 원하는 날짜 입력&원하는 뉴스 개수 입력
def get_date(start, end, page):
    return "https://www.hankyung.com/all-news/economy?sdate={}&edate={}&page={}".format(start, end, page)


start, end = input("yyyy.mm.dd-yyyy.mm.dd 시작과 종료날짜 입력: ").split('-')
page_num = int(input("몇 페이지까지 출력하시겠습니까?: "))
total_news = {}
titleList = [];
linkList = [];
contentList = [];
for page in range(1, page_num + 1):
    # 1.검색 페이지 이동
    url = url = get_date(start, end, page)
    driver.get(url)
    # 페이지 로딩 시간이 필요하므로 2초 딜레이
    time.sleep(2)
    print("현재 스크래핑 작업중인 페이지 번호 : ", page)
    # 2.로드된 페이지의 html 태그 읽어오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 현재 페이지의 기사들 가져오기
    news_list = soup.select('ul.article_list>li')  # 페이지 내 기사들

    for i in range(len(news_list)):
        title = soup.select('ul.article_list> li> div > h3.tit')[i].text  # 기사 제목과 링크 리스트
        link = soup.select('ul.article_list> li> div > h3.tit> a')[i].attrs['href']
        content = soup.select('ul.article_list> li> div >p.read')[i].text  # 기사 내용 리스트
        titleList.append(title);
        linkList.append(link);
        contentList.append(content)
news = list(zip(titleList, linkList, contentList))
df = pd.DataFrame(news)
df.to_excel("economicnews.xlsx", index=False)

