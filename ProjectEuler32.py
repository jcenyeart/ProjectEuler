import timeit

start = timeit.default_timer()
#Building Permutations

p = []
p.append(str(1))
q = []
prods = set([])


for i in range(2,10):
	for ele in p:
		for j in range(0,len(ele)+1):
			h = str(i)
			new = ele[:j] + h + ele[j:]
			q.append(new)
	p = sorted(q)  
	q = []


for ele in p:
  for i in range(0,len(ele)-2):
    for j in range (0,len(ele)-i-2):
      inter = ele
      a = inter[:i+1]
      inter = inter[i+1:]
      b = inter[:j+1]
      inter = inter[j+1:]
      if int(a)*int(b) == int(inter):
        prods.add(int(inter))
      
print(sum(prods))

stop = timeit.default_timer()

print stop - start