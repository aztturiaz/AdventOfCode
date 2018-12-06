
filepath = 'Data.txt'
#filepath = 'DataTest.txt'

claimsDictionary = {}
fabricOverlap = {}
totalSquareInches = 0

with open(filepath) as fp:
	cnt = 1
	for line in fp: #Read each line in the File
		
		point = line.split(' ')[2].rstrip(':').split(',')
		size = line.split(' ')[3].strip().split('x')

		for x in range(int(point[0]), int(point[0]) + int(size[0]), 1):
			for y in range(int(point[1]), int(point[1]) + int(size[1]), 1):
				if fabricOverlap.get('{},{}'.format(x, y)) == None:
				  fabricOverlap.update({'{},{}'.format(x, y):1})
				else:
				  fabricOverlap['{},{}'.format(x, y)] += 1

		cnt += 1

for item in fabricOverlap.items():
	if item[1] > 1:
	   totalSquareInches += 1

print('Total Square Inches = {}'.format(totalSquareInches))



