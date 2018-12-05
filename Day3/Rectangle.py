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

		#if self.x1 < r.x1 or r.x2 < self.x2:

		if r.x1 <= self.x1:
			if (r.x2 > self.x1 and (r.x2 < self.x2 or r.x2 >= self.x2)): newX1 = self.x1
		else:
			if (r.x1 < self.x2 and (r.x2 < self.x2 or r.x2 >= self.x2)): newX1 = r.x1

		if r.x2 <= self.x2:
			if (r.x2 > self.x1 and (r.x1 <= self.x1 or r.x1 > self.x1)): newX2 = self.x1
		else:
			if (r.x1 < self.x2 and (r.x2 < self.x2 or r.x2 > self.x2)): newX1 = r.x1

		print('({},{}) to ({},{})'.format(newX1, newY1, newX2, newY2))
		
			