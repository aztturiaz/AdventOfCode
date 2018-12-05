
from Rectangle import Rectangle

filepath = 'Data.txt'
#filepath = 'DataTest.txt'
#filepath = 'DataTest2.txt'

r = Rectangle(1, 1, 1, 1)
r2 = Rectangle(2, 2, 2, 2)

print(r)
r.Intersect(r2)
