class Solution:
    def segregate0and1(self, arr):
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] == 1:
                arr[left], arr[right] = arr[right], arr[left]
                right -= 1
            else:
                left += 1
