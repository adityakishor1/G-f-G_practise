class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        n=len(s)
        mod=10**9+7
        res=[0 for _ in range(n+1)]
        for i in range(n):
            res[i+1]=(res[i]*10+(i+1)*(ord(s[i])-ord('0')))%mod
        return sum(res) %mod
        
