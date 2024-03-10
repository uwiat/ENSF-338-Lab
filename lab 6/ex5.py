import random
import timeit

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = ListNode(value)
        if not self.head or value <= self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.value < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

class Heap:
    def __init__(self):
        self.heap_array = []

    def heapify(self, arr):
        self.heap_array = arr[:]
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i, n)

    def heapify_down(self, index, size):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index
        if left_child < size and self.heap_array[left_child] > self.heap_array[largest]:
            largest = left_child
        if right_child < size and self.heap_array[right_child] > self.heap_array[largest]:
            largest = right_child
        if largest != index:
            self.heap_array[index], self.heap_array[largest] = self.heap_array[largest], self.heap_array[index]
            self.heapify_down(largest, size)

    def enqueue(self, value):
        self.heap_array.append(value)
        current_index = len(self.heap_array) - 1
        parent_index = (current_index - 1) // 2
        while current_index > 0 and self.heap_array[current_index] > self.heap_array[parent_index]:
            self.heap_array[current_index], self.heap_array[parent_index] = self.heap_array[parent_index], self.heap_array[current_index]
            current_index = parent_index
            parent_index = (current_index - 1) // 2

    def dequeue(self):
        if not self.heap_array:
            return None
        root = self.heap_array[0]
        self.heap_array[0] = self.heap_array[-1]
        del self.heap_array[-1]
        self.heapify_down(0, len(self.heap_array))
        return root

class HeapPriorityQueue(Heap):
    def enqueue(self, value):
        super().enqueue(value)  

    def dequeue(self):
        return super().dequeue()  


def process_tasks(pq, tasks):
    times = []
    for task, value in tasks:
        start_time = timeit.default_timer()
        if task == 'enqueue':
            pq.enqueue(value)
        else:
            pq.dequeue()
        end_time = timeit.default_timer()
        times.append(end_time - start_time)
    return times
# Generate random list of tasks
tasks = []
for _ in range(1000):
    if random.random() < 0.7:  
        tasks.append(('enqueue', random.randint(1, 1000)))
    else:  
        tasks.append(('dequeue', None))


list_pq = ListPriorityQueue()
list_times = process_tasks(list_pq, tasks)
list_times_average = sum(list_times) / len(list_times)



heap_pq = HeapPriorityQueue()
heap_times = process_tasks(heap_pq, tasks)
heap_times_average = sum(heap_times) / len(heap_times)


print("ListPriorityQueue average execution time:", list_times_average)
print("HeapPriorityQueue average execution time:", heap_times_average)

#Q4he heap-based priority queue is expected to be faster because The enqueue operation for a heap-based priority 
#queue has a time complexity of O(log n), and the dequeue operation has a time complexity of O(log n), 
#where n is the number of elements in the heap. On the other hand, for a linked list-based priority queue, 
#both enqueue and dequeue operations may have a time complexity of O(n) in the worst case, as we might need to traverse 
#the list to find the correct position for insertion or removal.
