class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def binary_search(self, num):
        left, right = 0, self.length() - 1
        while left <= right:
            mid = (left + right) // 2
            if self.get(mid).data == num:
                return True
            elif self.get(mid).data < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get(self, index):
        if index < 0 or index >= self.length():
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
