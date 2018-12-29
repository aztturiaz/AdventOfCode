from datetime import datetime
filepath = 'Data.txt'
filepath = 'DataTest.txt'


dataDict = {}
guardsDictionary = {}

with open(filepath) as fp:
	
	for line in fp: #Read each line in the File
		
		dateTime = datetime.strptime(line.lstrip('[').split(']')[0], '%Y-%m-%d %H:%M')
		dataDict.update({dateTime : line.lstrip('[').split(']')[1].strip()})


guardId = 0
fallsAsleep = 0
wakesUp = 0

for key in sorted(dataDict):
	print('{0} - {1}'.format(key, dataDict[key]))
	
	if dataDict[key].strip()[0].upper() == 'G': # New Shift
		guardId = int(dataDict[key].strip().split('#')[1].split()[0]) # Get the Guard ID
		# Add the Guard Id to the Guards Dictionary if not exists
		if guardsDictionary.get(guardId) == None:
			guardsDictionary.update({guardId : [0, dict.fromkeys(range(60), 0)]})
		#print(guardsDictionary.get(guardId))

	if dataDict[key].strip()[0].upper() == 'F': # Falls Asleep
		fallsAsleep = key.minute
		#print(fallsAsleep)

	if dataDict[key].strip()[0].upper() == 'W': # Wakes Up
		wakesUp = key.minute
		guardsDictionary[guardId][0] += wakesUp - fallsAsleep
		for n in range(fallsAsleep,wakesUp,1):
			guardsDictionary[guardId][1][n] += 1
		#print(wakesUp)

#print(guardsDictionary)

guardId = 0
highestSleepTime = 0
for key in sorted(guardsDictionary):
	highestSleepTime = guardsDictionary[key][0] if guardsDictionary[key][0] > highestSleepTime else highestSleepTime
	guardId = key if guardsDictionary[key][0] == highestSleepTime else guardId
	print('{0} - {1}'.format(key, guardsDictionary[key][1]))

#print(myDict)
print('\n')
