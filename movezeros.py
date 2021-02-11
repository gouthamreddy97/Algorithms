def movezeros(a):

	ar = []
	z = []

	for i in range(len(a)):
		if a[i]==0:
			z.append(a[i])
		else:
			ar.append(a[i])
	return ar+z

print(movezeros(a))