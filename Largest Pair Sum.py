from typing import List

class Solution:
    def pairsum(self, arr: List[int]) -> int:
        first = second = -1
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num
        return first + second
