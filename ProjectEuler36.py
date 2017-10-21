import timeit
start = timeit.default_timer()

paltwo = []
palten = []

def palincheck(n):
  a = n
  b = str(a)
  c = len(b)
  if c%2 == 1 and all(b[i] == b[c-1-i] for i in range(0,(c-1)/2+1)):
    return True
  elif c%2 == 0 and all(b[i] == b[c-1-i] for i in range(0,c/2+1)):
    return True
  else:
    return False
  
for i in range(1,1000000):
  if palincheck(i):
    palten.append(i)
    
for ele in palten:
  a = "{0:b}".format(ele)
  if palincheck(int(a)):
    paltwo.append(ele)
  
print(len(palten))
print(len(paltwo))
print(paltwo)
print(sum(paltwo))

stop = timeit.default_timer()
print stop - start