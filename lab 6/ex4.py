import random
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
    
def test_sorted_heap():
    
    input_array = [11, 9, 8, 7, 3, 2, 5, 6]
    heap = Heap()
    heap.heapify(input_array)
    expected_output = [11, 9, 8, 7, 3, 2, 5, 6]
    if heap.heap_array == expected_output:
        print("Test sorted heap passed.")
    else:
        print("Test sorted heap failed.")

def test_empty_array():
    
    input_array = []
    heap = Heap()
    heap.heapify(input_array)
    expected_output = []
    if heap.heap_array == expected_output:
        print("Test empty array passed.")
    else:
        print("Test empty array failed.")

def test_random_shuffle():
    input_array = list(range(1000))
    random.shuffle(input_array)
    heap = Heap()
    heap.heapify(input_array)
    

    is_heap = True
    for i in range(len(heap.heap_array)):
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2
        if left_child_idx < len(heap.heap_array) and heap.heap_array[i] < heap.heap_array[left_child_idx]:
            is_heap = False
            break
        if right_child_idx < len(heap.heap_array) and heap.heap_array[i] < heap.heap_array[right_child_idx]:
            is_heap = False
            break
    
    if is_heap:
        print("Test random shuffle passed.")
    else:
        print("Test random shuffle failed.")

test_sorted_heap()
test_empty_array()
test_random_shuffle()



