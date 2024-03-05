import timeit
import random
#Ex 1.1
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        
        currentNode = self.root
        while True:
            if key < currentNode.val:
                if currentNode.left is None:
                    currentNode.left = Node(key)
                    break
                currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = Node(key)
                    break
                currentNode = currentNode.right


    def insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert_recursive(node.right, key)

    def search(self, key):
        currentNode = self.root
        while currentNode:
            if key == currentNode.val:
                return currentNode  # Found the key
            elif key < currentNode.val:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return None  # Key not found

    def search_recursive(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self.search_recursive(node.left, key)
        else:
            return self.search_recursive(node.right, key)

#Ex 1.2 and 1.3
# Generate a sorted vector of 10000 elements
sorted_vector = list(range(1, 10001))
bst = BST()

# Insert each element into the BST
for elem in sorted_vector:
    bst.insert(elem)

# Function to time the search operation
def time_search_operation(bst, elem):
    start = timeit.default_timer()
    bst.search(elem)
    return timeit.default_timer() - start

# Measure search performance on the sorted vector
total_time_sorted = 0
for elem in sorted_vector:
    total_time_sorted += sum(time_search_operation(bst, elem) for _ in range(10)) / 10
average_time_sorted = total_time_sorted / len(sorted_vector)

# Shuffle the vector
random.shuffle(sorted_vector)

# Measure search performance on the shuffled vector
total_time_shuffled = 0
for elem in sorted_vector:
    total_time_shuffled += sum(time_search_operation(bst, elem) for _ in range(10)) / 10
average_time_shuffled = total_time_shuffled / len(sorted_vector)

print(f"Average search time (sorted): {average_time_sorted}")
print(f"Total search time (sorted): {total_time_sorted}")
print(f"Average search time (shuffled): {average_time_shuffled}")
print(f"Total search time (shuffled): {total_time_shuffled}")

#Ex 1.4
# The conclusion according to the results is that the average and total time for 
# a shuffled search time is marginally lower than the sorted search time. This is 
# because the performance of the binary search tree depends on its height which is 
# usually logarithmic to the number of elements for balanced trees but can degrade 
# to linear with unbalanced trees.
#
# The excercise highlights the importance of balancing Binary Search Trees, a 
# balanced Binary tree ensures that search operations remain efficient regardless 
# of elements insertion or search order.