# This is Lotto numbering program made by Suh, Changsoo.

print('Lotto')

import random

lotto=[]

a=random.choices(range(1,46))

b=a[0]

for i in range(6):

      while b in lotto:

              a=random.choices(range(1,46))

              b=a[0]

      lotto.append(b)

lotto.sort()

print(lotto)