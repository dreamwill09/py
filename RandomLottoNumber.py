print('Lotto')

# random을 import 한다.
import random

# 횟수를 입력 받음
count = int(input("로또 번호를 몇개 생성할까요?> "))

sumlotto = []
no = []

for m in range(count):

      lotto = []      

      # 1 ~ 45 중에서 랜덤 생성
      a=random.choices(range(1,46))

      b=a[0]

      for i in range(6):

            while b in lotto:

                  a=random.choices(range(1,46))

                  b=a[0]

            lotto.append(b)

      # 로또 번호를 sort
      lotto.sort()

      # 생성된 로또 번호를 누적
      sumlotto += lotto

print(sumlotto)

# 1번 ~ 45번까지 빈도를 count
for c in range(1,45+1):
      no.append(sumlotto.count(c))

# 1번 ~ 45번까지 빈도를 print
for d in range(0,44+1):
      print(str(d+1) + " : " + str(no[d]))
