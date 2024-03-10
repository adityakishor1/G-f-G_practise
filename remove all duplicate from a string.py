class Solution:

	
	def removeDuplicates(self,str):
	    res=""
	    for i in str:
	        if i not in res:
	            res+=i
        return res
	    # code here
