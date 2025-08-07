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
    
    def prepend(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._length += 1
        return self
    
    def pop_left(self):
        if not self._length:
            raise Exception("List is empty.")
        
        former_head = self.head
        self.head = former_head.next
        former_head.next = None
        self._length -= 1

        if not self._length:
            self.tail = None
        return former_head.value
    
    def pop_right(self):
        if not self._length:
            raise Exception("List is empty.")
        
        former_tail = self.tail.value

        if self._length == 1:
            self.head = self.tail = None
        else:
            temp_node = self.head
            while temp_node.next != self.tail:
                temp_node = temp_node.next

            self.tail = temp_node
            self.tail.next = None

        self._length -= 1
        return former_tail.value
    
    def remove(self, value):
        if not self._length:
            raise Exception("List is empty.")
        if self.head == value:
            return self.pop_left()
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            raise ValueError("Item not in list")
        if current_node.next is None:
            self.tail = previous_node
        previous_node.next = current_node.next
        current_node.next = None
        self._length -= 1
        return current_node.value
    
        
    # reverse linked list
    # pointers left=none, middle=head, right=head.next
    # middle.next = left
    # left = middle
    # middle = right
    # right = right.next
    # after loop head, tail = tail, head

    def reverse(self):
        if not self._length:
            raise Exception("list is empty")
        
        if self._length == 1:
            return self
        
        left = None
        middle = self.head
        while middle != None:
            right = middle.next
            middle.next = left
            left = middle
            middle = right

        self.head, self.tail = self.tail, self.head
        return self
        
        