class Solution:
    def countStr(self, n):
        ans = (1 + 2*n) + (n*(n*n - 1)//2)
        return ans
