import timeit

start = timeit.default_timer()



#ProjectEuler34
count = 0
nums = []

def fact(n):
  product = 1
  for i in range(1,n+1):
    product = product*i
  return product

for i in range(10,3000000):
  string = str(i)
  sum = 0
  for j in range(0,len(string)):
    sum = sum + fact(int(string[j]))
  if sum == i:
    count = count + 1
    nums.append(i)

print(nums)

stop = timeit.default_timer()

print stop - start