import sys

class Solution:
	def min_operations(self,nums):
	    n=len(nums)
	    res=1
	    dp=[1]*(n)
	    for i in range(1,n):
	        for j in range(i):
	            if(nums[i]>nums[j] and i-j<=nums[i]-nums[j]):
	                dp[i]=max(dp[i],dp[j]+1)
	        res=max(res,dp[i])
	    return n-res
