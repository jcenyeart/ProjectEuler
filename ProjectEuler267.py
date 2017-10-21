#Project Euler 267

from math import *

norm = float(2**1000)

sum = 0

for i in range(432,1001):
  sum = sum + factorial(1000)/(factorial(i)*factorial(1000-i))
  
f = float(sum)

F = f/norm

print(F)