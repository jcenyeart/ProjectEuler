#Project Euler 43

import timeit
start = timeit.default_timer()

from itertools import *
primes = [2,3,5,7,11,13,17]
tally = []

perms = list(permutations('1234567890', 10))

for i in range(0, len(perms)):
  perms[i] = ''.join(perms[i])

perms = sorted(perms)
perms = perms[362880:]

for ele in perms:
  if all(int(ele[1+i:4+i])%primes[i] == 0 for i in range(0,7)):
    tally.append(int(ele))
    
print(tally)
print(sum(tally))



stop = timeit.default_timer()
print stop - start