from collections import deque

class Solution:
    
    def max_of_subarrays(self, k, arr):
        n = len(arr)
        if n * k == 0:
            return []
        if k == 1:
            return arr
        
        dq = deque()
        max_elements = []
        
        for i in range(n):
            if dq and dq[0] < i - k + 1:
                dq.popleft()
                
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
                
            dq.append(i)
            
            if i >= k - 1:
                max_elements.append(arr[dq[0]])
        
        return max_elements
