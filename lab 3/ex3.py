def bubble_sort(arr):
	n = len(arr)
	num_comparisons = 0
	num_swaps = 0
	
	for i in range(n):
		for j in range(0, n-i-1):
			num_comparisons += 1
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				num_swaps += 1
				
	return arr, num_comparisons, num_swaps

# Test the function
arr = [2, 1]
print(f"Original array is: {arr}")
sorted_arr, num_comparisons, num_swaps = bubble_sort(arr)
print(f"Sorted array is: {sorted_arr}")
print(f"Number of inputs: {len(arr)}")
print(f"Number of comparisons: {num_comparisons}")
print(f"Number of swaps: {num_swaps}")
print("--------------------------------------------------")
arr = [4, 1, 3, 2]
print(f"Original array is: {arr}")
sorted_arr, num_comparisons, num_swaps = bubble_sort(arr)
print(f"Sorted array is: {sorted_arr}")
print(f"Number of inputs: {len(arr)}")
print(f"Number of comparisons: {num_comparisons}")
print(f"Number of swaps: {num_swaps}")
print("--------------------------------------------------")
arr = [5, 1, 4, 6, 2, 3]
print(f"Original array is: {arr}")
sorted_arr, num_comparisons, num_swaps = bubble_sort(arr)
print(f"Sorted array is: {sorted_arr}")
print(f"Number of inputs: {len(arr)}")
print(f"Number of comparisons: {num_comparisons}")
print(f"Number of swaps: {num_swaps}")
print("--------------------------------------------------")
arr = [5, 7, 2, 4, 1, 6, 3, 8]
print(f"Original array is: {arr}")
sorted_arr, num_comparisons, num_swaps = bubble_sort(arr)
print(f"Sorted array is: {sorted_arr}")
print(f"Number of inputs: {len(arr)}")
print(f"Number of comparisons: {num_comparisons}")
print(f"Number of swaps: {num_swaps}")
print("--------------------------------------------------")
arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
print(f"Original array is: {arr}")
sorted_arr, num_comparisons, num_swaps = bubble_sort(arr)
print(f"Sorted array is: {sorted_arr}")
print(f"Number of inputs: {len(arr)}")
print(f"Number of comparisons: {num_comparisons}")
print(f"Number of swaps: {num_swaps}")







