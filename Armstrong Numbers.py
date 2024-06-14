class Solution:
    def armstrongNumber (self, n):
        num_str = str(n)
        num_digits = len(num_str)
        sum_cubes = sum(int(digit) ** num_digits for digit in num_str)
        return str(sum_cubes == n).lower()
