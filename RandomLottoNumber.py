print('Lotto')

# random을 import 한다.
import random

from collections import Counter

# 횟수를 입력 받음
count = int(input("로또 번호를 몇 개 생성할까요?> "))

sumlotto = []
no = []
a = []
b = 0

for m in range(count):

      lotto = []

      for i in range(6):

            while b in lotto:

                  a=random.choices(range(1,46))

                  b=a[0]

            lotto.append(b)

      # 로또 번호를 sort
      lotto.sort()

      # 생성된 로또 번호를 누적
      sumlotto += lotto

# 원하는 만큼 생성된 로또 번호를 다 보여줍니다. 너무 많을 경우 파일로 저장하는 기능 만들기?
print(sumlotto)

# 리스트의 빈도를 구해주는 counter
frequency = Counter(sumlotto)

# 로또 번호별 빈도를 보여줍니다
print(frequency)