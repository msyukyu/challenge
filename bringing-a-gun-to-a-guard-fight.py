from math import sqrt

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
		if orientation == "W" or orientation == "E":
			mirrors.append(orientation)
		else:
			mirrors.append(orientation)
			mirrors.append("W")
			mirrors.append("E")
		return mirrors

def solution(dimensions, your_position, guard_position, distance):
	C = Coordinates
	host = C(your_position[0], your_position[1])
	list_rooms = [Room(Room.center,
		C(dimensions[0], dimensions[1]),
		host,
		C(guard_position[0], guard_position[1]),
		["N", "S", "W", "E"])]
	count = 0
	while len(list_rooms) > 0:
		new_list = []
		for room in list_rooms:
			if host.distance(room.target) <= distance:
				if not (room.host != host and (host.x == room.target.x or host.y == room.target.y)):
					count += 1
				room.clone(new_list)
		list_rooms = new_list
	return count

print(str(solution([300,275], [150,150], [185,100], 500)))