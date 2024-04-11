class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self,n):
        binary=bin(n)[2:]
        res=binary[0]
        for i in range(1,len(binary)):
            res+=str(int(res[-1])^int(binary[i]))
        return int(res,2)
