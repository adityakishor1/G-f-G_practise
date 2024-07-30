from typing import List
class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        n = len(m)
        if m[0][0] == 0 or m[n-1][n-1] == 0:
            return []
        def is_safe(x, y):
            return 0 <= x < n and 0 <= y < n and m[x][y] == 1
        def dfs(x, y, path):
            if x == n - 1 and y == n - 1:
                result.append(path)
                return
            m[x][y] = -1
            for direction, (dx, dy) in zip('DLRU', [(1, 0), (0, -1), (0, 1), (-1, 0)]):
                nx, ny = x + dx, y + dy
                if is_safe(nx, ny):
                    dfs(nx, ny, path + direction)
            m[x][y] = 1
        
        result = []
        dfs(0, 0, "")
        return sorted(result)
