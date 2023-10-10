class Solution:
    def addNodesBelowAtK(self, root, k, ans):
        if root is None or k < 0:
            return
        
        if k == 0:
            ans.append(root.data)
            return
        
        self.addNodesBelowAtK(root.left, k - 1, ans)
        self.addNodesBelowAtK(root.right, k - 1, ans)

    def findTargetNode(self, root, target):
        if root is None:
            return None
        
        if root.data == target:
            return root
        
        l = self.findTargetNode(root.left, target)
        r = self.findTargetNode(root.right, target)

        if l:
            return l
        if r:
            return r

        return None

    def addNodesOnAncestorAtK(self, root, target, k, ans):
        if root is None:
            return -1
        
        if root == target:
            return 0
        
        l = self.addNodesOnAncestorAtK(root.left, target, k, ans)
        
        if l >= 0:
            if l + 1 == k:
                ans.append(root.data)
            else:
                self.addNodesBelowAtK(root.right, k - 2 - l, ans)
            return l + 1
        
        r = self.addNodesOnAncestorAtK(root.right, target, k, ans)
        
        if r >= 0:
            if r + 1 == k:
                ans.append(root.data)
            else:
                self.addNodesBelowAtK(root.left, k - 2 - r, ans)
            return r + 1
        
        return -1

    def KDistanceNodes(self, root, target, k):
        ans = []

        targetNode = self.findTargetNode(root, target)

        self.addNodesBelowAtK(targetNode, k, ans)
        self.addNodesOnAncestorAtK(root, targetNode, k, ans)

        ans.sort()
        return ans
        # return the sorted list all nodes at k distance from target
