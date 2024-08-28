from collections import Counter

class Solution:
    def sortByFreq(self, arr):
        freq = Counter(arr)
        arr.sort(key=lambda x: (-freq[x], x))
        
        return arr
