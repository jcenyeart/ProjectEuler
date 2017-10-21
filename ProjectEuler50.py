#Project Euler 50

import timeit
start = timeit.default_timer()

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

sumtot = 0
list = []
colle = []
def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            list.append(i)
            multiples.update(range(i*i, n+1, i))
    return(list)
    
colle = eratosthenes2(1000000)
length = 0

for ind in range(0,len(colle)):
	sum = 0 
	i = ind

	while sum < colle[-1]:
		sum = sum + colle[i]
		i = i + 1
	i = i - 1
	sum = sum - colle[i]  

	while not isPrime(sum):
		i = i - 1
		sum = sum - colle[i]

	if (i-ind) >= length:
	  length = i-ind
	  sumtot = sum

	
sum3 = 0	  
for i in range(3,546):
  sum3 = sum3 + colle[i]
print(sum3)  
stop = timeit.default_timer()
print stop - start