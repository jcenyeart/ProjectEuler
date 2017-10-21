#ProjectEuler29

pows = set([])

for a in range(2,101):
  for b in range(2,101):
    pows.add(a**b)
print(len(pows))