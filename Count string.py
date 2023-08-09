class Solution:
    # Version 1: Top down DP
    # TC: O(n * k * 2 * n) = O(kn^2), SC: O(n * k * 2 * n) = O(kn^2)
    def countStrings(self, n : int, s : str, k : int) -> int:
        # code here
        
        def pick(index, cont, pre, balance, dp):
            if balance < 0 or cont > k:
                return 0
            if index == n:
                return int(balance == 0)
            if s[index] == "(":
                if pre == 0:
                    nextCnt = cont + 1
                else:
                    nextCnt = 1
                return pick(index + 1, nextCnt, 0, balance + 1, dp)
            elif s[index] == ")":
                if pre == 1:
                    nextCnt = cont + 1
                else:
                    nextCnt = 1
                return pick(index + 1, nextCnt, 1, balance - 1, dp)
            if (index, cont, pre, balance) in dp:
                return dp[index, cont, pre, balance]
            res = 0
            if pre == 0:
                res = (res + pick(index + 1, cont + 1, 0, balance + 1, dp)) % M
                res = (res + pick(index + 1, 1, 1, balance - 1, dp)) % M
            else:
                res = (res + pick(index + 1, 1, 0, balance + 1, dp)) % M
                res = (res + pick(index + 1, cont + 1, 1, balance - 1, dp)) % M
            dp[index, cont, pre, balance] = res
            return res
            
        M = 10**9 + 7
        dp = {}
        return pick(0, 0, 0, 0, dp)
