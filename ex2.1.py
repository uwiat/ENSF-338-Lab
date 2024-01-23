import sys
import math
# (i) The code is intended to solve a quadratic function, and the roots are determined by the value of d
def do_stuff():
	a = float(sys.argv[1])
	b = float(sys.argv[2])
	c = float(sys.argv[3])
	d = b**2 - 4*a*c
	
	if d > 0:
		root1 = (-b + math.sqrt(d)) / (2*a)
		root2 = (-b - math.sqrt(d)) / (2*a)
		print(f'The solutions are: {root1}, {root2}')
	elif d == 0:
		root = -b / (2*a)
		print(f'The solution is: {root}')
		# (ii) the quotation mark used in print(f'The solution is: {root}’), are different
	else:
		print('There are no real solutions.')
		
do_stuff()

