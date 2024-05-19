from typing import List

class Solution:
    def findClosest(self, n: int, k: int, arr: List[int]) -> int:
        left, right = 0, n - 1
        closest = float('inf')

        # Binary search
        while left <= right:
            mid = left + (right - left) // 2
            if abs(arr[mid] - k) < abs(closest - k) or (abs(arr[mid] - k) == abs(closest - k) and arr[mid] > closest):
                closest = arr[mid]

            if arr[mid] == k:
                return arr[mid]
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1

        return closest
