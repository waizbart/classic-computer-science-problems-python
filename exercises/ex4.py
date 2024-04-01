from ListaDuplamenteLigada import ListaDuplamenteLigada

if __name__ == "__main__":
    lsec1 = ListaDuplamenteLigada()
    lsec2 = ListaDuplamenteLigada()
    
    lsec1.append(1)
    lsec1.append(1)
    lsec1.append(1)
    lsec1.append(1)
    lsec1.append(1)
    
    lsec1.display()
    
    lsec2.append(0)
    lsec2.append(0)
    lsec2.append(0)
    lsec2.append(0)
    lsec2.append(0)
    
    lsec2.display()
    
    new_lse = ListaDuplamenteLigada()
    
    def fusion(head1, head2, current=1):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if current == 1:
            head1.next = fusion(head1.next, head2, 2)
            return head1
        else:
            head2.next = fusion(head1, head2.next, 1)
            return head2
        
    new_lse.head = fusion(lsec1.head, lsec2.head)
    new_lse.display()
        
        
    
