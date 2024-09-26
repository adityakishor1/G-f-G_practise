class Solution:
    
    def maxStep(self, arr):
        max_steps = 0
        current_steps = 0
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                current_steps += 1
            else:
                current_steps = 0
            
            max_steps = max(max_steps, current_steps)
        
        return max_steps
