class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def RemoveHalfNodes(self, node):
        if not node:
            return None
        node.left = self.RemoveHalfNodes(node.left)
        node.right = self.RemoveHalfNodes(node.right)
        if node.left and not node.right:
            return node.left
        if node.right and not node.left:
            return node.right
        return node

    def inorderTraversal(self, root):
        result = []
        self.inorderHelper(root, result)
        return result

    def inorderHelper(self, node, result):
        if node:
            self.inorderHelper(node.left, result)
            result.append(node.value)
            self.inorderHelper(node.right, result)
