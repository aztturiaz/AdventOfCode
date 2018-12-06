
filepath = 'Data.txt'
filepath = 'DataTest.txt'

claimsDictionary = {}
totalSquareInches = 0
claimIDList = []
cnt = 0

with open(filepath) as fp:
	
	for line in fp: #Read each line in the File
		cnt += 1

		point = line.split(' ')[2].rstrip(':').split(',')
		size = line.split(' ')[3].strip().split('x')

		for x in range(int(point[0]), int(point[0]) + int(size[0]), 1):
			for y in range(int(point[1]), int(point[1]) + int(size[1]), 1):
				if claimsDictionary.get('{},{}'.format(x, y)) == None:
				  claimsDictionary.update({'{},{}'.format(x, y):[cnt, 1]})
				else:
				  claimsDictionary['{},{}'.format(x, y)][1] += 1

				#if cnt not in claimIDList:
				#	claimIDList.append(cnt)

# Get the Square Inches of overlaping fabric
for item in claimsDictionary.items():
	if item[1][1] > 1:
		totalSquareInches += 1
		if item[1][0] not in claimIDList:
			claimIDList.append(item[1][0])

# Get the Claim ID not overlaping
claimID = 0	
for id in range(1, cnt + 1, 1):
	if id not in claimIDList:
		claimID = id

print('Total Square Inches = {}'.format(totalSquareInches))
print('Claim Id w/no overlap: {}'.format(claimID))


