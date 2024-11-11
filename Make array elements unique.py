class Solution:
    def minIncrements(self, arr): 
        arr.sort()
        increments = 0
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                needed_increment = arr[i - 1] - arr[i] + 1
                increments += needed_increment
                arr[i] = arr[i - 1] + 1
        
        return increments
