import timeit
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


#EX 7.3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def get_size(self):
        return self.size

    def get_element_at_pos(self, pos):
        current = self.head
        for _ in range(pos):
            current = current.next
        return current
    #The reverse function given to us in the D2L Lab 4 document
    def reverseGiven(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
                prevNode = currNewNode  # Initialize prevNode here as well
            else:
                prevNode.next = currNewNode
                prevNode = currNewNode  # Move prevNode to the current new node
        self.head = newhead


    #The reverse function made by me in EX7.2 and rewritten for EX 7.3 and 7.4
    def reverseRemade(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev  # Reverse the next pointer
            current.prev = next  # Reverse the prev pointer for a doubly linked list
            prev = current
            current = next
        self.head = prev

def measureReversePerformance(dll, reverse_function, iterations=100):
    # Reset the list to its original state if necessary
    total_time = timeit.timeit(
        lambda: reverse_function(),  # This assumes reverse_function is correctly bound to dll instance.
        number=iterations
    )
    return total_time / iterations


arraySizes = [1000, 2000, 3000, 4000]
iterations = 100
avg_times_given = []
avg_times_remade = []
# Timing for reverseGiven
for size in arraySizes:
    dll = DoublyLinkedList()
    for i in range(size):
        dll.append(i)
    
    avg_time = measureReversePerformance(dll, dll.reverseGiven, iterations)
    avg_times_given.append(avg_time)  # Store the measured average time
    print(f'Average time for the given reverse function to work on a doubly-linked list of size {size}: ~ {avg_time} seconds')

# Repeat for reverseRemade
for size in arraySizes:
    # Initialize and populate the doubly linked list for the measurement
    dll = DoublyLinkedList()
    for i in range(size):
        dll.append(i)
    
    # Measure performance of reverseRemade
    avg_time = measureReversePerformance(dll, dll.reverseRemade, iterations)
    avg_times_remade.append(avg_time)  # Store the measured average time
    print(f'Average time for the reverse function I made to work on a doubly-linked list of size {size}: ~ {avg_time} seconds')

#EX 7.4
plt.figure(figsize=(10, 6))

# Plot for reverseGiven method
plt.plot(arraySizes, avg_times_given, label='reverseGiven', marker='o', linestyle='-', color='blue')

# Plot for reverseRemade method
plt.plot(arraySizes, avg_times_remade, label='reverseRemade', marker='s', linestyle='-', color='red')

# Adding titles and labels
plt.title('Performance Comparison: reverseGiven vs. reverseRemade')
plt.xlabel('List Size')
plt.ylabel('Average Execution Time (seconds)')

# Adding a legend to explain which line is which
plt.legend()

# Show grid for better readability
plt.grid(True)

# Display the plot
plt.show()