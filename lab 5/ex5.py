class CircularQueue:
	def __init__(self, max_size):
		self.max_size = max_size
		self.queue = [None] * max_size # Initialize the queue
		self.head = self.tail = -1 # Initialize the pointers
		
	def enqueue(self, value):
		# (self.tail + 1) % self.max_size calculates the next valid position for inserting an element
		if (self.tail + 1) % self.max_size == self.head:
			print("enqueue None")  # Queue is full
		else:
			if self.head == -1:
				# Insert the first element
				self.head = self.tail = 0
				self.queue[self.tail] = value
			else:
				self.tail = (self.tail + 1) % self.max_size
				self.queue[self.tail] = value
			print(f"enqueue {value}")
			
	def dequeue(self):
		if self.head == -1:
			print("dequeue None")  # Queue is empty
			return None
		else:
			value = self.queue[self.head]
			if self.head == self.tail:
				self.head = self.tail = -1
			else:
				self.head = (self.head + 1) % self.max_size
			print(f"dequeue {value}")
			return value
		
	def peek(self):
		if self.head == -1:
			print("peek None")  # Queue is empty
			return None
		else:
			print(f"peek {self.queue[self.head]}")
			return self.queue[self.head]
		
# Example usage
if __name__ == "__main__":
	cq = CircularQueue(max_size=5)
	cq.enqueue(10)
	cq.enqueue(20)
	cq.enqueue(30)
	cq.dequeue()
	cq.peek()
	cq.enqueue(40)
	cq.enqueue(50)
	cq.enqueue(60)  # Queue is full
	cq.dequeue()
	cq.peek()
	print(cq.queue)
	
	

	