class Solution:
     def optimalArray(self, n : int, a : List[int]) -> List[int]:
        # code here
        left_sum = total_sum = 0
        j = 0
        ans = [0]*n
        for i in range(n):
            total_sum += a[i]
            half = i // 2
            if i % 2 == 0:
                left_sum += a[j]
                j += 1
            ans[i] = a[half]*(half + 1) - left_sum + total_sum - left_sum - a[half] *(i - half)
        return ans
