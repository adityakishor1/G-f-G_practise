def util(s,r,n):
    if r==0:
        return s[n]
    else:
        step=""
        for i in range (n//2+1):
            if s[i]=="1":
                step+="10"
            else:
                step+="01"
    return util(step,r-1,n)
                
class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        return util(s,r,n)
