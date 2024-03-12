#User function Template for python3
import numpy as np
class Solution:
    def genFibNum(self, a, b, c, n, m):
        if n<=2:
            return 1
        res=np.array([
             [1,0,0],
             [0,1,0],
             [0,0,1]
        ])
        genfib=np.array([
             [a,b,c],
             [1,0,0],
             [0,0,1]
        ])
        n-=2
        while n:
            if n&1:
                res=np.matmul(res,genfib)%m
            genfib=np.matmul(genfib,genfib)%m
            n>>=1
        return sum(res[0])%m
