#import json
#import itertools

#expression = input("Enter a arithmetic S-expression: ")

#def getIntegers(string):

    #container = [i.split() for i in expression]
    ##return digit


#print(getIntegers(expression))

#if (container.contains('+')):*/

import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def tokenize(expression):
    return expression.replace('(', ' ( ').replace(')', ' ) ').split()

def evaluate(tokens):
    stack = Stack()
    tokens = tokens[::-1]  # Reverse the list for easier stack usage

    while tokens:
        token = tokens.pop()

        if token in '()+-*/':
            stack.push(token)
        else:  # Token is a number
            stack.push(int(token))

        if token == ')':
            # Perform calculation
            stack.pop()  # Remove ')'
            right = stack.pop()
            op = stack.pop()
            left = stack.pop()
            stack.pop()  # Remove '('

            if op == '+':
                stack.push(left + right)
            elif op == '-':
                stack.push(left - right)
            elif op == '*':
                stack.push(left * right)
            elif op == '/':
                stack.push(left / right)

    return stack.pop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py 'expression'")
        sys.exit(1)

    expression = sys.argv[1]
    tokens = tokenize(expression)
    result = evaluate(tokens)
    print(result)
