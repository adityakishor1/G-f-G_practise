class Solution:
    def max_Books(self, n, k, arr):
        max_books = 0
        current_sum = 0
        start = 0
        
        for end in range(n):
            if arr[end] <= k:
                current_sum += arr[end]
                max_books = max(max_books, current_sum)
            else:
                current_sum = 0
                start = end + 1
        
        return max_books
