class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def deleteK(self, head, k):
        if not head or k <= 1:
            return None
        
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        count = 0
        
        while head:
            count += 1
            if count % k == 0:
                prev.next = head.next
                head = prev.next  # Move head to the next node
            else:
                prev = head
                head = head.next
        
        return dummy.next
