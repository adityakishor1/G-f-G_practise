class Solution:
    def minSteps(self, d):
        if d == 0:
            return 0
        
        steps = 0
        current_sum = 0
        direction = 1  
        
        while True:
            steps += 1
            current_sum += steps * direction
            
            if current_sum == d:
                return steps
            elif current_sum > d and (current_sum - d) % 2 == 0:
                return steps
            else:
                direction *= -1  
            
        return steps 
