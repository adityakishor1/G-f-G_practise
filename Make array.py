class Solution:
    def makeArray(self, S : str, NUM : int, K : int) -> int:
        # code here
        n = len(S)
        M = 10**9 + 7
        val = [0]*(n + 1)
        base = 1
        for i in range(n - 1, -1, -1):
            val[i] = (val[i + 1] + int(S[i]) * base) % NUM
            base = (10 * base) % NUM
        
        dp = [[0]*2 for i in range(K + 1)]
        nextDp = [[0]*2 for i in range(K + 1)]
        dp[0][0] = 1
        for i in range(n - 1, -1, -1):
            nextDp[0][0] = dp[0][0]
            nextDp[0][1] = dp[0][1]
            for j in range(1, K + 1):
                nextDp[j][0] = dp[j][0]
                nextDp[j][1] = dp[j - 1][1]
                if val[i] == 0:
                    nextDp[j][0] += dp[j][1]
                    nextDp[j][1] += dp[j - 1][0]
                nextDp[j][0] %= M
                nextDp[j][1] %= M
            dp, nextDp = nextDp, dp
        return (dp[K][0] + dp[K][1]) % M
