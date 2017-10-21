#Project Euler 49

import timeit
start = timeit.default_timer()


from itertools import *
from math import *

def eratosthenes2(n):
    list = []
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            list.append(i)
            multiples.update(range(i*i, n+1, i))
    return(list)
    
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True


a = eratosthenes2(10000)
a = a[168:]

b = []
for i in range(0,len(a)):
  d = []
  c = list(permutations(str(a[i]),4))
  for j in range(0,len(c)):
    c[j] = ''.join(c[j])
  c = set(c)  
  c = list(c)
  for ele in c:
    if ele[0] == '0' or isPrime(int(ele)) == False:
      d.append(ele)
  c = set(c)
  d = set(d)
  e = c-d
  e = list(e)    

  b.append(sorted(e)) 
  
b = sorted(b)

f = []

for i in range(0,len(b)):
  if f.count(b[i]) < 1:
    f.append(b[i])

h = []

for i in range(0,len(f)):
  if len(f[i]) >= 3:
    h.append(f[i])
    
winners = []
diffs = []
isos = []

for i in range(0,len(h)):
  accum = []
  for j in list(reversed(range(1,len(h[i])))):
    for k in list(reversed(range(0,j))):
      diff = int(h[i][j])-int(h[i][k])
      if diff in accum:
        winners.append(h[i])
        diffs.append(diff) 
      accum.append(diff)

for i in range(0,len(winners)):
  for j in list(reversed(range(0,len(winners[i])))):
    diff2 = int(winners[i][j]) - diffs[i]
    if str(diff2) in winners[i]:
      if str(diff2 - diffs[i]) in winners[i]:
        print winners[i]
      


print len(h)
print len(winners)  
print len(diffs)
     
stop = timeit.default_timer()
print stop - start
 