class Solution:
    def DivisibleByEight(self,s):
        n= len(s)
        if n<3:
            if int(s)//8:
                return 1
            else:
                return -1
        x=s[-3:]
        if int(x)%8==0:
            return 1
        else:
            return -1
