#Project Euler 57	

import timeit
start = timeit.default_timer()

from math import *

a = [1,3]
b = [1,2]
c = []

while len(a) < 1000:
  a.append(2*a[-1] + a[-2])
  b.append(2*b[-1] + b[-2])

count = 0
for i in range(0,len(a)):
  if len(str(a[i])) > len(str(b[i])):
    count = count + 1

print(count)




#def a_n(n):
#  a = ((1+sqrt(2))/2)*(1+sqrt(2))**n + ((1-sqrt(2))/2)*(1-sqrt(2))**n
#  return a
  
#def b_n(n):
#  a = ((2+sqrt(2))/4)*(1+sqrt(2))**n + ((2-sqrt(2))/2)*(1-sqrt(2))**n
#  return a

stop = timeit.default_timer()
print stop - start