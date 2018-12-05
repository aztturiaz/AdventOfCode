class Rectangle:
	x1 = 0
	y2 = 0

	x2 = 0
	y1 = 0

	def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
		self.x1 = x1
		self.y1 = y1

		self.x2 = x2
		self.y2 = y2

	def Intersect(self, r: 'Rectangle'):
		newX1 = 0
		newY1 = 0
		
		newX2 = 0
		newY2 = 0

		# New X1
		if r.x1 <= self.x1:
			if (r.x2 >= self.x1): newX1 = self.x1
		else:
			if (r.x1 <= self.x2): newX1 = r.x1

		# New X2
		if r.x2 <= self.x2:
			if (r.x2 >= self.x1): newX2 = r.x2
		else:
			if (r.x1 <= self.x2): newX2 = self.x2

		# New Y1
		if r.y1 <= self.y1:
			if (r.y2 >= self.y1): newY1 = self.y1
		else:
			if (r.y1 <= self.y2): newY1 = r.y1

		# New Y2
		if r.y2 <= self.y2:
			if (r.y2 >= self.y1): newY2 = r.y2
		else:
			if (r.y1 <= self.y2): newY2 = self.y2

		return Rectangle(newX1, newY1, newX2, newY2)

	def SquareArea(self):
		x2 = (self.x2 + 1) if self.x2 != self.x1 else self.x2
		x1 = self.x1

		y2 = (self.y2 + 1) if self.y2 != self.y1 else self.y2
		y1 = self.y1

		width = abs(x2 - x1)
		height = abs(y2 - y1)

		print('W: {} - H: {}'.format(width, height))

		return width * height

		
			