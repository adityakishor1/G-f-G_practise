class Solution(object):
    def sortedArrayToBST(self, nums):
        def helper(s, e):
            if s>e: return None
            m = (s+e)/2
            node = TreeNode(nums[m])
            node.left = helper(s, m-1)
            node.right = helper(m+1, e)
            return node
        return helper(0, len(nums)-1)
