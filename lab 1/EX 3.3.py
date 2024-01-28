import json
import timeit
import numpy as np
import matplotlib.pyplot as plt

new_size = 42
num_records_to_process = 1000
num_repeats = 1000

# Timing the processing of the first 1000 records 1000 times using timeit's repeat function
processing_times = timeit.repeat(
    stmt="""
with open('pg2701.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Select only the lines up to the specified number of records
records = lines[40:40 + num_records_to_process]

# Assume each line is a record and split it into fields
records = [record.split() for record in records]

# Time the operation of modifying the size value in each record
for record in records:
    
    record = str(new_size)  
    """,
    setup=f"""
import json
new_size = {new_size}
num_records_to_process = {num_records_to_process}
with open('pg2701.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
""",
    repeat=num_repeats,
    number=1
)

# Plotting the histogram
plt.hist(processing_times, bins=20, edgecolor='black')
plt.xlabel('Processing Time (seconds)')
plt.ylabel('Frequency')
plt.title(f'Distribution of Processing Times for {num_records_to_process} records (Repeated {num_repeats} times)')
plt.savefig('output.3.3.png')
plt.show()
