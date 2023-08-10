 class solution:
     def goodSubtrees(self, root, k):
        #code here
        
        def dfs(node, ans):
            if node is None:
                return 0
            res = (1<<node.data)
            res = res | dfs(node.left, ans) | dfs(node.right, ans)
            if bin(res).count("1") <= k:
                ans[0] += 1
            return res
            
        ans = [0]
        dfs(root, ans)
        return ans[0]
