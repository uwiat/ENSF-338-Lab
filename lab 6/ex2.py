import timeit
import random

#EX: 2.1

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        currentNode = self.root
        while currentNode:
            if key == currentNode.val:
                return currentNode
            elif key < currentNode.val:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return None

def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return None



#EX: 2.2

# Measuring search performance in BST
def measure_search_bst(bst, elements):
    total_time = 0
    for elem in elements:
        start_time = timeit.default_timer()
        for _ in range(10):
            bst.search(elem)
        total_time += timeit.default_timer() - start_time
    avg_time = total_time / (len(elements) * 10)
    return avg_time, total_time

# Sorting the vector for binary search


# Measuring search performance in a sorted array using binary search
def measure_search_array(arr, elements):
    total_time = 0
    for elem in elements:
        start_time = timeit.default_timer()
        for _ in range(10):
            binary_search(arr, elem)
        total_time += timeit.default_timer() - start_time
    avg_time = total_time / (len(elements) * 10)
    return avg_time, total_time



#EX: 2.3
# Generate a 10000-element sorted vector, shuffle, and use it to build a tree
vector = list(range(1, 10001))
random.shuffle(vector)

# Building the BST
bst = BST()
for elem in vector:
    bst.insert(elem)

# Measure BST Search Performance
bst_avg_time, bst_total_time = measure_search_bst(bst, vector)
print(f'Binary Search Tree Search - Average Time: {bst_avg_time}, Total Time: {bst_total_time}')

# Shuffle, sort the vector, and measure binary search performance
random.shuffle(vector)  # Shuffle before sorting to simulate the scenario described
vector.sort()

# Measure Binary Search Performance
array_avg_time, array_total_time = measure_search_array(vector, vector)
print(f'Array Binary Search - Average Time: {array_avg_time}, Total Time: {array_total_time}')


#EX: 2.4

#The faster approach was shown to be Binary Search tree both in Average time and total time
#This mostly depends on how balanced the tree is for the binary search tree method. Binary 
#search trees offer advantages in different scenarios involving frequent insertions and deletions
#where maintaining a sorted array would be less efficient proving to be a circumstantial outcome.