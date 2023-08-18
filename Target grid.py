class Solution:
    
    def gridSum(self,grid, k):
        #code here
        m = len(grid)
        n = len(grid[0])
        minv = [[0]*n for _ in range(m)]
        maxv = [[0]*n for _ in range(m)]
        minv[0][0] = maxv[0][0] = grid[0][0]
        for i in range(1, m):
            minv[i][0] = minv[i - 1][0] + grid[i][0]
            maxv[i][0] = maxv[i - 1][0] + grid[i][0]
        
        for i in range(1, n):
            minv[0][i] = minv[0][i - 1] + grid[0][i]
            maxv[0][i] = maxv[0][i - 1] + grid[0][i]
        
        for i in range(1, m):
            for j in range(1, n):
                minv[i][j] = min(minv[i - 1][j], minv[i][j - 1]) + grid[i][j]
                maxv[i][j] = max(maxv[i - 1][j], maxv[i][j - 1]) + grid[i][j]
        #print(minv[-1][-1], maxv[-1][-1])
        return int(minv[-1][-1] <= k <= maxv[-1][-1] and (k - minv[-1][-1]) % 2 == 0)
        
