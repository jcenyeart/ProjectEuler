#Project Euler 38

import timeit
start = timeit.default_timer()

check = ['1','2','3','4','5','6','7','8','9']
pandig = []
s = 8999
C = 0

while s < 10000:
  st = ''
  s = s + 1
  i = 1
  while len(st) < 9:
    st = st + str(i*s)
    i = i + 1  
  coll = sorted(st)
  if coll == check:
    pandig.append(st)

print(pandig)

stop = timeit.default_timer()
print stop - start