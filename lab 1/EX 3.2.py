import json
import timeit
import numpy as np
import matplotlib.pyplot as plt

new_size = 42
num_records_to_process = [1000, 2000, 5000, 10000]
num_iterations = 100
processing_times = []

for num_records in num_records_to_process:
    total_time = 0

    for _ in range(num_iterations):
        with open('pg2701.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Select only the lines up to the specified number of records
        records = lines[40:40 + num_records]

        # Assume each line is a record and split it into fields
        records = [record.split() for record in records]

        # Time the operation of modifying the size value in each record
        start_time = timeit.default_timer()
        for record in records:
            
            record = str(new_size)  
        end_time = timeit.default_timer()

        total_time += end_time - start_time

    average_time = total_time / num_iterations
    print(f"Average time taken to modify size value in each record for {num_records} records over {num_iterations} runs: {average_time} seconds")
    
    processing_times.append(average_time)

# Convert lists to NumPy arrays for linear regression
num_records_array = np.array(num_records_to_process)
processing_times_array = np.array(processing_times)

# Compute linear regression to find the slope and intercept
slope, intercept = np.polyfit(num_records_array, processing_times_array, 1)

# Generate line values using the slope and intercept
line_values = slope * num_records_array + intercept

# Scatter plot of the data
plt.scatter(num_records_array, processing_times_array, label='Data')

# Plot the regression line
plt.plot(num_records_array, line_values, 'r', label=f'Linear Regression: t = {slope:.2e} * n + {intercept:.2e}')

# Label the axes and add a legend
plt.xlabel('Number of Records')
plt.ylabel('Average Processing Time')
plt.legend()

# Show the plot
plt.show()

# Finally, print out the linear relationship between the number of records and processing time
print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))
