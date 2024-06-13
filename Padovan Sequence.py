class Solution:
    def padovanSequence(self, n):
        MOD = 10**9 + 7
        if n <= 2:
            return 1
        a, b, c = 1, 1, 1
        for _ in range(3, n+1):
            a, b, c = b, c, (a + b) % MOD
        return c
