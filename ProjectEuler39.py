# Project Euler 39

from math import *
import timeit
start = timeit.default_timer()

check = 0
bestL = 0

for L in range(1,1000):
  coll = []
  for i in list(reversed(range(1,L))):
		for j in range(1,i):
			t = i**2 + j**2    
			if t == (L-i-j)**2:
				coll.append((i,j,int(sqrt(t))))
  if len(coll) > check:
    check = len(coll)
    bestL = L
    print(L)
    print(coll)
    print(len(coll))

stop = timeit.default_timer()
print stop - start