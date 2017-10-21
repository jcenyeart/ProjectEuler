#Project Euler 41
from datetime import datetime
startTime = datetime.now()

list = []
check = ['1','2','3','4','5','6','7']

def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            list.append(i)
            multiples.update(range(i*i, n+1, i))
    return(list)
    
eratosthenes2(7654322)

list = reversed(list)

for ele in list:
  s = str(ele)
  if sorted(s) == check:
    print(s)
    break
            
print datetime.now() - startTime