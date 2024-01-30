#Q1 This is a recursive function that calculates the nth Fibonacci number. 
#It recursively calculates the (n-1)th and (n-2)th Fibonacci numbers and returns their sum.

#Q2 No it is not divide and conquer method

#Q3 O(2^n)

import timeit
import numpy as np
import matplotlib.pyplot as plt




n_values = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
fib = [-1] * (max(n_values) + 1)

# Q4
def func2(n, fib):
    if n == 0 or n == 1:
        return n
    elif fib[n] != -1:
        return fib[n]
    else:
        fib[n] = func2(n-1, fib) + func2(n-2, fib)
        return fib[n]

# Q5 O(n)

# Q6
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def plot1():
  
    original_times = []

    for n in n_values:
        start_time = timeit.default_timer()
        func(n)
        original_times.append(timeit.default_timer() - start_time)

   
    plt.plot(n_values, original_times, label='Original')
    plt.xlabel('Input (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.savefig("ex1.6.1.jpg")
    plt.show()
   
   

def plot2():
    
    improved_times = []

    for n in n_values:
        start_time = timeit.default_timer()
        func2(n, fib)
        improved_times.append(timeit.default_timer() - start_time)

   
    plt.plot(n_values, improved_times, label='Improved')
    plt.xlabel('Input (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.savefig("ex1.6.2.jpg")
    plt.show()
   
    

# Call the plotting functions
plot1()
plot2()




