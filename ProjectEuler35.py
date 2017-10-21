#ProjectEuler35

from datetime import datetime
startTime = datetime.now()

nums = []
cycliclist = []


#Prime Generator/Finder
j = 1
i = 1
primelist = [2]
truncprimelist = []
import math

while i <1000000:
  i = i +2
  if all(i%d != 0 for d in range(2,int(math.ceil(math.sqrt(i)+1)))):
    primelist.append(i)
    
#Pretty slow, but works. Could introduce a check involving sqrt(primecandidate) to reduce times


#Rotation function
def rot(n):
  b = str(n)
  b = list(b)
  a = len(b)
  c = b[0]
  for i in range(0,a-1):
    b[i] = b[i+1]
  b[-1] = c
  b = int(''.join(b))
  return(b)

for ele in primelist:
  string = str(ele)
  z = list(string)
  if '0' in z or '2' in z or '5' in z or '4' in z or '6' in z or '8' in z:
    continue
  testlist = []
  test = ele
  for j in range(0,len(str(ele))-1):
    test =  rot(test)
    testlist.append(test)
  if all(i in primelist for i in testlist):
    cycliclist.append(ele)
    print(ele)

cycliclist.append(2)
cycliclist.append(5)
print(sorted(cycliclist))
print(len(cycliclist))

print datetime.now() - startTime