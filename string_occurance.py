#abbcccdeeeffg

def str_occurance(string):

	ans = []

	for i in range(len(string)):

		if string[i] == string[-1]:
			s = (string[i],string.count(string[i]))
			ans.append(s)
			continue

		if string[i] == string[i+1]:
			i += 1
		else:
			s = (string[i],string.count(string[i]))
			ans.append(s)

	dk = []
	dv = []

	for (k,v) in ans:
		dk.append(k)
		dv.append(v)

	dzip = zip(dk,dv)
	dic = dict(dzip)
	
	return dic

print(str_occurance('abbcccdeeeffg'))