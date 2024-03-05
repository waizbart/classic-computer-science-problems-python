from stack import Stack

if __name__ == "__main__":
    my_stack = Stack()
    
    s = input("Parenteses: ")
    
    for i in s:
        my_stack.push(i)
    
    v = 0
        
    while not my_stack.is_empty():
        curr_value = my_stack.pop()
        
        print(curr_value)
        
        if curr_value == ')':
            v += 1
        else:
            if v == 0:
                v = 999
                break    
            v -= 1
            
    if v == 0:
        print("TRUE")
    else:
        print("FALSE")