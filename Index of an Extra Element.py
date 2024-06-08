class Solution:
    def findExtra(self, n, arr1, arr2):
        left, right = 0, n - 2
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr1[mid] == arr2[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
