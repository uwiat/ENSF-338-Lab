import random
import timeit
import matplotlib.pyplot as plt
class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise Exception("Popping from an empty stack")
        return self.items.pop()

    def __len__(self):
        return len(self.items)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            raise Exception("Popping from an empty stack")
        popped_item = self.head.data
        self.head = self.head.next
        return popped_item



def generate_random_tasks_for_linked_list(num_tasks):
    tasks = []
    for _ in range(num_tasks):
        LinkedListStack()
        task = random.choices([f"task.push", f"task.pop"], weights=[0.7, 0.3])[0]
        tasks.append(task)
    return tasks

def generate_random_tasks_for_array(num_tasks):
    tasks = []
    for _ in range(num_tasks):
        task = ArrayStack()
        task = random.choices([f"task.push", f"task.pop"], weights=[0.7, 0.3])[0]
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

print(f"average time of push and pop for 100 arrays is {average_array_times}")
print(f"average time of push and pop for 100 linked list is {average_linked_times}")

def plot_results(linked_times, array_times):
    
    num_lists = len(linked_times)  
    list_indices = list(range(1, num_lists + 1))

    plt.hist(list_indices, bins=10, fc='none', edgecolor='blue', weights=linked_times, label='Linked List')
    plt.hist(list_indices, bins=10, fc='none', edgecolor='red', weights=array_times, label='Array')

    plt.xlabel('List Index')
    plt.ylabel('Runtime (seconds)')
    plt.title('Performance of Push and Pop Operations')
    plt.legend()
    plt.show()



plot_results(linked_times, array_times)
#Q5: Generally the times for pushing and popping from an array vs linked list are very similar:
#Linked List (Push and Pop from Head): Pushing and popping from the head of a linked list is generally faster compared to 
#pushing and popping from the tail of an array. These operations have a time complexity of O(1) because they involve only 
#updating the head pointer (for push) or removing the first node (for pop). 
#Array (Push and Pop from Tail): Pushing and popping from the tail of an array also typically have a time complexity of O(1) 
#when there's available space in the array. However, if resizing is required due to lack of space, it may involve copying elements, 
#leading to a time complexity of O(n), where n is the number of elements in the array.




 

