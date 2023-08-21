class Solution:
     def solveQueries(self, N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
        # code here
        suffix = [[0]*(N + 1) for _ in range(N + 1)]
        for i in range(N):
            cnt = 0
            for j in range(i, N):
                if A[i] == A[j]:
                    cnt += 1
            suffix[i][cnt] += 1
            
        for i in range(N - 1, 0, -1):
            for j in range(N + 1):
                suffix[i - 1][j] += suffix[i][j]
        
        ans = []
        for l, r, k in Q:
            ans.append(suffix[l][k] - suffix[r + 1][k])
        return ans
