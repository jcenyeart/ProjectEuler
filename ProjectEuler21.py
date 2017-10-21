import timeit

start = timeit.default_timer()


sumfactor = [0,0]
for i in range(2,10000):
  factors = []
  sum = 0
  for j in range (1,i):
    if i%j == 0:
      factors.append(j)
  for ele in factors:
    sum = sum + ele
  sumfactor.append(sum)    
  
print(len(sumfactor)) 
  
amicable = []  
for k in range(2,10000):
  if sumfactor[k] < 10000 and k != sumfactor[k]:
	  if sumfactor[sumfactor[k]] == k:
		  amicable.append(k)
		  amicable.append(sumfactor[k])
  
print(amicable)

amisum = 0
for eles in amicable:
  amisum = amisum + eles
  
amisum = amisum/2
print(amisum)

stop = timeit.default_timer()

print stop - start