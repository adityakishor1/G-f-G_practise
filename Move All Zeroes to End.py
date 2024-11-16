class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        non_zero_index = 0
        
        for i in range(n):
            if arr[i] != 0:
                arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
                non_zero_index += 1
