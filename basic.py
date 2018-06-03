def maxProductFinder(tomb):
	tomb.sort()
	for i in tomb:
		print i
	neg = tomb[0] * tomb[1]
	print neg
	t_length = len(tomb) - 1
	case1 = tomb[t_length] * tomb[t_length - 1] * tomb[t_length -2]
	case2 = neg * tomb[t_length]
	if(case1 > case2):
		return case1
	else:
		return case2

array = [-6, -8, 4, 2, 5, 3, -1, 9, 10]
asdasd = [-8, 6, -7, 3, 2, 1, -9]
print ( maxProductFinder(array))

print (maxProductFinder(asdasd))
