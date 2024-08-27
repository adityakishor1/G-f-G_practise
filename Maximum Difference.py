class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        ls = [0] * n
        rs = [0] * n
        stack = []
        for i in range(n):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            ls[i] = stack[-1] if stack else 0
            stack.append(arr[i])
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            rs[i] = stack[-1] if stack else 0
            stack.append(arr[i])
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(ls[i] - rs[i]))
        
        return max_diff
