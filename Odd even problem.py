class Solution:
    def oddEven(self, s: str) -> str:
        from collections import Counter
        freq = Counter(s)
        x = 0
        y = 0
        for char, count in freq.items():
            position = ord(char) - ord('a') + 1
            
            if position % 2 == 0:  
                if count % 2 == 0: 
                    x += 1
            else:  
                if count % 2 == 1:  
                    y += 1
        if (x + y) % 2 == 0:
            return "EVEN"
        else:
            return "ODD"
