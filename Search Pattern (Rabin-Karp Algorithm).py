class Solution:
    def search(self, pattern, text):
        res=[]
        n=len(pattern)
        for i in range(len(text)):
            if text[i:i+n]==pattern:
                res.append(i+1)
        return res
        
        
