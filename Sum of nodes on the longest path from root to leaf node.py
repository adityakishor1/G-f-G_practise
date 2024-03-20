class Solution:
    def sumOfLongRootToLeafPath(self,root):
        def dfs(rot):
            if not rot:
                return(0,0)
            maxheight,maxsum=max(dfs(rot.left),dfs(rot.right))
            return (maxheight+1, maxsum+rot.data)
        return dfs(root)[1]
