from typing import List

class Solution:
    def chefAndWells(self, n : int, m : int, c : List[List[str]]) -> List[List[int]]:
        from collections import deque
        dis = [[-1]*m for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(m):
                if c[i][j] == "W":
                    queue.append([i, j])
        
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        step = 2
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if c[nx][ny] in "NW":
                            continue
                        if dis[nx][ny] < 0:
                            dis[nx][ny] = step
                            queue.append([nx, ny])
            step += 2
        for i in range(n):
            for j in range(m):
                if c[i][j] in "NW.":
                    dis[i][j] = 0
        return dis
