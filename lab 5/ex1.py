import re

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0

def preprocess_expression(expression):
   
    tokens = re.findall(r'\d+|[-+*/()]', expression)
    return tokens

def eval_expression(tokens):
    stack = Stack()
    operators = '+-*/'
    
    for token in reversed(tokens):
        if token in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(operand1 / operand2)
        elif token.isdigit():
            stack.push(int(token))
    
    return stack.pop()

if __name__ == "__main__":
    expression = input("Enter the expression: ")
    tokens = preprocess_expression(expression)
    result = eval_expression(tokens)
    print(result)
