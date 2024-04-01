from queue_implement import Queue

def reverse_queue(queue: Queue):
    if queue.is_empty():
        return
    value = queue.pop()
    reverse_queue(queue)
    queue.push(value)

if __name__ == "__main__":
    queue = Queue()
    
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    
    reverse_queue(queue)
    
    print(queue)