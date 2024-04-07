class Solution:
	def maxDotProduct(self, n, m, a, b):
	    
	    dp=[[0 for _ in range(m+1)]for _ in range(n+1)]
	    for i in range(n):
	        for j in range(min(m,i+1)):
	            dp[i+1][j+1]=max(dp[i][j+1],dp[i][j]+a[i]*b[j])
	    return dp[-1][-1]
