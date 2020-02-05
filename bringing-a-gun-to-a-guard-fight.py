from math import sqrt
from fractions import Fraction

class Coordinates:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def mult(self, c):
		self.x *= c
		self.y *= c
		return self

	def c_mult(self, coordinates):
		self.x *= coordinates.x
		self.y *= coordinates.y
		return self

	def clone(self):
		return Coordinates(self.x, self.y)

	def add(self, coordinates):
		self.x += coordinates.x
		self.y += coordinates.y
		return self

	def sub(self, coordinates):
		self.x -= coordinates.x
		self.y -= coordinates.y
		return self

	def mirror(self, origin, dimensions, axis):
		origin = origin.clone()
		if axis.x == -1 or axis.y == -1:
			origin.add(dimensions)
		origin.c_mult(axis).sub(self.clone().c_mult(axis)).mult(2)
		return self.add(origin.c_mult(axis))

	def distance(self, coordinates):
		a = self.x - coordinates.x
		b = self.y - coordinates.y
		return sqrt(a * a + b * b)

	def between(self, c1, c2):
		return self.distance(c1) + self.distance(c2) == c2.distance(c1)

	def aligned(self, c1, c2):
		if (self.x == c2.x and self.x == c1.x) or \
			(self.y == c2.y and self.y == c1.y):
			return True
		c1 = c1.clone().sub(self)
		c2 = c2.clone().sub(self)
		return c1.y * c2.x == c1.x * c2.y

class Room:
	center = Coordinates(0, 0)
	axis = {
		"N": Coordinates(0, 1),
		"S": Coordinates(0, -1),
		"W": Coordinates(-1, 0),
		"E": Coordinates(1, 0)
	}
	def __init__(self, origin, dimensions, host, target, mirrors):
		self.dimensions = dimensions
		self.host = host
		self.target = target
		self.origin = origin
		self.mirrors = mirrors

	def clone(self, list_rooms):
		for orientation in self.mirrors:
			axis = Room.axis[orientation]
			origin = self.dimensions.clone().c_mult(axis).add(self.origin)
			dimensions = self.dimensions
			host = self.host.clone().mirror(origin, dimensions, axis)
			target = self.target.clone().mirror(origin, dimensions, axis)
			mirrors = self.get_mirrors(orientation)
			list_rooms.append(Room(origin, dimensions, host, target, mirrors))

	def get_mirrors(self, orientation):
		mirrors = []
		if orientation == "S" or orientation == "N":
			mirrors.append("W")
			mirrors.append("E")
		mirrors.append(orientation)
		return mirrors

def get_slope_position(host, c):
	s = Fraction(0, 1)
	p = 1 if c.x > host.x else 0
	if c.x == host.x:
		p = 1 if c.y > host.y else 0
		s = None
	elif c.y != host.y:
		s = Fraction(c.y - host.y, c.x - host.x)
	return s, p

def register_slope(slopes, s, p):
	if s not in slopes:
		slopes[s] = [0, 0]
	t = slopes[s]
	if t[p] == 1:
		return False
	t[p] = 1
	return True

def check_slopes(slopes, host, room):
	st, pt = get_slope_position(host, room.target)
	if room.host == host:
		return register_slope(slopes, st, pt)
	sh, ph = get_slope_position(host, room.host)
	if sh == st:
		if room.host.between(host, room.target):
			register_slope(slopes, sh, ph)
			return False
		return register_slope(slopes, st, pt)
	register_slope(slopes, sh, ph)
	return register_slope(slopes, st, pt)

def solution(dimensions, your_position, guard_position, distance):
	C = Coordinates
	host = C(your_position[0], your_position[1])
	target = C(guard_position[0], guard_position[1])
	list_rooms = [Room(Room.center,
		C(dimensions[0], dimensions[1]),
		host,
		target,
		["N", "S", "W", "E"])]
	count = 0
	slopes = {}
	while len(list_rooms) > 0:
		new_list = []
		for room in list_rooms:
			if host.distance(room.target) <= distance:
				if check_slopes(slopes, host, room):
					count += 1
				room.clone(new_list)
		list_rooms = new_list
	return count

print(str(solution([3,2], [1,1], [2,1], 4)))
print(str(solution([300,275], [150,150], [185,100], 500)))
print(str(solution([2,5], [1,2], [1,4], 11)))
