class Solution(object):
    def copyRandomList(self, head):
        if not head: return head
        curr = head
        while curr:
            nextCurr = curr.next
            copy = Node(curr.val)
            curr.next = copy
            copy.next = nextCurr
            curr = nextCurr
        
        copyHead = head.next

        curr = head
        while curr:
            if curr.random: curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        while curr:
            nextCurr = curr.next.next
            if nextCurr:
                curr.next.next = nextCurr.next
            curr.next = nextCurr
            curr = nextCurr
        
        return copyHead
