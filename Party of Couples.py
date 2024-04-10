class Solution:
    def findSingle(self, n, arr):
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d.items():
            if i[1]%2!=0:
                return i[0]
