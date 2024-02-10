import time
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Traditional Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Binary Insertion Sort
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # Find location to insert using binary search
        loc = binary_search(arr, key, 0, i - 1)
        # Move all elements after location to create space
        arr = arr[:loc] + [key] + arr[loc:i] + arr[i+1:]
    return arr

def binary_search(arr, key, start, end):
    if start == end:
        if arr[start] > key:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < key:
        return binary_search(arr, key, mid + 1, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid - 1)
    else:
        return mid

# Test the algorithms
sizes = list(range(100, 1001, 100))
traditional_times = []
binary_times = []

for size in sizes:
    arr = [random.randint(1, size) for _ in range(size)]
    
    start = time.time()
    insertion_sort(arr.copy())
    end = time.time()
    traditional_times.append(end - start)

    start = time.time()
    binary_insertion_sort(arr.copy())
    end = time.time()
    binary_times.append(end - start)

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(sizes, traditional_times, marker='o', label='Traditional Insertion Sort')
plt.plot(sizes, binary_times, marker='o', label='Binary Insertion Sort')

# Interpolating functions
xnew = np.linspace(min(sizes), max(sizes), 500)
spl_traditional = make_interp_spline(sizes, traditional_times, k=3)
spl_binary = make_interp_spline(sizes, binary_times, k=3)
plt.plot(xnew, spl_traditional(xnew), label='Traditional Insertion Sort (interpolated)')
plt.plot(xnew, spl_binary(xnew), label='Binary Insertion Sort (interpolated)')

plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.title('Performance Comparison: Traditional vs Binary Insertion Sort')
plt.show()


# 4. Binary Insertion Sort is usually faster than Traditional Insertion Sort. The reason is that Binary Insertion Sort uses binary search to find the proper location to insert the selected item at each iteration. This reduces the number of comparisons in the case of sorted lists, which is the main factor contributing to the time complexity