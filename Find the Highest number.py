from typing import List

class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        n = len(a)
        if n == 1:
            return a[0]

        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2

            if a[mid] > a[mid + 1]:  # decreasing
                right = mid
            else:
                left = mid + 1

        return a[left]
