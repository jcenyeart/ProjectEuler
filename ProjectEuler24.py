import timeit

start = timeit.default_timer()


#Building Permutations

p = []
p.append(str(0))
q = []
print(p)

for i in range(1,10):
	for ele in p:
		for j in range(0,len(ele)+1):
			h = str(i)
			new = ele[:j] + h + ele[j:]
			q.append(new)
	p = sorted(q)  
	q = []
print(len(p))	
print(p[999999])
stop = timeit.default_timer()

print stop - start