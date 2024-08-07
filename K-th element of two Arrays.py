class Solution:
    def kthElement(self, k, arr1, arr2):
        n = len(arr1)
        m = len(arr2)
        
        if n > m:
            return self.kthElement(k, arr2, arr1)
        
        low, high = max(0, k - m), min(n, k)
        
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = k - mid1
            
            left1 = arr1[mid1 - 1] if mid1 > 0 else float('-inf')
            left2 = arr2[mid2 - 1] if mid2 > 0 else float('-inf')
            right1 = arr1[mid1] if mid1 < n else float('inf')
            right2 = arr2[mid2] if mid2 < m else float('inf')
            
            if left1 <= right2 and left2 <= right1:
                return max(left1, left2)
            elif left1 > right2:
                high = mid1 - 1
            else:
                low = mid1 + 1
                
        return -1 
