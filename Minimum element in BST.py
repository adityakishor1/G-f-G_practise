class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        if not root:
            return None
        if not root.left:
            return root.data
        return self.minValue(root.left)
        ##Your code here
