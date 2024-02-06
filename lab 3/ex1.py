def merge_sort(array, low,high):
    if low < high:
        mid = (low + high)//2
        merge_sort(array, low, mid)
        merge_sort(array, mid + 1, high)
        merge(array, low, mid, high)


def merge(arr, low, mid, high):
    left_part = arr[low:mid + 1]
    right_part = arr[mid + 1:high + 1]
    

    i = j = 0
    k = low

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1


    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1



    
#Q2 merge_sort function:
#The function divides the array into halves recursively until each subarray contains only one element. 
#This operation takes O(log n) time because the array is divided into halves in each recursive call until it reaches a size of 1.
#Then, the merge operation is called on each pair of subarrays. Since there are log n levels of recursion, 
#and at each level, each element in the array is merged exactly once, the total time complexity for merging all levels is O(n).
#merge function:
#The merge function iterates through each element of the two subarrays exactly once, comparing and merging 
#them into a single sorted array. This process takes O(n) time, where n is the total number of elements in the two subarrays.

