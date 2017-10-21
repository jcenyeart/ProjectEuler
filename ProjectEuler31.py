#ProjectEuler31
#Bottom-Up approach
import timeit
start = timeit.default_timer()

goal = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*goal

for ele in coins:
    for i in range(ele, goal+1):
        ways[i] += ways[i-ele]

print ways[goal]
stop = timeit.default_timer()
print stop - start