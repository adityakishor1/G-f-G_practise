class Solution:
    def maximizeTheCuts(self, n, x, y, z):
        dp = [-1] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            if i >= x and dp[i - x] != -1:
                dp[i] = max(dp[i], dp[i - x] + 1)
            if i >= y and dp[i - y] != -1:
                dp[i] = max(dp[i], dp[i - y] + 1)
            if i >= z and dp[i - z] != -1:
                dp[i] = max(dp[i], dp[i - z] + 1)
        return dp[n] if dp[n] != -1 else 0
