class Solution:
    def alternatingMaxLength(self, arr):
        if not arr:
            return 0
        up = 1
        down = 1
        
        # Traverse the array
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                up = down + 1
            elif arr[i] < arr[i - 1]:
                down = up + 1
        return max(up, down)
