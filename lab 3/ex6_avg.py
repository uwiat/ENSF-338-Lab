import timeit
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#EX 6.1

def linearSearch(x, key):
    i=0
    for i in range(len(x)):
        if key == x[i]:
            return i
    return -1

def quickSort(A, l, h):
    if l < h:
        j = partition(A, l, h)
        quickSort(A, l, j)
        quickSort(A, j + 1, h)
    
def partition(A,l,h):
    pivot = A[l]
    i=l
    j=h
    
    while (i<j): 
        i+=1
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] > pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j             
        

        

def binarySearch(x,key):
    l= 0; h=n
    quickSort(A, 0, len(A)-1)
    while (l <= h):
            mid = (l+h)//2
            if (key==x[mid]):
                return mid
            elif (key < x[mid]):
                h = mid - 1
                
            else:
                l = mid+1
                
        
    return -1

def measureSearchPerformance(searchFunction,arraySize,constantElement,iterations=1000):
    array = list(range(arraySize))
    total_time = timeit.timeit(lambda : searchFunction(array, constantElement), number=iterations)
    return total_time/iterations

A = [2000,2230,8000,5000,16000,7000]
n=len(A)




#EX 6.2

for size in  [1000]:
    avg_time = measureSearchPerformance(linearSearch,size, constantElement=7000)
    print(f'Average time for linear search on array {size}: ~ {avg_time} seconds with the constant element 7000 in each instance of the array')

for size in  [1000]:
    avg_time = measureSearchPerformance(binarySearch,size, constantElement=7000)
    print(f'Average time for binary search on array {size}: ~ {avg_time} seconds with the constant element 7000 in each instance of the array')

#EX 6.3
z = [10, 20, 50]
while z[2] <= 5000000:
    for i in range(len(z)):  
        avg_time = measureSearchPerformance(linearSearch, z[i], constantElement=7000)
        print(f'Average time for linear search on array {z[i]}: ~ {avg_time} seconds with the constant element 7000 in each instance of the array')
        z[i] = z[i] * 10 

k = [10, 20, 50]
while k[2] <= 5000000:
    for i in range(len(k)):  
        avg_time = measureSearchPerformance(binarySearch, k[i], constantElement=7000)
        print(f'Average time for binary search on array {k[i]}: ~ {avg_time} seconds with the constant element 7000 in each instance of the array')
        k[i] = k[i] * 10 


def linear_model(x, a, b):
    return a * x + b

def logarithmic_model(x, a, b):
    return a * np.log(x) + b

#EX 6.4


linear_times = [measureSearchPerformance(linearSearch, size, 7000) for size in A]
binary_times = [measureSearchPerformance(binarySearch, size, 7000) for size in A]




params_linear, _ = curve_fit(linear_model, A, linear_times)
params_log, _ = curve_fit(logarithmic_model, A, binary_times)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(A, linear_times, label='Measured Times')
plt.plot(A, linear_model(np.array(A), *params_linear), label='Fitted Line', color='red')
plt.title('Linear Search Performance')
plt.xlabel('Array Size')
plt.ylabel('Change in Time (seconds)')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(A, binary_times, label='Measured Times')
plt.plot(A, logarithmic_model(np.array(A), *params_log), label='Fitted Curve', color='green')
plt.title('Binary Search Performance')
plt.xlabel('Array Size')
plt.ylabel('Change in Time (seconds)')
plt.legend()

plt.tight_layout()
plt.show()

#From the above algorithms- the faster algorithm would be the linear search as the best fit line 
#shows an average lesser time in completion of the search than the binary search which is significantly higher.

