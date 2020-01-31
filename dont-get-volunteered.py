from sys import argv

def whereAmI(pos):
	x = pos % 8
	y = pos // 8
	return x, y
	
def iAmHere(x, y):
	return y * 8 + x
	
def conquer(e, set_conquering, set_conquered):
	if e not in set_conquered:
		set_conquered.add(e)
		set_conquering.add(e)

def yellCharge(s, set_conquered):
	x, y = whereAmI(s)
	set_conquering = set()
	if y > 1:
		if x > 0:
			#up-left
			e = iAmHere(x - 1, y - 2)
			conquer(e, set_conquering, set_conquered)
		if x < 7:
			#up-right
			e = iAmHere(x + 1, y - 2)
			conquer(e, set_conquering, set_conquered)
	if y > 0:
		if x > 1:
			#left-up
			e = iAmHere(x - 2 , y - 1)
			conquer(e, set_conquering, set_conquered)
		if x < 6:
			#right-up
			e = iAmHere(x + 2, y - 1)
			conquer(e, set_conquering, set_conquered)
	if y < 7:
		if x > 1:
			#left-down
			e = iAmHere(x - 2, y + 1)
			conquer(e, set_conquering, set_conquered)
		if x < 6:
			#right-down
			e = iAmHere(x + 2, y + 1)
			conquer(e, set_conquering, set_conquered)
	if y < 6:
		if x > 0:
			#down-left
			e = iAmHere(x - 1, y + 2)
			conquer(e, set_conquering, set_conquered)
		if x < 7:
			#down-right
			e = iAmHere(x + 1, y + 2)
			conquer(e, set_conquering, set_conquered)
	return set_conquering

def solution(src, dest):
	set_conquered = {src}
	set_conquering = {src}
	i = 0
	while len(set_conquering) > 0:
		tmp_set = set()
		i += 1
		for p in set_conquering:
			tmp_set = tmp_set | yellCharge(p, set_conquered)
			if dest in tmp_set:
				return i
			set_conquering = tmp_set
	return 0

print(solution(int(argv[1]), int(argv[2])))