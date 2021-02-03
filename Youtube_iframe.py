from yt_iframe import yt # pip install yt-iframe
from datetime import datetime, timedelta

# iframe TAG 생성할 유튜브 채널들 동영상 중 
# 전일 오전 7시 ~ 당일 오전 6시 59분 59초 해당할 경우
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


testurl = 'https://youtu.be/Pi9dzHkdTiA'                                 # (Required)
# testurl = 'https://youtube.com/watch?v=Pi9dzHkdTiA&feature=youtu.be'     # (Required)
# testurl = 'https://www.youtube.com/watch?v=Pi9dzHkdTiA&feature=youtu.be' # (Required)

width = '560' # (Optional)
height = '315' # (Optional)

utubeShrotUrlIndex  = testurl.find('https://youtu.be/')                  # 유튜브 짧은 주소는 길게 변경 필요
utubeUrlIndex       = testurl.find('https://youtube.com/watch?v=')       # 유튜브 긴 주소는 Video ID만 추출
utubewwwUrlIndex    = testurl.find('https://www.youtube.com/watch?v=')   # 유튜브 www 긴 주소는 Video ID만 추출

utubeKey = ""       # 유튜브 키값 초기화
utubeKeyIndex = 0   # 유튜브 키 체크값 초기화
url = ""            # url 초기화

# 전일 오전 7시
yesterday = datetime.today() - timedelta(days=1)
fromdate = datetime(yesterday.year, yesterday.month, yesterday.day, 7, 0, 0)

# 당일 오전 6시 59분 59초
todate = datetime(datetime.today().year, datetime.today().month, datetime.today().day, 6, 59, 59)


if utubeShrotUrlIndex >= 0:
    utubeKeyIndex = testurl.find('https://youtu.be/')
    utubeKey = testurl[utubeKeyIndex + 17 : utubeKeyIndex + 17 + 11]
    url = 'https://www.youtube.com/watch?v=' + utubeKey
elif utubeUrlIndex >= 0:
    utubeKeyIndex = testurl.find('https://youtube.com/watch?v=')
    utubeKey = testurl[utubeKeyIndex + 28 : utubeKeyIndex + 28 + 11]
    url = 'https://www.youtube.com/watch?v=' + utubeKey
elif utubewwwUrlIndex >= 0:
    utubeKeyIndex = testurl.find('https://www.youtube.com/watch?v=')
    utubeKey = testurl[utubeKeyIndex + 32 : utubeKeyIndex + 32 + 11]
    url = 'https://www.youtube.com/watch?v=' + utubeKey
else:
    url = testurl

iframe = yt.video(url, width=width, height=height)

print(iframe)