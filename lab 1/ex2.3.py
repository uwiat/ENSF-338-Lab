import json

new_size = 42

with open('pg2701.txt', 'r') as file:
    lines = file.readlines()
    
# Select only the lines from 41 to 312 (Python uses 0-based indexing)
records = lines[40:312]

# Assume each line is a record and split it into fields
records = [record.split() for record in records]

for record in records:
    record = str(new_size)
    
records.reverse()

# Write the records as JSON objects to the file
with open('output.2.3.json', 'w') as file:
    json.dump(records, file)
    
        
    
    
    
    
    

    
    