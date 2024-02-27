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
			print("dequeue None")
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
			print("peek None")
			return None
		else:
			print(f"peek {self.queue[self.head]}")
			return self.queue[self.head]
		
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
		
class CircularQueueLinkedList:
	def __init__(self):
		self.front = None
		self.rear = None
		
	def enqueue(self, value):
		new_node = Node(value)
		if self.front is None:
			self.front = new_node
			self.rear = new_node
			new_node.next = self.front
		else:
			new_node.next = self.front
			self.rear.next = new_node
			self.rear = new_node
		print(f"enqueue {value}")
		
	def dequeue(self):
		if self.front is None:
			print("dequeue None")
			return None
		value = self.front.data
		if self.front == self.rear:
			self.front = self.rear = None
		else:
			self.front = self.front.next
			self.rear.next = self.front
		print(f"dequeue {value}")
		return value
	
	def peek(self):
		if self.front is None:
			print("peek None")
			return None
		print(f"peek {self.front.data}")
		return self.front.data
	

# Testing CircularQueue
cq = CircularQueue(5)

cq.enqueue(1)  # Expected output: "enqueue 1"
cq.enqueue(2)  # Expected output: "enqueue 2"
cq.enqueue(3)  # Expected output: "enqueue 3"
cq.enqueue(4)  # Expected output: "enqueue 4"
cq.enqueue(5)  # Expected output: "enqueue 5"
cq.enqueue(6)  # Expected output: "enqueue None" (Queue is full)

cq.peek()  # Expected output: "peek 1"

cq.dequeue()  # Expected output: "dequeue 1"
cq.dequeue()  # Expected output: "dequeue 2"
cq.dequeue()  # Expected output: "dequeue 3"
cq.dequeue()  # Expected output: "dequeue 4"
cq.dequeue()  # Expected output: "dequeue 5"
cq.dequeue()  # Expected output: "dequeue None" (Queue is empty)

cq.peek()  # Expected output: "peek None" (Queue is empty)

cq.enqueue(7)  # Expected output: "enqueue 7"
cq.enqueue(8)  # Expected output: "enqueue 8"
cq.enqueue(9)  # Expected output: "enqueue 9"
cq.enqueue(10)  # Expected output: "enqueue 10"
cq.enqueue(11)  # Expected output: "enqueue 11"
cq.enqueue(12)  # Expected output: "enqueue None" (Queue is full)

cq.peek()  # Expected output: "peek 7"

cq.dequeue()  # Expected output: "dequeue 7"
cq.dequeue()  # Expected output: "dequeue 8"
cq.dequeue()  # Expected output: "dequeue 9"
cq.dequeue()  # Expected output: "dequeue 10"
cq.dequeue()  # Expected output: "dequeue 11"
cq.dequeue()  # Expected output: "dequeue None" (Queue is empty)

cq.peek()  # Expected output: "peek None" (Queue is empty)

# Testing CircularQueueLinkedList
cql = CircularQueueLinkedList()

cql.enqueue(1)  # Expected output: "enqueue 1"
cql.enqueue(2)  # Expected output: "enqueue 2"
cql.enqueue(3)  # Expected output: "enqueue 3"
cql.enqueue(4)  # Expected output: "enqueue 4"
cql.enqueue(5)  # Expected output: "enqueue 5"

cql.peek()  # Expected output: "peek 1"

cql.dequeue()  # Expected output: "dequeue 1"
cql.dequeue()  # Expected output: "dequeue 2"
cql.dequeue()  # Expected output: "dequeue 3"
cql.dequeue()  # Expected output: "dequeue 4"
cql.dequeue()  # Expected output: "dequeue 5"
cql.dequeue()  # Expected output: "dequeue None" (Queue is empty)

cql.peek()  # Expected output: "peek None" (Queue is empty)

cql.enqueue(6)  # Expected output: "enqueue 6"
cql.enqueue(7)  # Expected output: "enqueue 7"
cql.enqueue(8)  # Expected output: "enqueue 8"
cql.enqueue(9)  # Expected output: "enqueue 9"
cql.enqueue(10)  # Expected output: "enqueue 10"

cql.peek()  # Expected output: "peek 6"

cql.dequeue()  # Expected output: "dequeue 6"
cql.dequeue()  # Expected output: "dequeue 7"
cql.dequeue()  # Expected output: "dequeue 8"
cql.dequeue()  # Expected output: "dequeue 9"
cql.dequeue()  # Expected output: "dequeue 10"
cql.dequeue()  # Expected output: "dequeue None" (Queue is empty)

cql.peek()  # Expected output: "peek None" (Queue is empty)


	