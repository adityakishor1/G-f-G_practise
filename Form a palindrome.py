class Solution:
    def countMin(self, str):
        n = len(str)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if str[i] == str[j]:
                    if cl == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        lps = dp[0][n - 1]
        return n - lps
