from typing import List

class Solution:
    def findPair(self, n: int, x: int, arr: List[int]) -> int:
        seen = set()  
        
        for num in arr:
            if num - x in seen or num + x in seen:
                return 1  
            
            seen.add(num)  
        
        return -1  
