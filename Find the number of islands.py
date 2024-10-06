class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 8 directions
        
        def iterative_dfs(x, y):
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                grid[cx][cy] = 0
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        stack.append((nx, ny))
                        grid[nx][ny] = 0  

        island_count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    island_count += 1
                    iterative_dfs(i, j)
        
        return island_count
