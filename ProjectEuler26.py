#modular arithmetic as it relates to loops in fraction

import timeit

start = timeit.default_timer()

leng = []
for i in range(1,1000):
  mods = set(10**j%i for j in range(1,i))
  leng.append(len(mods))
  
print(sorted(leng)[-1])
  
stop = timeit.default_timer()

print stop - start