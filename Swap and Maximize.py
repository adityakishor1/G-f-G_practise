class Solution:
    def maxSum(self, arr):
        arr.sort()
        left, right = 0, len(arr) - 1
        arranged = []
        while left <= right:
            if left == right:
                arranged.append(arr[left])
            else:
                arranged.append(arr[left])
                arranged.append(arr[right])
            left += 1
            right -= 1
        max_sum = 0
        for i in range(len(arranged)):
            max_sum += abs(arranged[i] - arranged[(i + 1) % len(arranged)])
        
        return max_sum
