class Solution:
    def absolute_diff(self,root):
        inarr=[]
        def inorder(node):
            if not node:
                 return
            inorder(node.left)
            inarr.append(node.data)
            inorder(node.right)
        inorder(root)
        i=0
        j=i+1
        res=float("inf")
        while j<len(inarr):
            if inarr[j]-inarr[i]<res:
                res=inarr[j]-inarr[i]
            i+=1
            j+=1
        return res
