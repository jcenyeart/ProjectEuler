#Project Euler 69b

import timeit
start = timeit.default_timer()

from math import *
from decimal import *

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
          if d not in primfac:
            primfac.append(d)  # supposing you want multiple factors repeated
          n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac
    
def totient(n):    
  product = 1
  for ele in primes(n):
    product = product*(1-Decimal(1)/ele)
  return (1/product)
  
max = 1
for i in range(1,510900):
  if totient(i) > max:
    print (i,totient(i))
    max = totient(i)
    
stop = timeit.default_timer()
print stop - start