from datetime import datetime
filepath = 'Data.txt'
#filepath = 'DataTest.txt'


dataDict = {}
guardsDictionary = {}

with open(filepath) as fp:
	
	for line in fp: #Read each line in the File
		# Create a date time value as a Key for the Dictionary
		dateTime = datetime.strptime(line.lstrip('[').split(']')[0], '%Y-%m-%d %H:%M')
		dataDict.update({dateTime : line.lstrip('[').split(']')[1].strip()}) # Add the description associated to the DateTime


guardId = 0
fallsAsleep = 0
wakesUp = 0

for key in sorted(dataDict):
	if filepath == 'DataTest.txt':
		print('{0} - {1}'.format(key, dataDict[key]))
	
	if dataDict[key].strip()[0].upper() == 'G': # New Shift
		guardId = int(dataDict[key].strip().split('#')[1].split()[0]) # Get the Guard ID
		# Add the Guard Id to the Guards Dictionary if not exists
		if guardsDictionary.get(guardId) == None:
			guardsDictionary.update({guardId : [0, dict.fromkeys(range(60), 0)]})

	if dataDict[key].strip()[0].upper() == 'F': # Falls Asleep
		fallsAsleep = key.minute # Get the minute the Guard falls asleep

	if dataDict[key].strip()[0].upper() == 'W': # Wakes Up
		wakesUp = key.minute # Get the minute the Guard wakes up
		guardsDictionary[guardId][0] += wakesUp - fallsAsleep # Add the amount of time spent asleep
		# For each minute on the sleeping range add 1 to the minutes dictionary for the GuardId
		for n in range(fallsAsleep,wakesUp,1):
			guardsDictionary[guardId][1][n] += 1


#if filepath == 'DataTest.txt':
#	print('\n{0}'.format(guardsDictionary))

guardId = 0
highestSleepTime = 0
for key in guardsDictionary:
	highestSleepTime = guardsDictionary[key][0] if guardsDictionary[key][0] > highestSleepTime else highestSleepTime
	guardId = key if guardsDictionary[key][0] == highestSleepTime else guardId

print('\nGuard Id: {0} - Sleep Time: {1}'.format(guardId, highestSleepTime))

# Get the most frequent minute 
mostFrequentMinute = 0
minuteFrequency = 0
for minute in guardsDictionary[guardId][1]: # For each minute on the GuardId minute Dictionary...
	# ...get the most frequent minute asleep
	if guardsDictionary[guardId][1][minute] > minuteFrequency:
		minuteFrequency = guardsDictionary[guardId][1][minute]
		mostFrequentMinute = minute

print('{0} * {1} = {2}'.format(guardId, mostFrequentMinute, guardId * mostFrequentMinute))

# Get the Guard with the most frequent minute asleep
guardId = 0
mostFrequentMinute = 0
minuteFrequency = 0
for guard in guardsDictionary:

	for minute in guardsDictionary[guard][1]: # For each minute on the GuardId minute Dictionary...
		# ...get the most frequent minute asleep
		if guardsDictionary[guard][1][minute] > minuteFrequency:
			guardId = guard
			minuteFrequency = guardsDictionary[guard][1][minute]
			mostFrequentMinute = minute

print('\nGuard Id: {0}'.format(guardId))
print('{0} * {1} = {2}'.format(guardId, mostFrequentMinute, guardId * mostFrequentMinute))

print('\n')
