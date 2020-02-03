class Coordinates:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __equ__(self, coordinates):
		return coordinates.x == self.x and coordinates.y == self.y

	def __hash__(self):
		return self.x * 1251 + self.y

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

class Room:
	orientations = {
		Coordinates(0, 1): [Coordinates(0, 1), Coordinates(-1, 0)],
		Coordinates(-1, 0): [Coordinates(-1, 0), Coordinates(0, -1)],
		Coordinates(0, -1): [Coordinates(0, -1), Coordinates(1, 0)],
		Coordinates(1, 0): [Coordinates(1, 0), Coordinates(0, 1)]
	}
	def __init__(self, origin, dimensions, host, target, clones):
		self.dimensions = dimensions
		self.host = host
		self.target = target
		self.origin = origin
		self.clones = clones

	def clone(self, list_rooms):
		for clone in self.clones:
			origin = self.dimensions.clone().c_mult(clone).add(self.origin)
			dimensions = self.dimensions
			host = self.host.clone().mirror(origin, dimensions, clone)
			target = self.target.clone().mirror(origin, dimensions, clone)
			clones = Room.orientations[clone]
			list_rooms.append(Room(origin, dimensions, host, target, clones))

def solution(dimensions, your_position, guard_position, distance):
	C = Coordinates
	init = Room(C(0, 0),
		C(dimensions[0], dimensions[1]),
		C(your_position[0], your_position[1]),
		C(guard_position[0], guard_position[1]),
		[C(0, 1), C(-1, 0), C(0, -1), C(1, 0)])
