import random
import timeit

#Ex 2.1

class PriorityQueueMergesort:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        self.queue = self.mergesort(self.queue)

    def mergesort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.mergesort(left_half)
            self.mergesort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1
        return array

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

#Ex 2.2

class PriorityQueueSortedInsertion:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        if not self.queue:
            self.queue.append(item)
        else:
            for i in range(len(self.queue)):
                if item < self.queue[i]:
                    self.queue.insert(i, item)
                    break
            else:
                self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

#Ex 2.3

def generate_tasks():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7:  # Enqueue with probability 0.7
            tasks.append(('enqueue', random.randint(1, 100)))
        else:  # Dequeue with probability 0.3
            tasks.append(('dequeue', None))
    return tasks

#Ex 2.4

def measure_performance(pq_class, task_lists):
    times = []
    for tasks in task_lists:
        pq = pq_class()
        start_time = timeit.default_timer()
        for task, value in tasks:
            if task == 'enqueue':
                pq.enqueue(value)
            elif task == 'dequeue':
                pq.dequeue()
        times.append(timeit.default_timer() - start_time)
    return sum(times) / len(times)

task_lists = [generate_tasks() for _ in range(100)]
mergesort_time = measure_performance(PriorityQueueMergesort, task_lists)
sorted_insertion_time = measure_performance(PriorityQueueSortedInsertion, task_lists)

print(f'Mergesort Priority Queue Average Time: {mergesort_time}')
print(f'Sorted Insertion Priority Queue Average Time: {sorted_insertion_time}')

#Ex 2.5
#In conclusion we can see that the sorted insertion priority queue has a much smaller average time
#However we can also note that merge sort queue may perform better when there are many dequeues relative to enqueues
#since the the cost of sorting is amortized over multiple dequeues. 
#Lastly sorted insertion in the queue is likely more efficient when enqueue opterations dominate,
#as the list size grows as it maintains a sorted order with each insertion not needing a complete sort after 
#every enqueue. The best choice depends on the specific use case and ratio of enqueue and dequeue operations.