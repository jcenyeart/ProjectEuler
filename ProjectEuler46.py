#Project Euler 46

import timeit
from math import *
start = timeit.default_timer()

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
    
S = 9
C = 0

while C < 2:
  S = S + 2
  if not isPrime(S):
    if all(not isPrime(S - 2*i**2) for i in range(1, int(ceil(sqrt(S/2))))):
      print(S)
      C = C + 1

stop = timeit.default_timer()
print stop - start