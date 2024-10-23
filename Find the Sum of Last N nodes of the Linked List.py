

class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None

class Solution:
    def sumOfLastN_Nodes(self, head, n):
        # Initialize two pointers
        first = head
        second = head
        for _ in range(n):
            if first:
                first = first.next
                while first:
            first = first.next
            second = second.next
        total_sum = 0
        while second:
            total_sum += second.data
            second = second.next
        
        return total_sum
