import requests
import pandas as pd
from bs4 import BeautifulSoup

# 
url = ['https://www.youtube.com/user/JTBC10news/videos']
# url = ['https://www.youtube.com/user/JTBC10news/videos', 'https://www.youtube.com/c/14FMBC/videos']
headers = {'User-Agent': 'Mozilla/5.0'}                             # 봇 방지 웹사이트 회피

# 정해진 유튜브 채널의 동영상 탭 내 정해진 날짜 시간을 만족하는 동영상 제목과 Iframe Tag를 생성하는 프로그램

res = requests.get(url[0], headers=headers)

if res.status_code == 200:
    # 응답 html코드를 text로 변환
    html = res.text

    # 응답받은 html코드를 BeautifulSoup에 사용하기 위하여 인스턴스 지정
    soup = BeautifulSoup(html, 'html.parser')

    # tbody 에 필요한 게시글 목록이 있어 해당 영역 가져오기 처리
    youtubebody = soup.select('#primary > ytd-section-list-renderer')

    print(len(youtubebody))
else:
        print(">>>> Youtube GET ERROR.....")



# print(url[0])
# print(url[1])