import timeit

# Function to calculate the n-th power of 2
def pow2(n):
    return 2 ** n

# Time the execution of 10000 instances of pow2(10000)
start_time = timeit.default_timer()
for _ in range(10000):
    pow2(10000)
end_time = timeit.default_timer()
print(f"Time taken for 10000 instances of pow2(10000): {end_time - start_time} seconds")

# Function to compute pow2(n) for n up to 1000 using a for loop
def compute_with_loop():
    results = []
    for i in range(1001):
        results.append(pow2(i))
    return results

# Function to compute pow2(n) for n up to 1000 using list comprehension
def compute_with_list_comprehension():
    return [pow2(i) for i in range(1001)]

# Time the execution of 1000 instances of each approach
start_time = timeit.default_timer()
for _ in range(1000):
    compute_with_loop()
end_time = timeit.default_timer()
print(f"Time taken for 1000 instances of compute_with_loop: {end_time - start_time} seconds")

start_time = timeit.default_timer()
for _ in range(1000):
    compute_with_list_comprehension()
end_time = timeit.default_timer()
print(f"Time taken for 1000 instances of compute_with_list_comprehension: {end_time - start_time} seconds")
