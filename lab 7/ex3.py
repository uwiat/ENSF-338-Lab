class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

def _left_rotate(root, x):
    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x
    y.parent = x.parent
    if x.parent is None:  # x is root
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
    return root, y  # Return the new root if changed, and the new sub-root

def _right_rotate(root, x):
    y = x.left
    x.left = y.right
    if y.right is not None:
        y.right.parent = x
    y.parent = x.parent
    if x.parent is None:  # x is root
        root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y
    return root, y  # Return the new root if changed, and the new sub-root

def insert(data, root=None):
    current = root
    parent = None
    pivot = None
    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    if root is None:
        root = Node(data)
    else:
        if data <= parent.data:
            parent.left = Node(data, parent)
        else:
            parent.right = Node(data, parent)

        # Adjust the tree balance starting from the new node's parent
        current = parent
        while current is not None:
            if abs(balance(current)) > 1:
                pivot = current
                break
            current = current.parent

    # Check if pivot exists and apply rotations if necessary
    if pivot is not None:
        # Case 3A: Left-Left or Right-Right situation
        if (pivot.left and data < pivot.left.data) or (pivot.right and data > pivot.right.data):
            print("Case #3a: adding a node to an outside subtree")
            if pivot.left and data < pivot.left.data:
                root, _ = _right_rotate(root, pivot)
            else:
                root, _ = _left_rotate(root, pivot)
        else:
            print("Case 3b not supported")

    return root

# Note: The height and balance functions remain unchanged from your previous implementation.

def height(node):
    """Calculate the height of a node."""
    if node is None:
        return -1
    else:
        return 1 + max(height(node.left), height(node.right))

def balance(node):
    """Calculate the balance factor of a node."""
    if node is None:
        return 0
    else:
        return height(node.left) - height(node.right)

def print_tree(node, level=0, prefix="Root:"):
    """Recursively print the tree structure."""
    if node is not None:
        print(' ' * (level*4) + prefix + str(node.data))
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "L---")
            print_tree(node.right, level + 1, "R---")

def search(data, root):
    """Search for a node with the specified data in the AVL tree."""
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None

# Example Usage
if __name__ == "__main__":
    root = None
    numbers = [20, 4, 26, 3, 9, 15, 30, 2, 7, 11]

    for number in numbers:
        root = insert(number, root)
    
    print("AVL Tree after insertions:")
    print_tree(root)

    # Optionally, print balance factors to see how balanced the tree is after insertions
    print("\nBalance Factors after insertions:")
    for number in numbers:
        node = search(number, root)  # Assuming a search function is defined
        if node:
            print(f"Node {node.data} Balance: {balance(node)}")
