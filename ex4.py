from ListaDuplamenteLigada import ListaDuplamenteLigada

def fusion(head1, head2):
    pass

if __name__ == "__main__":
    lsec1 = ListaDuplamenteLigada()
    lsec2 = ListaDuplamenteLigada()
    
    lsec1.append(0)
    lsec1.append(0)
    lsec1.append(0)
    lsec1.append(0)
    lsec1.append(0)
    
    lsec1.display()
    
    lsec2.append(1)
    lsec2.append(1)
    lsec2.append(1)
    lsec2.append(1)
    lsec2.append(1)
    
    lsec2.display()
    
    new_lse = ListaDuplamenteLigada()
    
    curr_list = 1
    
    while True:
        if curr_list == 1:
            print(lsec1.remove())
        
    
