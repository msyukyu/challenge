class Solver:
	def __init__(self, map):
		self.map = map
		self.y = len(map)
		self.x = len(map[0])
		self.e = self.iAmHere(self.x - 1, self.y - 1)
		self.s = self.iAmHere(0, 0)
		
	def whereAmI(self, pos):
		x = pos % self.x
		y = pos // self.x
		return x, y
		
	def iAmHere(self, x, y):
		return self.x * y + x

	def canGoThere(self, x, y, done, i):
		p = self.iAmHere(x, y)
		flag = self.map[y][x] == 1
		if p in done[0] or (p in done[1] and (i == 1 or flag == 1)):
			return False
		if i == 1 and flag == 1:
			return False
		return True

	def canGoLeft(self, x, y, done, i):
		if x == 0:
			return False
		return self.canGoThere(x - 1, y, done, i)
	
	def canGoRight(self, x, y, done, i):
		if x == self.x - 1:
			return False
		return self.canGoThere(x + 1, y, done, i)
		
	def canGoUp(self, x, y, done, i):
		if y == 0:
			return False
		return self.canGoThere(x, y - 1, done, i)
		
	def canGoDown(self, x, y, done, i):
		if y == self.y - 1:
			return False
		return self.canGoThere(x, y + 1, done, i)

	def goto(self, x, y, tcur, done, i):
		p = self.iAmHere(x, y)
		flag = self.map[y][x] == 1 or i == 1
		tcur[flag].add(p)
		done[flag].add(p)

	def advance(self, p, tcur, done, i):
		x, y = self.whereAmI(p)
		if self.canGoLeft(x, y, done, i):
			self.goto(x - 1, y, tcur, done, i)
		if self.canGoUp(x, y, done, i):
			self.goto(x, y - 1, tcur, done, i)
		if self.canGoRight(x, y, done, i):
			self.goto(x + 1, y, tcur, done, i)
		if self.canGoDown(x, y, done, i):
			self.goto(x, y + 1, tcur, done, i)
	
	def solve(self):
		cost = 1
		done = [{self.s}, set()]
		cur = [{self.s}, set()]
		while len(cur[0]) > 0 or len(cur[1]) > 0:
			tcur = [set(), set()]
			cost += 1
			for i in range(len(cur)):
				for p in cur[i]:
					self.advance(p, tcur, done, i)
					if self.e in tcur[0] or self.e in tcur[1]:
						return cost
			cur = tcur
		return 0
				
			
			
def solution(map):
	solver = Solver(map)
	return solver.solve()
	
print(str(solution([
   [0, 1, 0, 1, 0, 0, 0], 
   [0, 0, 0, 1, 0, 1, 0]
])))