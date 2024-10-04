class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head
        
        prev = None
        current = head
        next_node = None
        start = head
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == start:
                break
        head.next = prev
        head = prev
        return head
    def deleteNode(self, head, key):
        if not head:
            return None
        if head.data == key and head.next == head:
            return None
        
        current = head
        prev = None
        if head.data == key:
            while current.next != head:
                current = current.next
            
            current.next = head.next
            head = head.next
            return head
        current = head
        while True:
            if current.data == key:
                prev.next = current.next
                break
            prev = current
            current = current.next
            if current == head: 
                break
        
        return head
    def deleteAndReverse(self, head, key):
        head = self.deleteNode(head, key)
        head = self.reverse(head)
        return head
