# selenium에서 webdriver를 사용할 수 있게 webdriver를 import 한다.
from selenium import webdriver
# BeautifulSoup4를 import 한다.
from bs4 import BeautifulSoup
# 날짜 시간 처리 위해 datetime, timedelta를 import 한다.
from datetime import datetime, timedelta
# iframe TAG 작성을 위해 yt를 import 한다. (pip install yt-iframe)
from yt_iframe import yt 

# <p>제목</p><p><a>URL</a></p><p><iframe></p> 로 작성

# 14F 일사에프 https://www.youtube.com/channel/UCLKuglhGlMmDteQKoniENIQ
# Kurzgesagt – In a Nutshell https://www.youtube.com/channel/UCsXVk37bltHxD1rDPwtNM8Q
# TED-Ed https://www.youtube.com/channel/UCsooa4yRKGN_zEE8iknghZA
# Vox https://www.youtube.com/channel/UCLXo7UDZvByw2ixzpQCufnA
# LG전자 https://www.youtube.com/channel/UCrIAnDo3VuWex3fywkGpB1g
# LG https://www.youtube.com/channel/UC4SaZQMdD97YEjs26kSHn9w
# 디즈니 https://www.youtube.com/channel/UCbv7Dcn5iNrAyd3GwgVHkIQ
# MarvelKorea https://www.youtube.com/channel/UCSB5FOwUVnAhGo_o99IhxYA
# 리뷰엉이: Owl's Review https://www.youtube.com/channel/UCrBpV_pG2kyMMEHCMTNzjAQ
# movie trip 무비트립 https://www.youtube.com/channel/UCpr2S3SBmyjvrx9Q4pLUZHw
# 고몽 https://www.youtube.com/channel/UCpcft4FJXgUjnxWoQYsl7Ug
# 천재이승국 GeniusSKLee https://www.youtube.com/channel/UCu3BjLd03jxTVHXTPqZ77iQ
# 은빛유니콘 https://www.youtube.com/channel/UCPq0i_bZeqVoVYm_u8qimDA
# 엔스Ens https://www.youtube.com/channel/UC_Aly3X5CdojHdRDGmKi1ow
# 가전주부 GJJB https://www.youtube.com/channel/UC5aNQ65ADb02zEJxzb_zmYQ
# 멋진기영TV https://www.youtube.com/channel/UCl8OVxF0iHY3uFEgXz9w00g
# B Man 삐맨 https://www.youtube.com/channel/UCxlv4aOnrRTXMRSL8bVJqEw
# 빨강도깨비 https://www.youtube.com/channel/UCKNdfTZCJuOQfWN5Pe5UAAQ
# 발없는새 https://www.youtube.com/channel/UCiOWYRzOTiUYi9pJ-kscIKw
# sanggung상궁 https://www.youtube.com/channel/UCZUjLw9C0Tt3VECAhQO9buA
# 엉삼 https://www.youtube.com/channel/UCu1jlal8cou2kEUK9lycRWg
# 오토뷰(Autoview) https://www.youtube.com/channel/UCfcgDLazgMa1L92Kl3r9ZAA
# 한상기 오토프레스 Han Sang Ki https://www.youtube.com/channel/UC-IBt8pM8hWx8wiwjcDLdIQ
# LikeRing https://www.youtube.com/channel/UC7A1QdDXcu3zu_KS8DddL1A
# 사람사는세상노무현재단 https://www.youtube.com/channel/UCJS9VvReVkplPwCIbxnbsjQ

# 전일 오전 7시
yesterday = datetime.today() - timedelta(days=1)
fromdate = datetime(yesterday.year, yesterday.month, yesterday.day, 7, 0, 0)

# 당일 오전 6시 59분 59초
todate = datetime(datetime.today().year, datetime.today().month, datetime.today().day, 6, 59, 59)

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
time = [all_time[n].text for n in range(1,len(all_time),2)]


width = '560' # (Optional)
height = '315' # (Optional)
finalurl ='' # 임시

utubeKey = ""       # 유튜브 키값 초기화
utubeKeyIndex = 0   # 유튜브 키 체크값 초기화
finalurl = ""       # url 초기화

utubeKey = firsturl[utubeKeyIndex + 9 : utubeKeyIndex + 9 + 11]
# url = 'https://www.youtube.com/watch?v=' + utubeKey

# iframe = yt.video(url, width=width, height=height)

print(str(len(all_title)))
print(title)
print(str(len(all_url)))
print(firsturl)
print(str(len(all_time)))
print(time)

# webdriver를 종료한다.
driver.close()