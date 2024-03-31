class Solution:
    def findMaxForN(self, root, n):
        res=-1
        while(root):
            if root.key>n:
                root=root.left
            else:
                if root.key<=n:
                    res=root.key
                    root=root.right
        return res
