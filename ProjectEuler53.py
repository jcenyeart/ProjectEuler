#Project Euler 53

from math import *
from itertools import *

import timeit
start = timeit.default_timer()

tally = 0
for i in range(1,101):
  for j in range(0,i+1):
    check = factorial(i)/factorial(j)/factorial(i-j)
    if check > 1000000:
      tally = tally + (i+1) - 2*j
      print(i,j)
      print(tally)
      break

print(tally)




stop = timeit.default_timer()
print stop - start
 

