Exercise 6.1
The differnce between arrayas and linked lists:
Arrays:
Advantages:
-Simple to use 
-Retrievals and replacements are quick if the index is known
making them highly efficient for tasks accessing elements frequently.
-Memory efficiency: Arrays are very space efficient for storing elements of the same data type and especially when the size is known in advance and is static.


Disadvantages:
-Adding and removing elements is a little compicated
-Fixed size arrays either limits space or wastes space
-Dynamic sized arrays requires copying

-Insertion is 𝑂(𝑛) in the worst case
-Deletion is 𝑂(𝑛) in the worst case

Linked lists:
Advantages:
-Simple to use (often a built-in type)
- Retrievals and replacements are quick if the index is known (𝑂(1))
-A dynamic size: linked lists are dynamic data structures that can easily grow or shrink, the allocate and deallocation of nodes

Disadvantages:
- Random Access: Access elements ar a specific position requires traversing the list from the beginning to the desired position so you cannot accesss specific elements without going through the whole list first.
-Adding/removing elements may be awkward
-Fixed size arrays either limits the size of the list or wastes space
-Dynamic sized arrays requires copying

-Insertion and deletion are 𝑂(1)
-𝑂(𝑛) in the average and worst cases

Exercise 6.2
-For an unsorted array, the replace operation can simply overwrite the element at the desired index. This approach is highly efficient because it avoids the overhead of deletion and insertion.
-In a sorted array, if the replacement maintains the array's order, you can also overwrite the element directly as in the unsorted case. However, if the new value alters the sort order, you must find the correct position for the new value to keep the array sorted.

The best implementation strategy depends on the array's characteristics and the operations' frequency. Direct replacement is efficient for unsorted arrays or when the order is preserved. For sorted arrays where order changes, a combination of careful deletion and insertion with minimal shifting is preferable. For highly dynamic datasets, consider data structures like linked lists that minimize the cost of insertions and deletions.

Excercise 6.3
Implementing both methods are feasable 

Insertion Sort
-Firstly insertion Sort is suitable for doubly linked list as elements are reordered and put in the correct position one by one - through comparison with the previous element and finding the corresponding right spot for it. In a doubly linked list we can efficiently move backwards thanks to the previous pointers as well as forward to find correct position for each element. This eliminates the need for random access, which is a limition of linked lists in comparison to arrays. Additionally, swapping nodes or adjusting pointers does require shifting elements making insertion operations relatively efficient.

Merge Sort 
-Merge sort is also feasable and often recommended for sorting linked lists as it involves dividing the list into two halves sorting each half and merging the halves back together. The advantage of merge sort is that it does not require random access for efficient splitting or merging, make it well suited for linked lists. For a doubly linked list, merge operation can be efficiently implemented by adjusting pointers without needing additional space for arrays. The split operation can be performed by traversing the list from the beginning to find the middle point, which although not as efficient as in arrays is straightforward in a linked list environment. 

In summary, both insertion sort and merge sort are feasible for sorting a doubly linked list each having its own advantages. Insertion sort is more suitable for small lists or lists that are nearly sorted, while MergeSort provides a more efficient and stable sorting meechanism for larger lists.

Excercise 6.4

Insertion Sort
Complexity on Doubly Linked List:

Time Complexity: Average and worst-case time complexity is O(n^2)
Space Complexity: O(1)

In comparison to 

Complexity on Regular Array:
Average and worst-case time complexity is O(n^2)
Space Complexity: O(1)

The main difference in applying Insertion Sort to a doubly linked list versus an array lies in the traversal and swapping mechanism.

Merge Sort
Complexity on Doubly Linked List:

Time Complexity: O(n log n)

Space Complexity: O(1)

Complexity on Regular Array:

Time Complexity: O(n log n)

Space Complexity: O(n)

Differences: 
The most significant difference when applying Merge Sort to a doubly linked list instead of an array is in space complexity. For arrays, Merge Sort requires additional space proportional to the size of the array, making it O(n).