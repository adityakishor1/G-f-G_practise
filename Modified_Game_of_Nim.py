class Solution:
    def findWinner(self, n, A):
        ans = 0
        for i in range(n):
            ans ^= A[i]
        if(ans == 0 or n%2 == 0):
            return 1
        else:
            return 2
