class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def alternatingSplitList(self, head):
        if not head:
            return [None, None]
        
        head1 = tail1 = None
        head2 = tail2 = None
        
        current = head
        count = 1
        
        while current:
            if count % 2 != 0:
                if not head1:
                    head1 = tail1 = current
                else:
                    tail1.next = current
                    tail1 = tail1.next
            else:
                if not head2:
                    head2 = tail2 = current
                else:
                    tail2.next = current
                    tail2 = tail2.next
            
            current = current.next
            count += 1
        
        if tail1:
            tail1.next = None
        if tail2:
            tail2.next = None
        
        return [head1, head2]
