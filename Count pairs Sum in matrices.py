class Solution:
	def countPairs(self, mat1, mat2, n, x):
	    s=set()
	    res=0
	    for i in range(n):
	        for j in range(n):
	            s.add(mat2[i][j])
	    for i in range(n):
	       for j in range(n):
	           if x-mat1[i][j] in s:
	               res+=1
	    return res
		
