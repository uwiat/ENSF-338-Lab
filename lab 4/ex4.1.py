#def processdata(li):
#	for i in range(len(li)):
#		if li[i] > 5:
#			for j in range(len(li)):
#				li[i] *= 2


# 1. Best Case: The best case scenario occurs when all elements in the list li are less than or equal to 5. In this case, the inner loop does not get executed at all. The time complexity is therefore linear, O(n)

# Worst Case: The worst case scenario occurs when all elements in the list li are greater than 5. In this case, for each element in the list, the inner loop runs n times. Therefore, the time complexity is quadratic, O(n^2)

# Average Case: We assume a uniform random distribution of numbers, the average case complexity would still be O(n2)
				

# 2. They are not the same. Below is modified code for which average, best, and worst case complexity are equivalent.

def processdata(li):
	result = []
	for i in range(len(li)):
		if li[i] > 5:
			result.append(li[i] * 2)
		else:
			result.append(li[i])
	return result