class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        n = len(arr1)
        if n > len(arr2):
            return self.sum_of_middle_elements(arr2, arr1)
        
        low, high = 0, n
        
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = n - partition1
            
            maxLeft1 = float('-inf') if partition1 == 0 else arr1[partition1 - 1]
            minRight1 = float('inf') if partition1 == n else arr1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else arr2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else arr2[partition2]
            
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                return max(maxLeft1, maxLeft2) + min(minRight1, minRight2)
            
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1

        raise ValueError("Input arrays are not sorted or have invalid sizes.")
