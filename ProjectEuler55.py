#Project Euler 55

from itertools import *
from math import *

import timeit
start = timeit.default_timer()


def palincheck(n):
  a = n
  b = str(a)
  c = len(b)
  if c%2 == 1 and all(b[i] == b[c-1-i] for i in range(0,(c-1)/2+1)):
    return True
  elif c%2 == 0 and all(b[i] == b[c-1-i] for i in range(0,c/2+1)):
    return True
  else:
    return False

def reversing(n):
  a = n
  b1 = ''
  b2 = str(a)
  c = len(b2)
  for i in range(0, c):
    b1 = b1 + b2[(-1)*(i+1)]
  return b1
  
countcount = 0  
for i in range(1,10000):
  inter = i
  inter = inter + int(reversing(inter))
  count = 0
  while not palincheck(inter) and count < 51:
    inter = inter + int(reversing(inter))
    count = count + 1
  if count == 51:
    countcount += 1
print(countcount)

stop = timeit.default_timer()
print stop - start