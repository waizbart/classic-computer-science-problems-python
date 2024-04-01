from queue_implement import Queue

def intercalate(q: Queue):
    original_length = q.length
    q1, q2 = split_queue(q)
    
    next_q = 1
    
    while q.length != original_length:
        if next_q == 1:
            q.push(q1.pop())
            next_q = 2
        else:
            q.push(q2.pop())
            next_q = 1
    
def split_queue(q: Queue):
    q1 = Queue()
    q2 = Queue()
    
    middle = q.length / 2
    
    while not q.is_empty():
        if q.length <= middle:
            q2.push(q.pop())
        else:
            q1.push(q.pop())
    return q1, q2

if __name__ == "__main__":
    new_q = Queue()
    
    new_q.push(1)
    new_q.push(2)
    new_q.push(3)
    new_q.push(4)
    new_q.push(5)
    new_q.push(6)
    new_q.push(7)
    new_q.push(8)
    
    intercalate(new_q)
    
    print(new_q)
    