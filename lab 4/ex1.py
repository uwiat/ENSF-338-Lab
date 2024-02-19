import time
import random
import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def binary_search(self, num):
        left, right = 0, self.length() - 1
        while left <= right:
            mid = (left + right) // 2
            if self.get(mid).data == num:
                return True
            elif self.get(mid).data < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get(self, index):
        if index < 0 or index >= self.length():
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

class Array:
    def __init__(self):
        self.arr = []

    def append(self, data):
        self.arr.append(data)

    def binary_search(self, num):
        left, right = 0, len(self.arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] == num:
                return True
            elif self.arr[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

def measure_performance(data_structure, input_sizes):
    avg_runtimes = []
    for size in input_sizes:
        runtimes = []
        for _ in range(10):  # Repeat 10 times for averaging
            data = sorted(random.sample(range(size * 10), size))
            start_time = time.time()
            for i in range(100):  # Perform binary search 100 times
                data_structure.binary_search(random.choice(data))
            end_time = time.time()
            runtimes.append(end_time - start_time)
        avg_runtimes.append(np.mean(runtimes))
    return avg_runtimes

input_sizes = [1000, 2000, 4000, 8000]
linked_list_perf = measure_performance(LinkedList(), input_sizes)
array_perf = measure_performance(Array(), input_sizes)

# Plot performance
plt.plot(input_sizes, linked_list_perf, marker='o', label='Linked List')
plt.plot(input_sizes, array_perf, marker='o', label='Array')
plt.xlabel('Input Size')
plt.ylabel('Average Runtime (s)')
plt.title('Performance of Binary Search in Linked List and Array')
plt.legend()

# Interpolate 
x = np.linspace(min(input_sizes), max(input_sizes), 1000)
linked_list_fit = np.polyfit(input_sizes, linked_list_perf, 2)
linked_list_interpolated = np.polyval(linked_list_fit, x)
array_fit = np.polyfit(input_sizes, array_perf, 2)
array_interpolated = np.polyval(array_fit, x)

plt.plot(x, linked_list_interpolated, linestyle='--', label='Linked List (Interpolated)')
plt.plot(x, array_interpolated, linestyle='--', label='Array (Interpolated)')

plt.legend()
plt.show()

#Q4 The complexity of binary search for linked lists is O(log n), where n is the number of elements in the list. 
#This is because at each step, we are effectively reducing the search space by half.
#Accessing elements in a linked list requires traversing the list from the head, which takes linear time proportional to the 
#length of the list. However, binary search on a linked list still exhibits logarithmic time complexity 
#due to the halving of the search space at each step.