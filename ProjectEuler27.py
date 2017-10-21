import timeit
start = timeit.default_timer()

from math import *
primelist = []
ijlist = []

def poly(i,j,n):
  val = n**2+i*n+j
  return val

for i in range(-999,1000):
  for j in range(-999,1000):
    count = 0
    primes = 0
    n = 0
    while count < 1:
      a =  poly(i,j,n)
      if a > 1 and all(a%d != 0 for d in range(2, int(ceil(sqrt(a)+1)))):
        primes = primes + 1
        n = n+1
      else:
        count = 1
        primelist.append(primes)
        ijlist.append([i,j])
        
print (primelist.index(max(primelist)))
print (max(primelist))
print len(primelist)
print len(ijlist)
print ijlist[primelist.index(max(primelist))]

stop = timeit.default_timer()
print stop - start