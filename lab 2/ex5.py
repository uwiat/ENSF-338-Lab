import timeit
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
#Ex 5 part 1
#Implement linear search and binary search
def linearSearch(x, key):
    i=0
    for i in range(len(x)):
        if key == x[i]:
            return i
    return -1
    
    

def binarySearch(x,key):
    l= 0; h=n
    
    while (l <= h):
            mid = (l+h)//2
            if (key==x[mid]):
                return mid
            elif (key < x[mid]):
                h = mid - 1
                
            else:
                l = mid+1
                
        
    return -1



x = [1000,2000,3000,4000,5000,6000,7000]
key =  3000
n=len(x)


#Ex 5 Part 2
def measureSearchPerformance(searchFunction,arraySize,iterations=100):
    total_time = timeit.timeit(lambda : searchFunction(list(range(arraySize)), random.randint(0,arraySize-1)), number=iterations)
    return total_time/iterations
    

arraySizes = [1000,2000,4000,8000,16000,32000]

for size in  arraySizes:
    avg_time = measureSearchPerformance(linearSearch,size)
    print(f'Average time for linear search on array {size}: ~ {avg_time} seconds')
    
for size in  arraySizes:
    avg_time = measureSearchPerformance(binarySearch,size)
    print(f'Average time for binary search on array {size}: ~ {avg_time} seconds')

#Ex 5 Part 3
linear_times = [measureSearchPerformance(linearSearch, size) for size in arraySizes]    
binary_times = [measureSearchPerformance(binarySearch,size) for size in arraySizes]

def linear_model(x, a, b):
    return a * x + b

def logarithmic_model(x, a, b):
    return a * np.log(x) + b

# Curve fitting
params_linear, _ = curve_fit(linear_model, arraySizes, linear_times)
params_log, _ = curve_fit(logarithmic_model, arraySizes, binary_times)

# Plotting
plt.figure(figsize=(12, 6))    
# Linear Search Plot
plt.subplot(1, 2, 1)
plt.scatter(arraySizes, linear_times, label='Measured Times')
plt.plot(arraySizes, linear_model(np.array(arraySizes), *params_linear), label='Fitted Line', color='red')
plt.title('Linear Search Performance')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()
# Binary Search Plot
plt.subplot(1, 2, 2)
plt.scatter(arraySizes, binary_times, label='Measured Times')
plt.plot(arraySizes, logarithmic_model(np.array(arraySizes), *params_log), label='Fitted Curve', color='green')
plt.title('Binary Search Performance')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.legend()

plt.tight_layout()
plt.show()

#Ex 5 part 4
#LINEAR SEARCH
#The interpolating function for linear search is a linear function. A linear function is of the form f(x) = a * x + b.
#Parameters:
# a - slope: this parameter indicates the rate of timie with resepct to the size of the array. The larger 'a' value means a larger increase in time as the array size increases
# b - y intercept: this parameter represents the baseline time the algorithm takes, regardless of the array size. It is the time measurement when the array size is zero

#BINARY SEARCH
#The interpolating function for binary search is a logarithmic function. A logarithmic function is of the form f(x) = a * log(x) + b
#Paremeters:
# a - coefficient: this paremeter indicates how quick the time increases logarithmcally to the array size.
# b - constant: baseline time measurement offset. 

# The results conclude to be very similar to what my prediction were for both linear and binary search results. 
#The results showed that the functions align with the theoretical aspects of both search theorems where the linear 
#search scales linearly with the size of data and on the other hand, binary search scales logrithmically making it ideally efficient for large datasets. 