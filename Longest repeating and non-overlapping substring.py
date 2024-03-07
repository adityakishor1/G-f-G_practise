class Solution:
    def longestSubstring(self, s , n):
        # code here 
        maxlen=0
        res="-1"
        i,j=0,0
        while i<n and j<n:
            ss=s[i:j+1]
            if s.find(ss,j+1)!=-1:
                sslen=len(ss)
                if sslen>maxlen:
                    res=ss
                    maxlen=sslen
            else:
                i+=1
            j+=1
        return res
