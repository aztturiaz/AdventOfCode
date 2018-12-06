
filepath = 'Data.txt'
#filepath = 'DataTest.txt'

fabricDictionary = {}
claimIDDict = {}
totalSquareInches = 0
claimID = 0

overlapIDs = {}

with open(filepath) as fp:
	
	for line in fp: #Read each line in the File
		claimID += 1

		point = line.split(' ')[2].rstrip(':').split(',')
		size = line.split(' ')[3].strip().split('x')

		for x in range(int(point[0]), int(point[0]) + int(size[0]), 1): # Iterate through the X range
			for y in range(int(point[1]), int(point[1]) + int(size[1]), 1): # Iterate through the Y range for each X
				if fabricDictionary.get('{},{}'.format(x, y)) == None: # If the coordinate is not found in the Fabric Dictionary
					fabricDictionary.update({'{},{}'.format(x, y):[claimID, 1]}) # Add 1 more coordinate for the Fabric on the ClaimID
					if claimIDDict.get(claimID) == None: claimIDDict.update({claimID:1}) # If the Claim ID is not in the Claims Dictionary, add it
				else: # the coordinate IS found in the Fabric Dictionary
					fabricDictionary['{},{}'.format(x, y)][1] += 1 # Add 1 to the coordinate counter for Fabric and ClaimID
					if fabricDictionary.get('{},{}'.format(x, y))[0] != claimID: # If the Claim ID for the coordinate is not the same as the current Claim ID
						claimIDDict[fabricDictionary.get('{},{}'.format(x, y))[0]] += 1 # Add 1 to the coordinate counter for the existing ClaimID
						
						# Add 1 to the coordinate counter for the current ClaimID or add it to the Dictionary if does not exists
						if claimIDDict.get(claimID) == None: 
							claimIDDict.update({claimID: 1})
						else: 
							claimIDDict[claimID] += 1

# Get the Square Inches of overlaping fabric
for item in fabricDictionary.items():
	if item[1][1] > 1:
		totalSquareInches += 1

claimID = 0
# Get the Claim ID not overlaping
for id in claimIDDict.items():
	if id[1] == 1:
		claimID = id[0]
		break


print('Total Square Inches = {}'.format(totalSquareInches))
print('Claim Id w/no overlap: {}'.format(claimID))


