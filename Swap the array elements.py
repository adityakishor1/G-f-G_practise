class Solution:
	def swapElements(self, arr, n):
	    for i in range(n-2):
	        arr[i],arr[i+2]=arr[i+2],arr[i]
	    #Code here
