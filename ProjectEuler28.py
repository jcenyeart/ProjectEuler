import timeit
start = timeit.default_timer()

#Constructive Approach to Spirals
r = range(1,1001**2+1)
sum = 1
for i in range(1,501):
  cyclelength = (2*i+1)**2-(2*i-1)**2
  for j in range(1,5):  
    sum = sum + r[(2*i-1)**2+(j*cyclelength)/4-1]
    
print(sum)



stop = timeit.default_timer()
print stop - start