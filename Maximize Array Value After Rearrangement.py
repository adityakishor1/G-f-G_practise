
class Solution:
    def Maximize(self, arr): 
        arr.sort()
        result = 0
        mod = 10**9 + 7
        for i in range(len(arr)):
            result = (result + arr[i] * i) % mod
        
        return result
