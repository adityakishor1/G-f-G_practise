class Solution:
    def totalCount(self, k, arr):
        total_parts = 0
        
        for num in arr:
            total_parts += num // k
            if num % k != 0:
                total_parts += 1
        
        return total_parts
