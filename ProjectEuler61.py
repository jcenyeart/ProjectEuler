#Project Euler 61
import timeit
start = timeit.default_timer()


import copy


def Three(n):
  return n*(n+1)/2
 
def Four(n):
  return n*n
  
def Five(n):
  return n*(3*n-1)/2
  
def Six(n):
  return n*(2*n-1)
  
def Seven(n):
  return n*(5*n-3)/2
  
def Eight(n):
  return n*(3*n-2)
  
Threes = []
Fours = []
Fives = []
Sixs = []
Sevens = []
Eights = []  
  
for i in range(1,150):
  if Three(i)>999 and Three(i)<10000:
    Threes.append(Three(i))
  if Four(i)>999 and Four(i)<10000:
    Fours.append(Four(i))
  if Five(i)>999 and Five(i)<10000:
    Fives.append(Five(i))
  if Six(i)>999 and Six(i)<10000:
    Sixs.append(Six(i))
  if Seven(i)>999 and Seven(i)<10000:
    Sevens.append(Seven(i))
  if Eight(i)>999 and Eight(i)<10000:
    Eights.append(Eight(i))

alltogether = []
alltogether.append(Threes)
alltogether.append(Fours)
alltogether.append(Fives)
alltogether.append(Sixs)
alltogether.append(Sevens)
alltogether.append(Eights)


def masterf(n):
  totallist = []
  for N in n:
		newlist = []
		#n will be a list, or collection of lists of the form [#,#,#,subset]
		digits = str(N[-2])[-2:]
		for i in N[-1]:
			for ele in alltogether[i]:
				m = copy.deepcopy(N)
				if str(ele)[0:2] == digits:
					m.insert(-1,ele)
					m[-1].remove(i)
					newlist.append(m)
		if newlist:
		  for ele in newlist:
			  totallist.append(ele)
  return totallist
sum = 0
for eles in Threes:
  starter = [[eles,[1,2,3,4,5]]]
  fin = masterf(masterf(masterf(masterf(masterf(starter)))))
  if len(fin) > 0:
    for ele in fin:
      if str(ele[0])[0:2] == str(ele[5])[-2:]:
        print ele
        for i in range(0,6):
          sum = sum + ele[i]
        print sum
  
stop = timeit.default_timer()
print stop - start