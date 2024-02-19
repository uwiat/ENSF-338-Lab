#Q1 The strategy used to grow array when full is a form of dynamic array resizing, referred to as over-allocation
#Initially, the code calculates a new allocation size (new_allocated) based on the current size of the list (newsize)
#new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3; This formula in line 70 calculates a size that is slightly 
#larger than the new size, ensuring that there's room for additional growth without the need for frequent reallocations. 
#The growth factor here is roughly 1.125x.
#However, the code also checks if the new size is significantly smaller than the current allocation size, and if so, 
#it adjusts the new allocation size to be closer to the new size: 
#if (newsize - Py_SIZE(self) > (Py_ssize_t)(new_allocated - newsize)) new_allocated = ((size_t)newsize + 3) & ~(size_t)3; line 74-75
#This adjustment prevents over-allocation when the new size is much smaller than the current allocation.
#Finally, the code adds padding to ensure that the allocated size is a multiple of 4: 
#new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3; line 70

import sys

# Initialize an empty list
my_list = []

# Initialize variable to keep track of previous size
prev_size = 0

# Loop to grow the list from 0 to 63 integers
for i in range(64):
    # Append an integer to the list
    my_list.append(i)
    
    # Check if the size has changed
    current_size = sys.getsizeof(my_list)
    if current_size != prev_size:
        print(f"Capacity changed after adding {i + 1} elements!")
        prev_size = current_size

import timeit
import numpy as np
import matplotlib.pyplot as plt


# Initialize array of size S
S = 8000
array = np.arange(S)

# Measure time to grow from S to S+1
start_time = timeit.default_timer()
array = np.append(array, 0)
end_time = timeit.default_timer()
time_S_to_S_plus_1 = end_time - start_time

# Repeat the measure 1000 times
times_S_to_S_plus_1 = []
for _ in range(1000):
    array = np.arange(S)
    start_time = timeit.default_timer()
    array = np.append(array, 0)
    end_time = timeit.default_timer()
    times_S_to_S_plus_1.append(end_time - start_time)

avg_time_S_to_S_plus_1 = np.mean(times_S_to_S_plus_1)

# Measure time to grow from S-1 to S
times_S_minus_1_to_S = []
for _ in range(1000):
    array = np.arange(S-1)
    start_time = timeit.default_timer()
    array = np.append(array, 0)
    end_time = timeit.default_timer()
    times_S_minus_1_to_S.append(end_time - start_time)

avg_time_S_minus_1_to_S = np.mean(times_S_minus_1_to_S)



# Plot distributions
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.hist(times_S_to_S_plus_1, bins=30, color='skyblue', edgecolor='black')
plt.title('Time to grow from S to S+1')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(times_S_minus_1_to_S, bins=30, color='salmon', edgecolor='black')
plt.title('Time to grow from S-1 to S')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
#Q5 generally the times are very similar but  increasing the size from S-1 to S is a bit faster because     
#When appending an element to this array there is already enough allocated space the operation typically 
#involves a constant-time operation to add the element to the end of the array. 
#This is because there's no need to resize the array; the space for the new element is already available
#On the other hand, when appending an element to an array that needs to be resized (i.e., growing from size S to S+1), 
#the operation involves allocating a new block of memory with a larger size. This resizing operation can take more time
