#Project Euler 65

#String Representation of 'e'



import timeit
start = timeit.default_timer()

from math import *
from fractions import *
from decimal import *

a = [2,1]
i = 1

while len(a) < 100:
  a.append(2*i)
  a.append(1)
  a.append(1)
  i = i+1

a = a[:100]
b = []
b.append(2)
b.append(3)

while len(b) < 100:
    b.append(b[-1]*a[len(b)]+b[-2])  #Recusion that Num_n = a_n*Num_(n-1) + Num(n-2)
print sum(map(int,str(b[-1])))
	     
# def StC(a):
	# b = float(1)/a[-1]
	# for i in range(2,len(a)):
		# b = 1/(a[-i]+b)
	# return(a[0] + b)

stop = timeit.default_timer()
print stop - start