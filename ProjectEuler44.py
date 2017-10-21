#Project Euler 43

import timeit
start = timeit.default_timer()

from itertools import *
from math import *

def penta(n):
  val = n*(3*n-1)/2
  return val
  
coll = [1]

a = 1
d = 0
c = 0

while c < 1:
  a += 1
  d += 2
  coll.append(penta(d))
  coll.append(penta(d+1))
  for b in range(1,a):
    if (penta(a)- penta(b)) in coll and (penta(a)+ penta(b)) in coll:
      c = 1
      print(penta(a))
      print(penta(b))

stop = timeit.default_timer()
print stop - start