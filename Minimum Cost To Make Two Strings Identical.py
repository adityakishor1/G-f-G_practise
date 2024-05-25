class Solution:
    def findMinCost(self, x, y, costX, costY):
        m, n = len(x), len(y)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i * costX          
        # Fill the first row (0, j)
        for j in range(1, n + 1):
            dp[0][j] = j * costY 
   
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if x[i - 1] == y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  
                else:
                    delete_from_x = dp[i - 1][j] + costX  
                    delete_from_y = dp[i][j - 1] + costY 
                    dp[i][j] = min(delete_from_x, delete_from_y)

        return dp[m][n]
