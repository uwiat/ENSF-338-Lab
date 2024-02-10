def quicksort(arr, low, high):
    partitions = 0
    if low < high:
        pivot_index, new_partitions = partition(arr, low, high)
        partitions += new_partitions
        arr, new_partitions = quicksort(arr, low, pivot_index)
        partitions += new_partitions
        arr, new_partitions = quicksort(arr, pivot_index + 1, high)
        partitions += new_partitions
    return arr, partitions

def partition(arr, low, high):
    partitions = 0
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
            partitions += 1
        while arr[right] >= pivot and right >=left:
            right = right -1
            partitions += 1
        if right < left:
            done= True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right, partitions

arr1 = [2,1]
arr2 = [4,3,2,1]
arr3 = [6,5,4,3,2,1]
arr4 = [8,7,6,5,4,3,2,1]
arr5 = [10,9,8,7,6,5,4,3,2,1]

for arr in [arr1, arr2, arr3, arr4, arr5]:
    sorted_arr, partitions = quicksort(arr, 0, len(arr) - 1)
    print(f"Sorted array: {sorted_arr}")
    print(f"Number of inputs: {len(arr)}")
    print(f"Number of partitions: {partitions}\n")
    
    