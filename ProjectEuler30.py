#Project Euler 30

import timeit
start = timeit.default_timer()

sum = 0
for i in range(2,1000000):
  sumcheck = 0
  lt = 0
  string = str(i)
  lt = len(string)  
  for j in range(0,len(string)):
    sumcheck = sumcheck + int(string[j])**5
  if sumcheck == i:
    sum = sum + i
    print(i)
    
print(sum)

stop = timeit.default_timer()
print stop - start