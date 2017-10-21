#Project Euler 62
listofcubes = []
slistofcubes = []

for i in range(0,10000):
  listofcubes.append(i**3)
  
for ele in listofcubes:
  scube = []
  for i in range(0, len(str(ele))):
    scube.append(str(ele)[i])
  slistofcubes.append(sorted(scube))

L = sorted(slistofcubes, key = slistofcubes.count, reverse = True)

sol = L[0]
print sol

for ele in listofcubes:
  scube = []
  for i in range(0, len(str(ele))):
    scube.append(str(ele)[i])
  if sorted(scube) == sol:
    print(ele)
    
Extension = []
Lmod = []

for ele in L:
  if ele not in Lmod:
    Lmod.append(ele)

  
for ele in Lmod:
  Extension.append([ele,L.count(ele)])




