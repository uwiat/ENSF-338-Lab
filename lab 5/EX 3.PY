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

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count



def generate_random_tasks(num_tasks, name):
    tasks = []
    for _ in range(num_tasks):
        task = random.choices([f"push.{name}", f"pop.{name}"], weights=[0.7, 0.3])[0]
        tasks.append(task)
    return tasks

def measure_performance_array(num_lists, num_tasks, name):
    array_times = []
    for _ in range(num_lists):
        start_time = timeit.default_timer()
        generate_random_tasks(num_tasks, name)
        end_time = timeit.default_timer()
        array_times.append(end_time - start_time)
    return array_times

def measure_performance_linkedlist(num_lists, num_tasks, name):
    linked_times = []
    for _ in range(num_lists):
        start_time = timeit.default_timer()
        generate_random_tasks(num_tasks, name)
        end_time = timeit.default_timer()
        linked_times.append(end_time - start_time)
    return linked_times

num_lists = 100
num_tasks = 10000

array_times = measure_performance_array(num_lists, num_tasks, "ArrayStack")
linked_times = measure_performance_linkedlist(num_lists, num_tasks, "LinkedListStack")

def plot_results(linked_times, array_times):
    list_sizes = list(range(1, num_lists + 1))
    plt.plot(list_sizes, linked_times, marker='o', label='Linked List')
    plt.plot(list_sizes, array_times, marker='o', label='Array')
    plt.xlabel('List Size')
    plt.ylabel('Runtime (seconds)')
    plt.title('Performance of Push and Pop Operations')
    plt.legend()
    plt.show()

plot_results(linked_times, array_times)





 

