# selenium에서 webdriver를 사용할 수 있게 webdriver를 import 한다.
from selenium import webdriver
# BeautifulSoup4를 import 한다.
from bs4 import BeautifulSoup
# 날짜 시간 처리 위해 datetime, timedelta를 import 한다.
from datetime import datetime, timedelta
# iframe TAG 작성을 위해 yt를 import 한다. (pip install yt-iframe)
from yt_iframe import yt 
# 월, 년 단위 계산 위해서 relativedelta를 import 한다.
from dateutil.relativedelta import relativedelta

# <p>제목</p><p><a>URL</a></p><p><iframe></p> 로 작성

# 14F 일사에프 https://www.youtube.com/c/14FMBC/videos
# Kurzgesagt – In a Nutshell https://www.youtube.com/c/inanutshell/videos
# TED-Ed https://www.youtube.com/teded/videos
# Vox https://www.youtube.com/c/Vox/videos
# LG전자 https://www.youtube.com/c/LGElectronicsKorea/videos
# LG https://www.youtube.com/user/LGSTORY/videos
# 디즈니 https://www.youtube.com/c/DisneyMovieKr/videos
# MarvelKorea https://www.youtube.com/c/MarvelKorea/videos
# 리뷰엉이: Owl's Review https://www.youtube.com/c/Owlsreview/videos
# movie trip 무비트립 https://www.youtube.com/c/movietrip%EB%AC%B4%EB%B9%84%ED%8A%B8%EB%A6%BD/videos
# 고몽 https://www.youtube.com/user/rladndgussla/videos
# 천재이승국 GeniusSKLee https://www.youtube.com/c/GeniusSKLee/videos
# 은빛유니콘 https://www.youtube.com/channel/UCPq0i_bZeqVoVYm_u8qimDA/videos
# 엔스Ens https://www.youtube.com/channel/UC_Aly3X5CdojHdRDGmKi1ow
# 가전주부 GJJB https://www.youtube.com/channel/UC5aNQ65ADb02zEJxzb_zmYQ/videos
# 멋진기영TV https://www.youtube.com/channel/UCl8OVxF0iHY3uFEgXz9w00g
# B Man 삐맨 https://www.youtube.com/c/BMan%EC%82%90%EB%A7%A8/videos
# 빨강도깨비 https://www.youtube.com/c/%EB%B9%A8%EA%B0%95%EB%8F%84%EA%B9%A8%EB%B9%84dokkebi/videos
# 발없는새 https://www.youtube.com/user/nofeetbird/videos
# sanggung상궁 https://www.youtube.com/c/sanggungtv/videos
# 엉삼 https://www.youtube.com/c/%EB%A6%AC%EB%B7%B0%EC%97%89%EC%9D%B4%EB%B6%81%EC%8A%A4/videos
# 오토뷰(Autoview) https://www.youtube.com/channel/UCfcgDLazgMa1L92Kl3r9ZAA/videos
# 한상기 오토프레스 Han Sang Ki https://www.youtube.com/c/%ED%95%9C%EC%83%81%EA%B8%B0HanSangKi/videos
# LikeRing https://www.youtube.com/channel/UC7A1QdDXcu3zu_KS8DddL1A/videos
# 사람사는세상노무현재단 https://www.youtube.com/c/%EC%82%AC%EB%9E%8C%EC%82%AC%EB%8A%94%EC%84%B8%EC%83%81%EB%85%B8%EB%AC%B4%ED%98%84%EC%9E%AC%EB%8B%A8/videos

# 전일 오전 7시
yesterday = datetime.today() - timedelta(days=1)
fromdate = datetime(yesterday.year, yesterday.month, yesterday.day, 7, 0, 0)

# 당일 오전 6시 59분 59초
todate = datetime(datetime.today().year, datetime.today().month, datetime.today().day, 6, 59, 59)

# writetime global 변수로 선언


# driver란 변수에 객체를 만들어 준다.
driver = webdriver.Chrome(executable_path='chromedriver')

# 원하는 사이트의 url을 입력하여 사이트를 연다.
driver.get('https://www.youtube.com/c/14FMBC/videos')

# body를 스크롤하기 위해 tagname이 body로 되어있는것을 추출합니다.
body = driver.find_element_by_tag_name('body')

# 로드 된 페이지 소스를 html이란 변수에 저장합니다.
html = driver.page_source

# html을 'lxml' parser를 사용하여 분석합니다.
soup = BeautifulSoup(html, 'lxml')

# title 조건에 맞는 모든 a 태그의 class들을 가져옵니다.
all_title = soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')

# title이란 변수에 저장합니다.
title = [soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')[n].string for n in range(0,len(all_title))]

# href 조건에 맞는 모든 a 태그의 id들을 가져옵니다.
all_url = soup.find_all('a', {'id':'video-title'})

# firsturl이란 변수에 저장합니다.
firsturl = [soup.find_all('a', {'id':'video-title'})[n].get('href') for n in range(0,len(all_url))]

# time 조건에 맞는 모든 span 태그의 class들을 가져옵니다. title, url의 2배수.
all_time = soup.find_all('span','style-scope ytd-grid-video-renderer')

# time이란 변수에 시간 정보(짝수)를 저장합니다.
# 분 전, 시간 전, 일 전, 주 전, 개월 전, 년 전
time = [all_time[n].text for n in range(1,len(all_time),2)]

for x in range(0, 29):

    global writetime
        
    delta = ''
    if '분' in time:
        # 분일 경우 작성 시간 확인
        timenumber = time[0:time.find('분')]
        writetime = datetime.today() - timedelta(minutes=int(timenumber))
    elif '시간' in time:
        # 시간일 경우 작성 시간 확인
        timenumber = time[0:time.find('시간')]
        writetime = datetime.today() - timedelta(hours=int(timenumber))
    elif '일' in time:
        # 일일 경우 작성 시간 확인
        timenumber = time[0:time.find('일')]
        writetime = datetime.today() - timedelta(days=int(timenumber))
    elif '주' in time:
        # 주일 경우 작성 시간 확인
        timenumber = time[0:time.find('주')]
        writetime = datetime.today() - timedelta(weeks=int(timenumber))
    elif '개월' in time:
        # 개월일 경우 작성 시간 확인
        timenumber = time[0:time.find('개월')]
        delta = relativedelta(months=int(timenumber))
        writetime = datetime.today() - delta
    elif '년' in time:
        # 년일 경우 작성 시간 확인
        timenumber = time[0:time.find('년')]
        delta = relativedelta(years=int(timenumber))
        writetime = datetime.today() - delta

# print(str(writetime))

width = '560' # (Optional)
height = '315' # (Optional)
finalurl ='' # 임시

utubeKey = ""       # 유튜브 키값 초기화
utubeKeyIndex = 0   # 유튜브 키 체크값 초기화
finalurl = ""       # url 초기화

utubeKey = firsturl[utubeKeyIndex + 9 : utubeKeyIndex + 9 + 11]
# url = 'https://www.youtube.com/watch?v=' + utubeKey

# iframe = yt.video(url, width=width, height=height)

"""
print(str(len(all_title)))
print(title)
print(str(len(all_url)))
print(firsturl)
print(str(len(time)))
print(time)
"""

# webdriver를 종료한다.
driver.close()