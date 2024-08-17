class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left = [1] * n
        right = [1] * n
        product = [0] * n
        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]
        for i in range(n):
            product[i] = left[i] * right[i]
        
        return product
