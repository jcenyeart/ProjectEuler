#Project Euler 63
count = 0
for j in range(2,10):
	for i in range(0,100):
		print (i,len(str(j**i)))
		if len(str(j**i)) == i:
			count = count + 1

print count
