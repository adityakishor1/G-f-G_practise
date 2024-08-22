from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        graph = defaultdict(list)
        in_degree = [0] * k
        order = ""
        
        for i in range(n - 1):
            word1 = dict[i]
            word2 = dict[i + 1]
            min_len = min(len(word1), len(word2))
            
            for j in range(min_len):
                if word1[j] != word2[j]:
                    graph[ord(word1[j]) - ord('a')].append(ord(word2[j]) - ord('a'))
                    in_degree[ord(word2[j]) - ord('a')] += 1
                    break
        
        queue = deque()
        
        for i in range(k):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            order += chr(node + ord('a'))
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) < k:
            return ""
        
        return order
