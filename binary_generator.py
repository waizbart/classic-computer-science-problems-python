from queue_implement import Queue

def binary_generator(n):
    if n <= 0:
        print('n deve ser maior ou igual a 1')
        return
    
    q = Queue()
    
    q.push('1')
    
    if n == 1:
        return q
    
    for i in range(2, n + 1):
        b = ''
        
        prox = i
        
        while True:
            rest = prox % 2
            prox = prox // 2
            
            b += str(rest)
            
            if prox < 2:
                b += str(prox)
                break
            
        q.push(b[::-1])
        
    return(q)

if __name__ == "__main__":
    t1 = binary_generator(5) 
    t2 = binary_generator(4) 
    t3 = binary_generator(10) 
    
    print(t1)
    print(t2)
    print(t3)