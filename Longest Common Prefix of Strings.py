class Solution:
    def longestCommonPrefix(self, arr):
        if not arr:
            return "-1"
        min_length = min(len(s) for s in arr)
        
        if min_length == 0:
            return "-1"
        prefix = arr[0][:min_length]
        
        for i in range(min_length):
            char = prefix[i]
            for string in arr:
                if string[i] != char:
                    if i == 0:
                        return "-1"
                    else:
                        return prefix[:i]
        
        return prefix
