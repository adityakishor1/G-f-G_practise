class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None

class Solution:
    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def addOne(self, head):
        head = self.reverse(head)
        current = head
        carry = 1
        
        while current is not None:
            current.data += carry
            if current.data >= 10:
                current.data = 0
                carry = 1
            else:
                carry = 0
            
            if carry == 0:
                break
            
            if current.next is None and carry == 1:
                current.next = Node(1)
                carry = 0
            
            current = current.next
        head = self.reverse(head)
        return head
