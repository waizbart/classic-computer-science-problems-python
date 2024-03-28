from stack import Node

class Queue:
    def __init__(self) -> None:
        self.last = None
        self.first = None
    
    def push(self, value):
        new_node = Node(value)
        if self.last is None:
            self.first = self.last = new_node
            return
        self.last.next = new_node
        self.last = new_node
        
    def pop(self):
        if self.first is None:
            return None
        removed_node = self.first
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return removed_node.value
    
    def peek(self):
        return self.first.value if self.first else None
    
    def is_empty(self):
        return self.first is None
    
    def __str__(self) -> str:
        result = []
        current = self.first
        while current:
            result.append(current.value)
            current = current.next
        return f"Queue: {result}"
    
    def __repr__(self) -> str:
        return self.__str__()

# Test
queue = Queue()
print(queue.is_empty()) # True
queue.push(1)
queue.push(2)
queue.push(3)

queue.pop()

print(queue) # Queue: [1, 2, 3]