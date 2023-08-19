class Solution:
    # Version 1: Min
    # TC: O(n), SC: O(1)
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        # code here
        ans = float('inf')
        for i in range(N):
            ans = min(ans, time[i]*abs(cur - pos[i]))
        return ans
