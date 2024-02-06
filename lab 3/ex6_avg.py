import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

def linearSearch(x, key):
    i=0
    for i in range(len(x)):
        if key == x[i]:
            return i
    return -1
    
    
def partition(l,h):
    pivot = A[l]
    i=l
    j=h;
    
    while (i<j): 
        i+=1
    while (A[i]<=pivot):
        j-=1
    while (A[j]>pivot):
        if (i<j):
            A[i], A[j] = A[j], A[i]
                    
    A[l], A[j] = A[j], A[l]
    return j                
        

def quickSort(l,h):
    
    if(l<h):
    
        j=partition(l,h)
        quickSort(l,j)
        quickSort(j+1,h)       
        
   


def measureSearchPerformance(searchFunction,arraySize,iterations=100):
    total_time = timeit.timeit(lambda : searchFunction(list(range(arraySize)), random.randint(0,arraySize-1)), number=iterations)
    return total_time/iterations

A = [1000,2000,4000,8000,16000,32000]

for size in  A:
    avg_time = measureSearchPerformance(linearSearch,size)
    print(f'Average time for linear search on array {size}: ~ {avg_time} seconds')
    