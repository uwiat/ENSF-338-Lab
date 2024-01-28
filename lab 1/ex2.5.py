import json
import timeit

new_size = 42
total_time = 0

for _ in range(10):
    with open('pg2701.txt', 'r') as file:
        lines = file.readlines()

    # Select only the lines from 41 to 312 (Python uses 0-based indexing)
    records = lines[40:312]

    # Assume each line is a record and split it into fields
    records = [record.split() for record in records]

    # Time the operation of modifying the size value in each record
    start_time = timeit.default_timer()
    for record in records:
        record = str(new_size)
    end_time = timeit.default_timer()

    total_time += end_time - start_time

    records.reverse()

    # Write the records as JSON objects to the file
    with open('output.2.3.json', 'w') as file:
        json.dump(records, file)

print(f"Average time taken to modify size value in each record over 10 runs: {total_time / 10} seconds")
