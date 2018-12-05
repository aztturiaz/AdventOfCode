
from Rectangle import Rectangle

filepath = 'Data.txt'
filepath = 'DataTest.txt'
#filepath = 'DataTest2.txt'

## ----------------------------------------------------------------------
r1 = Rectangle(1, 3, 4, 6)
r2 = Rectangle(3, 1, 6, 4)

r3 = r1.Intersect(r2)
print('({},{}) to ({},{})'.format(r3.x1, r3.y1, r3.x2, r3.y2))
print('Intersect Rectangle size = {}'.format(r3.SquareArea()))
print('Intersect Rectangle size = {}'.format(Rectangle(0, 0, 0, 0).SquareArea()))

## ----------------------------------------------------------------------

claimsDictionary = {}

with open(filepath) as fp:
	cnt = 1

	for line in fp: #Read each line in the File
		
		point = line.split(' ')[2].rstrip(':').split(',')
		size = line.split(' ')[3].strip().split('x')

		# Create the claim Rectangle
		rectangle = Rectangle(int(point[0]), int(point[1]), int(point[0]) + (int(size[0]) - 1), int(point[1]) + (int(size[1]) - 1))

		claimsDictionary.update({cnt:rectangle})

		cnt += 1

print('\n\n')
print(claimsDictionary)

copyClaims = claimsDictionary.copy()

for claim in claimsDictionary.items():

	rec01 = claim[1]

	del copyClaims[claim[0]]
	for copyClaim in copyClaims.items():
		continue
		rec02 = copyClaim[1]
		#rec01.Intersect



