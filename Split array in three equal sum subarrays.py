class Solution:
    def findSplit(self, arr):
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return [-1, -1]
        
        target_sum = total_sum // 3
        n = len(arr)
        
        current_sum = 0
        count = 0
        split_indices = []
        
        for i in range(n):
            current_sum += arr[i]
            if current_sum == target_sum:
                split_indices.append(i)
                current_sum = 0
                count += 1
            if count == 2:
                break
        if len(split_indices) == 2:
            return [split_indices[0], split_indices[1]]
        else:
            return [-1, -1]
