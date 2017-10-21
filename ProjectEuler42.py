#Project Euler 42
letters2num = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, \
             'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, \
            'K': 11, 'L': 12, 'M': 13, 'N': 14, \
            'O': 15, 'P': 16, 'Q': 17, 'R': 18, \
            'S': 19, 'T': 20, 'U': 21, 'V': 22, \
            'W': 23, 'X': 24, 'Y': 25, 'Z': 26 \
            }
            
text_file = open("ProjectEuler42.txt", "r")
lines = text_file.read().split(',')
#print lines
print len(lines)
text_file.close()
lines = sorted(lines)

for i in range(0,len(lines)):
  lines[i] = lines[i][1:-1]

triangs = []
for i in range(1,30):
  triangs.append(i*(i+1)/2)

count = 0

for ele in lines:
  sum = 0
  for h in range(0,len(ele)):
    sum = sum + letters2num[ele[h]]
  if sum in triangs:  
    print(ele)
    print(sum)
    count += 1

print(count)

