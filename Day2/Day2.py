
filepath = 'Data.txt'
#filepath = 'DataTest.txt'

with open(filepath) as fp:
	cnt = 1
	checksumDict = {2: 0, 3: 0}

	for line in fp:
		substring = ""
		charDict = {}
		foundDoubles = False; foundTriples = False

		
		for char in line.strip():
			if charDict.get(char, 0) == 0:
				charDict.update({char: 1})
			else:
				charDict[char] += 1
		
		for char in charDict.items():
			if (char[1] == 2 and not foundDoubles):
				checksumDict[2] += 1
				foundDoubles = True
			if (char[1] == 3 and not foundTriples):
				checksumDict[3] += 1
				foundTriples = True
		
		#print('Line {}: charDict = {}'.format(cnt, charDict))
		cnt += 1
	
	print('Checksum Dictionary = {}'.format(checksumDict))
	print('Final CheckSum = {}'.format(checksumDict[2] * checksumDict[3]))

print('\n\n')



