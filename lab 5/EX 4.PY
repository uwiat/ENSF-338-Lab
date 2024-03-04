import random
import timeit
import matplotlib.pyplot as plt
class ArrayQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
       
        self.items.insert(0, item)

    def dequeue(self):
        if not self.items:
            raise Exception("Dequeuing from an empty queue")
        
        return self.items.pop()



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            
            new_node.next = self.head
            self.head = new_node
        
        if not self.tail:
            self.tail = new_node

    def dequeue(self):
        if not self.head:
            raise Exception("Dequeuing from an empty queue")
        
        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next
        
        if prev:
            prev.next = None
            self.tail = prev
        else:
            self.head = None
            self.tail = None
        return current.data



def generate_random_tasks_for_linked_list(num_tasks):
    tasks = []
    for _ in range(num_tasks):
        task = LinkedListQueue()
        task = random.choices([f"task.enqueue", f"task.dequeue"], weights=[0.7, 0.3])[0]
        tasks.append(task)
    return tasks

def generate_random_tasks_for_array(num_tasks):
    tasks = []
    for _ in range(num_tasks):
        task = ArrayQueue()
        task = random.choices([f"task.enqueue", f"task.dequeue"], weights=[0.7, 0.3])[0]
        tasks.append(task)
    return tasks

def measure_performance_array(num_lists, num_tasks):
    array_times = []
    for _ in range(num_lists):
        start_time = timeit.default_timer()
        generate_random_tasks_for_array(num_tasks)
        end_time = timeit.default_timer()
        array_times.append(end_time - start_time)
    return array_times

def measure_performance_linkedlist(num_lists, num_tasks):
    linked_times = []
    for _ in range(num_lists):
        start_time = timeit.default_timer()
        generate_random_tasks_for_linked_list(num_tasks)
        end_time = timeit.default_timer()
        linked_times.append(end_time - start_time)
    return linked_times

num_lists = 100
num_tasks = 10000

array_times = measure_performance_array(num_lists, num_tasks)
linked_times = measure_performance_linkedlist(num_lists, num_tasks)

average_array_times = sum(array_times)/len(array_times)
average_linked_times = sum(linked_times)/len(linked_times)

print(f"average time of enqueue and dequeue for 100 arrays is {average_array_times}")
print(f"average time of enqueue and dequeue for 100 linked list is {average_linked_times}")

def plot_results(linked_times, array_times):
    
    num_lists = len(linked_times)  
    list_indices = list(range(1, num_lists + 1))

    plt.hist(list_indices, bins=10, fc='none', edgecolor='blue', weights=linked_times, label='Linked List')
    plt.hist(list_indices, bins=10, fc='none', edgecolor='red', weights=array_times, label='Array')

    plt.xlabel('List Index')
    plt.ylabel('Runtime (seconds)')
    plt.title('Performance of enqueue and dequeue Operations')
    plt.legend()
    plt.show()



plot_results(linked_times, array_times)
#Q5: Generally the times for enqueue and dequeue  from an linked list is faster:
#Linked List (enqueue from Head and dequeue from tail): enqueue from Head and dequeue from tail of a linked list is  
#faster compared to enqueue at the head, and dequeue from the tail of an array. These operations have a time complexity of O(1) because 
#they involve only updating the head pointer (for enqueue) or updating the tail pointer (for dequeue). 
#Array (enqueue from Head and dequeue from tail): enqueue from Head has time complexity of O(n) because when enqueueing an element 
#at the head of the array, you need to shift all existing elements to the right by one position to make space for the 
#new element at the head. Dequeue from tail of an array has a time complexity of O(1) because when dequeuing an element from 
#the tail of the array, you simply remove the last element from the array.
#However, if resizing is required due to lack of space, it may involve copying elements, 
#leading to a time complexity of O(n), where n is the number of elements in the array.




 

