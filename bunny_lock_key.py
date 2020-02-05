import operator as op
from functools import reduce

class CustomDic:
	def __init__(self, n):
		self.dic = {}
		self.count = n
		for i in range(n):
			self.dic[i] = 1

	def add(self, key):
		self.count += 1
		self.dic[key] += 1

def nCr(n, r):
    r = min(r, n - r)
    numerator = reduce(op.mul, range(n, n  -r, -1), 1)
    denominator = reduce(op.mul, range(1, r + 1), 1)
    return numerator / denominator

def solution(x, y):
	t = nCr(x, y)
	max_key_repeat = min(y, x - y + 1)
	dicos = []
	out = "	t : " + str(t) + "\n"
	for n in range(1, 11):
		if ((n - y) * max_key_repeat + y) / y >= 1:
			for k in range(n - y, (n - y) * max_key_repeat + 1):
				if (k + y) % y == 0:
					out += "	n : " + str(n)
					out += "	k : " + str(k + y) + "\n"
					
					# trouver le nombre de combinaisons de prendre k clef dans un ensemble de (n - y) clefs
					# avec au moins 1 clef de chaque et max_key_repeat de chaque (avec repetition)
# le nombre de groupements = 
# 	n * (nombre de facons d'arriver a k en repartissant 1 a max_key_repeat dans n - 1 slots)
	return out

out = ""
for x in range(1, 10):
	for y in range(1, x + 1):
		out += "x : " + str(x) + " y : " + str(y) + "\n"
		out += solution(x, y)
with open("test.txt", "w") as f:
	f.write(out)