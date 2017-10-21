#Project Euler 79

pcodes = [319,
680,
180,
690,
129,
620,
762,
689,
762,
318,
368,
710,
720,
710,
629,
168,
160,
689,
716,
731,
736,
729,
316,
729,
729,
710,
769,
290,
719,
680,
318,
389,
162,
289,
162,
718,
729,
319,
790,
680,
890,
362,
319,
760,
316,
729,
380,
319,
728,
716,
]

print pcodes

rels = set()

for ele in pcodes:
  rels.add((str(ele)[0],str(ele)[1]))
  rels.add((str(ele)[1],str(ele)[2]))
  rels.add((str(ele)[0],str(ele)[2]))
  
digs = set ()

for ele in pcodes:
  digs.add(str(ele)[0])
  digs.add(str(ele)[1])
  digs.add(str(ele)[2])

coll = list(rels)
print(coll)

counts = []
for ele in coll:
  counts.append(ele[0])

print counts

for ele in digs:
  print(ele, counts.count(ele))
  
correct = list(reversed(sorted(digs, key = counts.count)))

string = ''

for ele in correct:
  string = string + ele

print string
