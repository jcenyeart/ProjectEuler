#ProjectEuler33	

collect = []

for i in range(10,99):
  for j in range(i+1,100):
    a = float(i)/j
    c = str(i)
    d = str(j)
    e = int(c[0])
    f = int(d[1])
    if c[1] == d[0] and f != 0 and float(e)/f == a:
      collect.append([i,j,e,f])
      
print(collect)