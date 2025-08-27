class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList():
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
            self.tail = new_node
        
        self._length += 1
        return self
    
    def pop_left(self):
        if not self._length:
            raise Exception("List is empty")
        
        if self._length < 2:
            self.head = self.tail = None
        
        former_head = self.head
        self.head = former_head.next
        former_head.next = None
        self._length -= 1

        if not self._length:
            self.tail = None

        return former_head.value



