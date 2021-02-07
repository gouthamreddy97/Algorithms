def word_average(text):
	sum = 0
	sptext = text.split()
	for i in range(len(sptext)):
		sum += len(sptext[i])
	return (sum/float(len(sptext)))

print(word_average('The quick brown fox jumps over the lazy dog'))

# Always add space between assignment operators and leave lines for code readability
# Logic should always be written within a function that accepts an input and returns an output