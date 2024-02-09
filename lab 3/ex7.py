import timeit 
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import json
# Ex 7.1
f = open(r'c:\Users\azmat\Desktop\Ucal\Y2\S2\ENSF338\ENSF-338-Lab\lab 3\ex7data.json', 'r')


my_array = json.load(f)

def binarySearch(x,key, mid1):
    l= 0; h=len(x) - 1
    firstIteration = True;
    
    while (l <= h):
            if firstIteration:
                mid = mid1
                firstIteration = False 
            else:
                mid = (l+h)//2
            if (key==x[mid]):
                return mid
            elif (key < x[mid]):
                h = mid - 1
                
            else:
                l = mid+1
                
        
    return -1


A = [2230,2000,8000,5000,16000,7000]

# Ex 7.2
results=[]
indexOfMidpoints = []
for midpoint in range(0,999997,100000):
    x = timeit.timeit(lambda:binarySearch(my_array,2000,midpoint))
    results.append(x)
    indexOfMidpoints.append(midpoint)


print(results)
best_result= np.min(results)
bestResultIndex = results.index(best_result)
bestResultIndex = bestResultIndex*100000
print('The best result out of the average of ten runs of the task is ',best_result)
print('The midpoint correlating to this time is ',bestResultIndex)

plt.scatter(indexOfMidpoints, results, color='blue', label='Execution Time')
plt.title('Execution Time by Midpoint Index')
plt.xlabel('Midpoint Index')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.grid(True)
plt.show()

f.close()

# On average the initial midpoint increases proportionally to the performance time of 
# the program, I think this is due to the need for a larger number of passes for larger 
# midpoints within the array. 