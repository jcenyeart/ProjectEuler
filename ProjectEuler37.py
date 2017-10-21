import timeit
start = timeit.default_timer()


#ProjectEuler37

from itertools import *
from math import *

#test if a number is prime
def primetest(n):
  if all(n%d != 0 for d in range(2,int(ceil(sqrt(n)+1)))):
    return True
  else: 
    return False

a = ['2','3','5','7']
mids = 1379
z = ['3','7']
primes = 4
length = 1
length2 = length + 2
truncprime = ['23','37','53','73']

while primes < 11:
  
  l = list(product(str(mids), repeat=length))
  for i in range(0,len(l)):
    l[i] = ''.join(l[i])
  col = []
  
  for A in a:
    for B in l:
      for C in z:
        cand = A + B + C
        col.append(cand)
        
  for ele in col:
    if all(primetest(int(ele[:d+1])) for d in range(0, length2)) and all(primetest(int(ele[(-1)*d:])) for d in range(1,length2+1)):
      primes = primes +1
      truncprime.append(ele)
      
  length = length + 1
  length2 = length + 2

print(truncprime)
sum = 0
for ele in truncprime:
  sum = sum + int(ele)
  
print(sum)

stop = timeit.default_timer()
print stop - start