#Project Euler

import timeit
start = timeit.default_timer()

highace = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, \
           '9' : 9, '8' : 8, '7' : 7, '6' : 6, '5' : 5, \
           '4' : 4, '3' : 3, '2' : 2 \
           }

lowace = {'A': 1, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, \
           '9' : 9, '8' : 8, '7' : 7, '6' : 6, '5' : 5, \
           '4' : 4, '3' : 3, '2' : 2 \
           }     

handreader = {9 : 'straight flush', 8 : 'four of a kind'}      
        
#Poker Hierarchy:

#Straight Flush
#Four of a King
#Full House
#Flush
#Straight
#Three of a kind
#2 Pair
#One Pair
#High Card

text_file = open("ProjectEuler54b.txt", "r")
lines = text_file.read().split(',')
text_file.close()

lines2 = []

for i in range(0,len(lines)):
  lines[i] = lines[i].lstrip()
  lines2.append(lines[i])
  

handatot = []
handbtot = []

for i in range(0,1000):
  handa = []
  handb = []
  for j in range(10*i,10*i+5):
    handa.append(lines2[j])
    handb.append(lines2[j+5])
  handatot.append(handa)
  handbtot.append(handb)
  
#PointScoring Each Hand
#9 Possible Categories, assign 1-9

def isStraight(n):
  #n is a list of 5 elements, each element is a string of 2 chars
  col = []
  for i in range(0,5):
    col.append(n[i][0])
  if 'T' not in col and '5' not in col:
    return False  
  if 'T' in col:
    for i in range(0,5):
      col[i] = highace[col[i]]
    col = sorted(col)
    if all((col[i] == col[i+1]-1) for i in range(0,4)):
      col = list(reversed(col))
      col.insert(0,5)
      return col
    else:
      return False
  if '5' in col:
    for i in range(0,5):
      col[i] = lowace[col[i]]
    col = sorted(col)
    if all((col[i] == col[i+1]-1) for i in range(0,4)):
      col = list(reversed(col))
      col.insert(0,5)
      return col
    else:
      return False

def isFlush(n):
  #n is a list of 5 elements, each element is a string of 2 chars
  col = []
  for i in range(0,5):
    col.append(n[i][-1])
  b = col[0]
  if col.count(b) == 5:
    col = []
    for i in range(0,5):
      col.append(highace[n[i][0]])
      col = list(reversed(sorted(col)))
      col.insert(0,6)
      return col
  else:
    return False
  
def PairedHands(n):
  #n is a list of 5 elements, each element is a string of 2 chars
  col = []
  nums = []
  for i in range(0,5):
    col.append(highace[n[i][0]])
    col = sorted(col)
  for ele in col:
    nums.append(col.count(ele))
  nums = sorted(nums)
  if nums == [1,1,1,1,1]:
    return [1,col[4],col[3],col[2],col[1],col[0]]
  if nums == [1,1,1,2,2]:
    z = list(reversed(sorted(col, key=col.count)))
    z.insert(0,2)
    return z
  if nums == [1,2,2,2,2]:
    z = list(reversed(sorted(col,key=col.count)))
    z.insert(0,3)
    return z
  if nums == [1,1,3,3,3]:
    z = list(reversed(sorted(col, key=col.count)))
    z.insert(0,4)
    return z
  if nums == [2,2,3,3,3]:
    z = list(reversed(sorted(col, key=col.count)))
    z.insert(0,7)
    return z
  if nums == [1,4,4,4,4]:
    z = list(reversed(sorted(col, key=col.count)))
    z.insert(0,8)
    return z

ascore = []
bscore = []

for i in range(0,1000):

  if isFlush(handatot[i]) and isStraight(handatot[i]): 
    ascore = [9,15,15,15,15,15]
    continue
  if isFlush(handatot[i]):
    ascore.append(isFlush(handatot[i]))
    continue
  if isStraight(handatot[i]):
    ascore.append(isStraight(handatot[i]))
    continue
  if PairedHands(handatot[i]):
    ascore.append(PairedHands(handatot[i]))
    
for i in range(0,1000):
  if isFlush(handbtot[i]) and isStraight(handbtot[i]): 
    bscore = [9]
    continue
  if isFlush(handbtot[i]):
    bscore.append(isFlush(handbtot[i]))
    continue
  if isStraight(handbtot[i]):
    bscore.append(isStraight(handbtot[i]))
    continue
  if PairedHands(handbtot[i]):

    bscore.append(PairedHands(handbtot[i]))
  
#Comparing
awin = 0
bwin = 0
tie = 0

for i in range(0,1000):
  for j in range(0,6):
    if ascore[i][j] > bscore[i][j]:
      awin += 1
      break
    if ascore[i][j] < bscore[i][j]:
      bwin += 1
      break
    if ascore[i][j] == bscore[i][j]:
      if j == 5:
        tie += 1
        break
      continue
      
print(awin)
print(bwin)

def highcard(n):
  #n is a list of 5 elements, each element is a string of 2 chars
  col = []
  for i in range(0,5):
    col.append(highace[n[i][0]])
  col = sorted(col)
  return col

scores1 = [0,0,0,0,0,0,0,0,0]
for i in range(0,1000):
  ph = ascore[i][0]
  scores1[ph-1] = scores1[ph-1]+1



scores2 = [0,0,0,0,0,0,0,0,0]
for i in range(0,1000):
  ph = bscore[i][0]
  scores2[ph-1] = scores2[ph-1]+1



stop = timeit.default_timer()
print stop - start


#Testflush
#Teststraight
#Test4ofakind
#Testfullhouse
#Test3ofakind
#Test2pair
#Testpair


