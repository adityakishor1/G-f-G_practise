class Solution:
    
    def missingNumber(self, n, arr):
        total_sum = n * (n + 1) // 2
        arr_sum = sum(arr)
        missing = total_sum - arr_sum
        
        return missing
