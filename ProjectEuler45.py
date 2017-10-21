#Project Euler 45

import timeit
start = timeit.default_timer()

t = []
p = []
h = []

for i in range(1,100000):
  t.append(i*(i+1)/2)
  p.append(i*(3*i-1)/2)
  h.append(i*(2*i-1))
  
T = set()
P = set()
H = set()

T.update(t)
P.update(p)
H.update(h)

print(T & P & H)

stop = timeit.default_timer()
print stop - start