class Solution:
    def maxDifferenceBST(self,root, target):
        #code here
        def dfs(node):
            if not node:
                return float('inf')
            res = min(dfs(node.left), dfs(node.right))
            if res == float('inf'):
                res = 0
            return res + node.data
        
        current = root
        total = 0
        while current:
            if current.data == target:
                break
            total += current.data
            if current.data > target:
                current = current.left
            else:
                current = current.right
        
        if not current:
            return -1
        return total - dfs(current) + current.data
