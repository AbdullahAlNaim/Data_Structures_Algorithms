class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def remove(self, value):
        if not self._length:
            raise Exception("List is empty")
        if self.head == value:
            return self.pop_left()
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None and curr_node.val != value:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            raise ValueError("Item not in list")
        if curr_node.next is None:
            self.tail = prev_node
        prev_node.next = curr_node.next
        curr_node.next = None
        self._length -= 1
        return curr_node.val