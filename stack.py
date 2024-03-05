class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self) -> None:
        self.top = None
        
    def peek(self):
        if self.is_empty():
            return None
        return self.top.value
    
    def is_empty(self):
        return not self.top
    
    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.top = new_node
        else:
            holding_pointer = self.top
            self.top = new_node
            self.top.next = holding_pointer
        
    def pop(self):
        if self.is_empty():
            return None
        holding_pointer = self.top
        self.top = self.top.next
        return holding_pointer.value
    
    def __repr__(self):
        s = ''
        current_node = self.top
        while current_node:
            s += str(current_node.value) + '\n'
            current_node = current_node.next
        return s
    
    