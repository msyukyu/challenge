class Solver:
	def __init__(self, map):
		self.map = map
		self.y = len(map)
		self.x = len(map[0])
		self.cost = [[-1] * self.x for i in range(self.y)]
		self.fcost = [[-1] * self.x for i in range(self.y)]
		self.cost[0][0] = 1
		self.flag = 0
		
	def whereAmI(self, pos):
		x = pos % self.x
		y = pos // self.x
		return x, y
		
	def iAmHere(self, x, y):
		return self.x * y + x
		
	def canGoThere(self, x, y, cost):
		flag = self.flag
		if self.map[y][x] == 1 and self.flag == 1:
			return False
		elif self.map[y][x] == 1:
			flag = 1
		if flag == 1 and \
			((self.fcost[y][x] != -1 and self.fcost[y][x] <= cost) or \
			(self.cost[y][x] != -1 and self.cost[y][x] <= cost)):
			return False
		if flag == 0 and self.cost[y][x] != -1 and self.cost[y][x] <= cost:
			return False
		return True
		
	def canGoLeft(self, x, y, cost):
		if x == 0:
			return False
		return self.canGoThere(x - 1, y, cost)
	
	def canGoRight(self, x, y, cost):
		if x == self.x - 1:
			return False
		return self.canGoThere(x + 1, y, cost)
		
	def canGoUp(self, x, y, cost):
		if y == 0:
			return False
		return self.canGoThere(x, y - 1, cost)
		
	def canGoDown(self, x, y, cost):
		if y == self.y - 1:
			return False
		return self.canGoThere(x, y + 1, cost)
	
	def goto(self, pos, x, y, cost):
		if self.map[y][x] == 1:
			self.flag = 1
		if self.flag == 1:
			self.fcost[y][x] = cost
		else:
			self.cost[y][x] = cost
		if x != self.x - 1 or y != self.y - 1:
			self.solve(self.iAmHere(x, y), cost)
		if self.map[y][x] == 1:
			self.flag = 0
	
	def solve(self, pos, cost):
		x, y = self.whereAmI(pos)
		cost += 1
		if self.canGoLeft(x, y, cost):
			self.goto(pos, x - 1, y, cost)
		if self.canGoUp(x, y, cost):
			self.goto(pos, x, y - 1, cost)
		if self.canGoRight(x, y, cost):
			self.goto(pos, x + 1, y, cost)
		if self.canGoDown(x, y, cost):
			self.goto(pos, x, y + 1, cost)
			
def solution(map):
	solver = Solver(map)
	solver.solve(0, 1)
	sol = solver.cost[solver.y - 1][solver.x -1]
	fsol = solver.fcost[solver.y - 1][solver.x - 1]
	if fsol != -1:
		sol = fsol if sol == -1 else min(sol, fsol)
	return sol

print(str(solution([
   [0, 1, 0, 1, 0, 0, 0], 
   [0, 0, 0, 1, 0, 1, 0]
])))