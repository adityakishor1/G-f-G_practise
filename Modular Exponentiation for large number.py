class Solution:
    def PowMod(self, x, n, m):
        if n == 0:
            return 1 % m
        result = 1
        x = x % m
        
        while n > 0:
            if n % 2 == 1:
                result = (result * x) % m
            n = n // 2
            x = (x * x) % m
        
        return result
