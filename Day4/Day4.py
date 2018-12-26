from datetime import datetime
filepath = 'Data.txt'
#filepath = 'DataTest.txt'


myDict = {}

with open(filepath) as fp:
	
	for line in fp: #Read each line in the File
		
		dateTime = datetime.strptime(line.lstrip('[').split(']')[0], '%Y-%m-%d %H:%M')
		myDict.update({dateTime : line.lstrip('[').split(']')[1].strip()})



for key in sorted(myDict):
  print('{0} - {1}'.format(key, myDict[key]))

#print(myDict)
print('\n')
