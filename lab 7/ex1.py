import random
import time
import matplotlib.pyplot as plt

# 1. Binary search tree with insertion and search operations 
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        
def insert(data, root=None):
    current = root
    parent = None
    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right
    if root is None:
        root = Node(data)
    elif data <= parent.data:
        parent.left = Node(data, parent)
    else:
        parent.right = Node(data, parent)
    return root

def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data <= current.data:
            current = current.left
        else:
            current = current.right
    return None

# 2. Measure balance
def height(node):
    if node is None:
        return -1
    else:
        return 1 + max(height(node.left), height(node.right))
    
def balance(node):
    if node is None:
        return 0
    else:
        return height(node.left) - height(node.right)
    
    
    
# 3. Generate a 1000 random search tasks
def generate_search_tasks(n_tasks, n_numbers):
    tasks = []
    numbers = list(range(n_numbers))
    
    for _ in range(n_tasks):
        random.shuffle(numbers)
        tasks.append(numbers.copy())
        
    return tasks


# 4. Measure average performance and largest absolute balance value
def max_balance(node):
    if node is None:
        return 0
    else:
        return max(abs(balance(node)), max_balance(node.left), max_balance(node.right))
    
def measure_performance(tasks):
    balance_values = []
    search_times = []
    for i, task in enumerate(tasks, start=1):
        root = None
        for number in task:
            root = insert(number, root)
            
        start_time = time.time()
        for number in task:
            search(number, root)
        end_time = time.time()
        
        avg_search_time = (end_time - start_time) / len(task)
        largest_balance = max_balance(root)
        
        balance_values.append(largest_balance)
        search_times.append(avg_search_time)
        
        print(f"Task {i}: Average search time = {avg_search_time}, Largest absolute balance = {largest_balance}")        
            
    # 5. Scatterplot
    plt.scatter(balance_values, search_times)
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time')
    plt.title('Scatterplot of Search Time vs Absolute Balance')
    plt.show()


tasks = generate_search_tasks(1000, 1000)
measure_performance(tasks)




        