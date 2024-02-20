1. timeit.timeit() runs the code snippet a specified number of times and returns the total elapsed time. This approach is
useful when you want to measure the time taken by a function to execute a certain number of times. It helps to average out
the noise that might be caused by other processes running on the system.
timeit.repeat() runs the timeit() method several times and returns a list of results. This approach is useful when you want
to see the distribution of times and not just the average. It helps to identify outliers and understand the variability in
the execution time.

2. For timeit.timeit(), the output is the total time for all runs, so it’s appropriate to divide this by the number of runs
to get the average time per run.
For timeit.repeat(), since it returns a list of times, you can use min, max, and average to understand the distribution of
times. The min can give you the best-case scenario (least noise), the max can show you the worst-case scenario (most noise),
and the average can give you the typical case.