#Project Euler 52

from itertools import *
from math import *

import timeit
start = timeit.default_timer()

a = list(permutations('124578',6))

for i in range(0,len(a)):
  a[i] = int(''.join(a[i]))
  
for i in range(0,len(a)):
  if (2*a[i] in a):
    print('2 times', a[i], 'is', 2*a[i])
    if (3*a[i] in a):
      if (4*a[i] in a):
        if (5*a[i] in a):
          if (6*a[i] in a):
            print('Winner')
            print(a[i])


stop = timeit.default_timer()
print stop - start
 