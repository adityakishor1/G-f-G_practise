class Solution:
    def maxIndexDiff(self,a, n): 
        res=0
        for i in range(n):
            j=n-1
            if j-i<=res:
                return res
            while j>=1 and a[j]<a[i]:
                j-=1
            res=max(res,j-i)
        return res
        ##Your code here
