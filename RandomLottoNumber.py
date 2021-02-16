# This is Lotto numbering program made by Suh, Changsoo.

print('Lotto')

import random

count = int(input("로또 번호를 몇개 생성할까요?> "))

sumlotto = []
no = []

for m in range(count):

      lotto = []      

      a=random.choices(range(1,46))

      b=a[0]

      for i in range(6):

            while b in lotto:

                  a=random.choices(range(1,46))

                  b=a[0]

            lotto.append(b)

      lotto.sort()

      # print(str(m+1) + " : " + str(lotto))

      sumlotto += lotto

print(sumlotto)

# for c in range(1,45+1):
#       # print(str(c))
#       no1 = sumlotto.count(1)
#       print(str(c) + " : " + str(no[c]))