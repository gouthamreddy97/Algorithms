#The quick brown fox jumps over the lazy dog
text=('The quick brown fox jumps over the lazy dog')
sptext=text.split()
sum=0
for i in range(len(sptext)):
	lt=len(sptext[i])
	sum=sum+lt
print(sum/len(sptext))
