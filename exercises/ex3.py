from ListaCircular import ListaCircular

if __name__ == "__main__":
    lsec = ListaCircular()
    
    # adding elements
    lsec.insert(1)
    lsec.insert(2)
    lsec.insert(3)
    lsec.insert(4)
    lsec.insert(5)
    
    lsec.display()
    
    k = 2
    
    for _ in range(k):
        lsec.head = lsec.head.next
    
    lsec.display()
