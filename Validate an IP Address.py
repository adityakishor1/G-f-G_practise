class Solution:
    def isValid(self, s):
        parts = s.split('.')
        if len(parts) != 4:
            return False
        
        for part in parts:
            if not part.isdigit():
                return False
            num = int(part)
            if num < 0 or num > 255:
                return False
            if part != str(num):
                return False
        
        return True
