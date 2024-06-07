class Solution:
    def maxOccured(self, n, l, r, maxx):
        arr = [0] * (maxx + 2)
        for i in range(n):
            arr[l[i]] += 1
            if r[i] + 1 <= maxx:
                arr[r[i] + 1] -= 1
        max_occurrence = arr[0]
        index = 0
        for i in range(1, maxx + 1):
            arr[i] += arr[i - 1]
            if arr[i] > max_occurrence:
                max_occurrence = arr[i]
                index = i
        
        return index
