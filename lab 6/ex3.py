class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		
def evaluate(root):
	if root is None:
		return 0
	
	if root.left is None and root.right is None:
		return int(root.value)
	
	left_sum = evaluate(root.left)
	right_sum = evaluate(root.right)
	
	if root.value == '+':
		return left_sum + right_sum
	elif root.value == '-':
		return left_sum - right_sum
	elif root.value == '*':
		return left_sum * right_sum
	elif root.value == '/':
		return left_sum / right_sum
	
def buildTree(tokens):
	stack = []
	
	for token in tokens:
		if token in "*/+-":
			node = Node(token)
			node.right = stack.pop()
			node.left = stack.pop()
			stack.append(node)
			
		elif token not in "()":
			stack.append(Node(token))
			
		elif token == '(':
			expression = []
			while stack and stack[-1].value != ')':
				expression.append(stack.pop().value)
			if stack:
				stack.pop()  # Remove the ')'
			root = buildTree(expression)
			stack.append(root)
			
	return stack[0] if stack else None

expression = input("Enter the expression: ").split()
root = buildTree(expression[::-1])
print(root)
result = evaluate(root)

print(result)


	



	