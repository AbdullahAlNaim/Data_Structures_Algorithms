class Node:
    def __init__(self, value):
        self.value = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._lenth = 0

    def append(self, value):
        new_node = Node(value)
        if not self._lenth:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._lenth += 1
        return self
    

    

my_list = LinkedList()
my_list.append(5)

print(my_list.tail.value)