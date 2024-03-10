class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		
def evaluate(root):
	if root is None:
		return 0
	
	if root.left is None and root.right is None:
		return root.value
	
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
	
def buildTree(expression):
	precedence = {'+':1, '-':1, '*':2, '/':2}
	operators = ['+', '-', '*', '/']
	stack = []
	operandStack = []
	
	for token in expression:
		if token.isdigit():
			operandStack.append(Node(int(token)))
		elif token in operators:
			while stack and stack[-1] != '(' and precedence[token] <= precedence[stack[-1]]:
				right = operandStack.pop()
				left = operandStack.pop()
				op = stack.pop()
				operator = Node(op)
				operator.left = left
				operator.right = right
				operandStack.append(operator)
			stack.append(token)
		elif token == '(':
			stack.append(token)
		elif token == ')':
			while stack and stack[-1] != '(':
				right = operandStack.pop()
				left = operandStack.pop()
				op = stack.pop()
				operator = Node(op)
				operator.left = left
				operator.right = right
				operandStack.append(operator)
			stack.pop()  # discard '('
			
	while stack:
		right = operandStack.pop()
		left = operandStack.pop()
		op = stack.pop()
		operator = Node(op)
		operator.left = left
		operator.right = right
		operandStack.append(operator)
		
	return operandStack.pop() if operandStack else None

expression = input("Enter the expression: ").split()
root = buildTree(expression)
result = evaluate(root)
print(result)


	



	