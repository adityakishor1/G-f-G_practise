class Solution:
    # Function to check whether a binary tree is balanced or not.
    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root):
        if root is None:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if (abs(left_height - right_height) == 0 or abs(left_height - right_height) == 1) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
