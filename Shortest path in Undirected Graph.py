from collections import deque, defaultdict

class Solution:
    def shortestPath(self, edges, n, m, src):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dist = [float('inf')] * n
        dist[src] = 0
        queue = deque([src])
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if dist[neighbor] > dist[node] + 1:
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i] = -1
        
        return dist
