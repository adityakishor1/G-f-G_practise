class Solution:
    def getSingle(self, arr):
        result = 0
        for num in arr:
            result ^= num
        return result
