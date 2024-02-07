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



    


