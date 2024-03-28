from ListaSE import ListaSE
from node import Node

def find_n(head, n):
    curr = head
    count = 1
    
    while True:
        if curr:
            if count == n:
                return curr.value
            else:
                curr = curr.next
                count += 1
        else:
            return None
        
        
if __name__ == "__main__":
    lse = ListaSE()
    
    lse.insert(1)
    lse.insert(2)
    lse.insert(3)
    
    # testing function
    value = find_n(lse.head, 1)
    print(value)