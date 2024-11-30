from collections import Counter

class Solution:
    def areAnagrams(self, s1, s2):
        # Anagrams must have the same length
        if len(s1) != len(s2):
            return False
        return Counter(s1) == Counter(s2)
