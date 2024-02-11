import random
import time
import matplotlib.pyplot as plt

# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Quicksort for Best Case
def quicksort_best_case(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Select the middle element as pivot
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_best_case(left) + [pivot] + quicksort_best_case(right)

def quicksort_worst_case(arr):
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = high  # Choose the last element as pivot for worst case
            i = low - 1
            for j in range(low, high):
                if arr[j] <= arr[pivot]:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]
            p = i + 1
            stack.append((low, p - 1))
            stack.append((p + 1, high))
    
    return arr

# Function to generate arrays for best, worst, and average cases for Bubble Sort
def generate_arrays_bubble(size):
    best_case = list(range(1, size+1))
    worst_case = list(range(size, 0, -1))
    average_case = random.sample(range(1, size+1), size)
    return best_case, worst_case, average_case

# Function to generate arrays for best, worst, and average cases for Quick Sort
def generate_arrays_quick(size):
    best_case = list(range(1, size+1))
    return best_case

# Function to test algorithm performance for Bubble Sort
def test_algorithm_performance_bubble(algorithm_name, sizes):
    best_times = []
    worst_times = []
    average_times = []

    for size in sizes:
        best_case, worst_case, average_case = generate_arrays_bubble(size)

        # Measure time for best case
        start_time = time.time()
        bubble_sort(best_case.copy())
        best_time = time.time() - start_time

        # Measure time for worst case
        start_time = time.time()
        bubble_sort(worst_case.copy())
        worst_time = time.time() - start_time

        # Measure time for average case
        start_time = time.time()
        bubble_sort(average_case.copy())
        average_time = time.time() - start_time

        best_times.append(best_time)
        worst_times.append(worst_time)
        average_times.append(average_time)

    plot_performance(algorithm_name, sizes, best_times, worst_times, average_times)

# Function to test algorithm performance for Quick Sort
def test_algorithm_performance_quick(algorithm_name, sizes):
    best_times = []
    worst_times = []
    average_times = []

    for size in sizes:
        best_case = generate_arrays_quick(size)
        worst_case = best_case.copy()  
        average_case = random.sample(best_case, len(best_case))  

        # Measure time for best case
        start_time = time.time()
        quicksort_best_case(best_case.copy())
        best_time = time.time() - start_time

        # Measure time for worst case
        start_time = time.time()
        quicksort_worst_case(worst_case.copy())
        worst_time = time.time() - start_time

        # Measure time for average case
        start_time = time.time()
        quicksort_best_case(average_case.copy())
        average_time = time.time() - start_time

        best_times.append(best_time)
        worst_times.append(worst_time)
        average_times.append(average_time)

    plot_performance(algorithm_name, sizes, best_times, worst_times, average_times)

# Function to generate performance plots
def plot_performance(algorithm_name, sizes, best_times, worst_times, average_times):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

    ax1.plot(sizes, best_times, label='Best Case')
    ax1.set_ylabel('Time (s)')
    ax1.set_title(f'Performance of {algorithm_name} (Best Case)')

    ax2.plot(sizes, worst_times, label='Worst Case')
    ax2.set_ylabel('Time (s)')
    ax2.set_title(f'Performance of {algorithm_name} (Worst Case)')

    ax3.plot(sizes, average_times, label='Average Case')
    ax3.set_xlabel('Input Size')
    ax3.set_ylabel('Time (s)')
    ax3.set_title(f'Performance of {algorithm_name} (Average Case)')

    plt.tight_layout()
    plt.show()

# Test both algorithms on 20 different sizes of input arrays
sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

# Test Bubble Sort performance
test_algorithm_performance_bubble("Bubble Sort", sizes)

# Test Quicksort for Best Case performance
test_algorithm_performance_quick("Quicksort", sizes)
