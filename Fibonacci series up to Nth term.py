class Solution:
    def series(self, n):
        # Code here
        m=10**9+7
        res=[0,1]
        while len(res)<=n:
            res.append((res[-1]+res[-2])%m)
        return res
