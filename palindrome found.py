class Solution:
    def is_palindrome(self, lst):
        return lst == lst[::-1]

    def pattern(self, arr):
        n = len(arr)
        for i in range(n):
            if self.is_palindrome(arr[i]):
                return "{} R".format(i)
        for j in range(n):
            col = [arr[i][j] for i in range(n)]
            if self.is_palindrome(col):
                return "{} C".format(j)
        return "-1"

