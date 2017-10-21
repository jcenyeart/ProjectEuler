#Project Euler 47

import timeit
from math import *
start = timeit.default_timer()

s = 3
c = 0

def primefact(n):
  d = 2
  primefac = []
  while d*d <= n:
    while (n % d) == 0:
      primefac.append(d)
      n /= d
    d = d +1
  if n > 1:
    primefac.append(n)
  return primefac
    
while c < 4:
  s = s + 1
  if len(set(primefact(s))) == 4:
    c = c + 1
  else:
    c = 0  
    
print(s-3)

stop = timeit.default_timer()
print stop - start