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


arr = [3, 7, 2, 11, 9, 8, 5, 6]
heap = Heap()
heap.heapify(arr)
print(heap.heap_array)  
