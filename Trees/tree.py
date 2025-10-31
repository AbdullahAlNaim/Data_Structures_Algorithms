class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return self
        
        current_node = self.root
        while value != current_node.value:
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    break
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    break
                current_node = current_node.right
        return self
    
    def contains(self, value):
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return True
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
    
    def remove(self, value, start=None, parent=None):
        current = start or self.root
        while current and current.value != value:
            parent = current
            if value < current.value:
                current = parent.left
            else:
                current = parent.right
        if not current:
            raise Exception("item not in tree")
        if not current.right and not current.left:
            return self._remove_node_two_children(current, parent)
        if current.right and current.left:
            return self._remove_node_two_children(current)
        return self._remove_node_one_child(current, parent)