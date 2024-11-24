class Solution:
    def maxSubArraySum(self, arr):
        # Initialize variables
        max_so_far = arr[0]  
        current_max = arr[0]          
        for i in range(1, len(arr)):
            current_max = max(arr[i], current_max + arr[i])
            max_so_far = max(max_so_far, current_max)
        
        return max_so_far
