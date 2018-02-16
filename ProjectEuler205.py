from sympy import *

def DiceGame(a_min,a_max, b, c_min,c_max, d):
	'''
	a_min = minimum number on player 1's die
	a_max = maximum number on player 1's die
	b =     number of die player 1 has
	c_min = minimum number on player 2's die
	c_max = maximum number on player 2's die
	d =     number of die player 2 has
	'''
	a = range(a_min,a_max+1)
	c = range(c_min,c_max+1)

	x = Symbol('x')
	player_1_dist = dict(zip(range(a[0]*b,a[-1]*b+1), Poly(expand(sum(x**i for i in a)**b), x).coeffs()))
	player_2_dist = dict(zip(range(c[0]*d,c[-1]*d+1), Poly(expand(sum(x**i for i in c)**d), x).coeffs()))

	player_1_combos = sum(player_1_dist.values())
	player_2_combos = sum(player_2_dist.values())

	p_1_win = float(0)
	p_2_win = float(0)
	tie = float(0)
	for i in player_1_dist:
		for j in player_2_dist:
			p = player_1_dist[i]*player_2_dist[j]/(player_1_combos*player_2_combos)
			if i > j:
				p_1_win += p
			elif i == j:
				tie += p
			else:
				p_2_win += p


	return p_1_win, tie, p_2_win



# print "The probability of player 1 winning is " + str(DiceGame(1,4,9,1,6,6)[0])
# print "The probability of player 2 winning is " + str(DiceGame(1,4,9,1,6,6)[2])
# print "The probability of a tie is " + str(DiceGame(1,4,9,1,6,6)[1])

a,b,c = DiceGame(1,4,9,1,6,6)
print a
print b
print c




