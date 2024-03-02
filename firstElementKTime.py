class Solution:
    def firstElementKTime(self, n, k, a):
        if len(a)<k:
            return -1
        if k==1:
            return a[0]
        d={}
        for i in a:
            if i in d:
                d[i]+=1
                if d[i]==k:
                    return i
            else:
                d[i]= 1
        return -1
