import time
import numpy as np
import matplotlib.pyplot as plt


# Linear Search (Inefficient Implementation)
# Worst-case Complexity: O(n)
def linear_search(arr, target):
	for i in range(len(arr)):
		if arr[i] == target:
			return i
	return -1

# Binary Search (Efficient Implementation)
# Worst-case Complexity: O(logn)
def binary_search(arr, target):
	low = 0
	high = len(arr) - 1
	mid = 0
	
	while low <= high:
		mid = (high + low) // 2
		if arr[mid] < target:
			low = mid + 1
		elif arr[mid] > target:
			high = mid - 1
		else:
			return mid
	return -1

def measure_time(search_func, arr, target):
	start_time = time.time()
	search_func(arr, target)
	end_time = time.time()
	return (end_time - start_time) * 1000  # Convert to milliseconds

def experiment():
	linear_search_times = []
	binary_search_times = []
	arr = sorted(np.random.randint(0, 1000000, size=1000))
	target = np.random.randint(0, 1000000)
	
	for _ in range(100):
		linear_search_times.append(measure_time(linear_search, arr, target))
		binary_search_times.append(measure_time(binary_search, arr, target))
		
	plt.hist(linear_search_times, alpha=0.5, label='Linear Search')
	plt.hist(binary_search_times, alpha=0.5, label='Binary Search')
	plt.xlabel('Execution Time (milliseconds)')
	plt.ylabel('Frequency')
	plt.legend(loc='upper right')
	plt.show()
	
experiment()


