class Solution:
    def kthElement(self, a, b, k):
        if len(a) > len(b):
            a, b = b, a
        
        n, m = len(a), len(b)
        low, high = max(0, k - m), min(k, n)  
        
        while low <= high:
            i = (low + high) // 2  
            j = k - i  
 
            a_left = a[i - 1] if i > 0 else float('-inf')
            a_right = a[i] if i < n else float('inf')
            b_left = b[j - 1] if j > 0 else float('-inf')
            b_right = b[j] if j < m else float('inf')
            if a_left <= b_right and b_left <= a_right:
                return max(a_left, b_left)   
            elif a_left > b_right:
                high = i - 1  
            else:
                low = i + 1 
        
        return -1  
