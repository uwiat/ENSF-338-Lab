Excercise 7.1
To find an expression for the time complexity of the reverse() implementation shown in the picture given to us is firstly, consider the costliest operation which is the loop. Inside the loop the costliest operation seems to be 'get_element_at_poos(i)' which when traversing the list each time, gives us the series of opertions of O(n-1) + O(n-2) + ... + O(1) + O(0)

This series can be simplified to O(n(n-1)/2) which simplifies to 0(n^2). Hence the total time  completxity of the reverse function is O(n^2).

Excercise 7.2
To optimize the reverse functino for a doubly linked list, we can eliminate the need for indexing nodes which is not normally an operation for a linked list and is costly in terms of performance. Instead, we can traverse the list once and reverse the pointers as we go.

def reverse(self):
    current = self.head
    prev = None
    while current:
        next = current.next
        current.next = prev  # Reverse the next pointer
        current.prev = next  # Reverse the prev pointer for a doubly linked list
        prev = current
        current = next
    self.head = prev

-I eliminated the get_element_at_pos as we remoced the need to find a node by its position.
-The new algorith only makes one pass through the list starting from the head and going to the end. This means it runs in O(n) time, where n is the number of elements in the list.
-Pointer reversal where as we iteratet over the list we reverse the pointers in place. Making the time taken for the function to run substantially less.
-Since we deal with double linked list we need to reverse both next and prv pointers of each node which ensures that we maintain the bidirectional navigation of the doubly linked lists.

