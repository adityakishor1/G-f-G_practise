from typing import List

class Solution:
    def countPartitions(self, n: int, d: int, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        total_sum = sum(arr)
        target = (total_sum + d) // 2
        if (total_sum + d) % 2 != 0 or d > total_sum:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % MOD
        
        return dp[target]
