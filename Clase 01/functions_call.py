fruit = ['apple', 'orange', 'grape', 'kiwi', 'apple', 'orange', 'strawberry']

def analyse_list(l):

	counts = {}
	for item in l:
		if item in counts:
			counts[item] = counts[item] + 1
		else:
			counts[item] = 1

	return counts

#comment
counts = analyse_list(fruit)
print counts