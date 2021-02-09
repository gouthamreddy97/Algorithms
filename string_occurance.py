#abbcccdeeeffg

def str_occurance(string):
	
	data = {}
	count = 1

	for i in range(len(string)):
		if(i+1 == len(string)):
			data[string[i]] = count
		elif(string[i] == string[i+1]):
			count += 1
		else:
			data[string[i]] = count
			count = 1
	return data

print(str_occurance('abbcccdeeeffg'))