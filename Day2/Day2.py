
#s = "Hello Visual Studio"
#print(s)
#if 'techbeamers'.isidentifier():
#    print("techbeamers is identifier")



filepath = 'Data.txt'
with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	for line in fp:
		#print("Line {}: {}".format(cnt, line.strip()))
		substring = ""
		charDict = {}
		for char in line.strip():
			charDict[char] += 1
			substring += "{}-".format(char)
		print("Line {}: {}".format(cnt, substring))
		line = fp.readline()
		cnt += 1
		if cnt == 10:
			break


print("\n\n\n")



