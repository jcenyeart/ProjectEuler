sequence = [1,1,2,3,5,8]

def add_next(sequence):
	suma = sequence[-1] + sequence[-2]
	sequence.append(suma)
	return sequence

while len(str(sequence[-1])) != 1000:
	sequence = add_next(sequence)

print len(sequence)