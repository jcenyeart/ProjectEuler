#ProjectEuler 48

import timeit
from math import *
start = timeit.default_timer()

print str(sum([i**i for i in range(1,1001)]))[-10:]

stop = timeit.default_timer()
print stop - start