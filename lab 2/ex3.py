import timeit
import cProfile
import re

def sub_function(n):
  if n == 0:
    return 1
  else:
    return n * sub_function(n-1)
  
def test_function():
  data = []
  for i in range(10):
    data.append(sub_function(i))
  return data

def third_function():
  return [i**2 for i in range(100000000)]

# Create a profiler object
profiler = cProfile.Profile()

profiler.runcall(test_function)
profiler.print_stats()

profiler.runcall(third_function)
profiler.print_stats()


#1. A profile is a set of statistics that describes how often and for how long various parts of the program executed.
#The profiler modules are designed to provide an execution profile for a given program
#
#2. In summary, profiling is about understanding the behavior of your program and finding out where to optimize, 
#while benchmarking is about comparing the performance of different systems or versions of a system.
#
#4. 
# tottime: the total time spent in the function excluding time made in calls to sub-functions.
# percall(1): the time per call, calculated as tottime divided by ncalls.
# cumtime: the cumulative time spent in this and all subfunctions. This figure is accurate even for recursive functions.
# percall(2): the cumulative time per primitive call, calculated as cumtime divided by ncalls.