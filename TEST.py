import re

temp = '<span class="style-scope ytd-grid-video-renderer">스트리밍 시간: 3주 전</span>'

number = re.findall("\d+", temp)

print(number[0])