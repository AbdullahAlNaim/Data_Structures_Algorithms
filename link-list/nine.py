class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
       

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def append(self, value):
        new_node = Node(value)

        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self._length += 1
        return self
    
    def prepend(self, value):
        new_node = Node(value)

        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self._length += 1
        return self