#Project Euler 40	

from math import *
import timeit
start = timeit.default_timer()

r = ''
i = 1
while len(r) < 1000001:
  r = r + str(i)
  i = i + 1

sum = int(r[1-1]) * int(r[10-1]) * int(r[100-1]) * int(r[1000-1]) * int(r[10000-1]) * int(r[100000-1]) * int(r[1000000-1])

print(sum)


stop = timeit.default_timer()
print stop - start