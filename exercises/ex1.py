from ListaSE import ListaSE
from node import Node

lse = ListaSE()

def add_end_elem(head, value):
    curr = head
    
    if not head:
        lse.insert(value)
    else:
        while True:
            if not curr.next:
                new_node = Node(value)
                curr.next = new_node
                break
            curr = curr.next
        
        
if __name__ == "__main__":
    
    # testing function pt2
    add_end_elem(lse.head, 0)
    
    # adding some elements 
    lse.insert(1)
    lse.insert(2)
    lse.insert(3)
    
    lse.display()
    
    # testing function pt2
    add_end_elem(lse.head, 4)
    
    lse.display()
    