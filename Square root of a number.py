class Solution:
    def floorSqrt(self, n): 
        if n == 0 or n == 1:
            return n
        
        start = 1
        end = n
        ans = 0
        
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == n:
                return mid
            if mid * mid < n:
                start = mid + 1
                ans = mid  
            else:
                end = mid - 1
        
        return ans
