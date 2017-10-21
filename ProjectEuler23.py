#Finding the factors of integers < 28123:

import timeit

start = timeit.default_timer()


abundants = []
sumfact = 0
for i in range(10,28124):
  factors = []
  for j in range(1,i/2 +1):
    if i%j == 0:
      factors.append(j)
  sumfact = sum(factors)
  if sumfact > i:
    abundants.append(i)
    
#now we have a list of the abundant integers < 28123
#want to compile a list of all integers < 28123 that are NOT represented as
#a sum of two abundant integers

intlist = []
sumlist = []

for ele in range(1,28124):
  intlist.append(ele)


for i in abundants:
  for j in abundants:
    sum = i + j
    if sum < 28124:
      sumlist.append(sum)
    
sumlist = sorted(sumlist)
sumlist = list(set(sumlist))    


for ele in sumlist:
  intlist.remove(ele)

sum2 = 0 
for element in intlist:
  sum2 = sum2 + element

print(sum2)  

stop = timeit.default_timer()

print stop - start