class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    class Info:
        def __init__(self, is_bst, size, min_val, max_val):
            self.is_bst = is_bst
            self.size = size
            self.min_val = min_val
            self.max_val = max_val

    def largestBst(self, root):
        def helper(node):
            if not node:
                return Solution.Info(True, 0, float('inf'), float('-inf'))
            
            left_info = helper(node.left)
            right_info = helper(node.right)
            
            if left_info.is_bst and right_info.is_bst and left_info.max_val < node.data < right_info.min_val:
                is_bst = True
                size = left_info.size + right_info.size + 1
                min_val = min(left_info.min_val, node.data)
                max_val = max(right_info.max_val, node.data)
            else:
                is_bst = False
                size = max(left_info.size, right_info.size)
                min_val = float('-inf')
                max_val = float('inf')
            
            self.largest_bst_size = max(self.largest_bst_size, size if is_bst else 0)
            
            return Solution.Info(is_bst, size, min_val, max_val)

        self.largest_bst_size = 0
        helper(root)
        return self.largest_bst_size

def build_tree(level_order):
    if not level_order or level_order[0] == 'N':
        return None
    
    root = TreeNode(int(level_order[0]))
    queue = [root]
    i = 1
    while queue and i < len(level_order):
        current = queue.pop(0)
        
        if i < len(level_order) and level_order[i] != 'N':
            current.left = TreeNode(int(level_order[i]))
            queue.append(current.left)
        i += 1
        
        if i < len(level_order) and level_order[i] != 'N':
            current.right = TreeNode(int(level_order[i]))
            queue.append(current.right)
        i += 1
    
    return root
