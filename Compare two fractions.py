class Solution:
    def compareFrac(self, str):
        frac1, frac2 = str.split(', ')
        num1, den1 = map(int, frac1.split('/'))
        num2, den2 = map(int, frac2.split('/'))
        val1 = num1 / den1
        val2 = num2 / den2
        if val1 > val2:
            return frac1
        elif val1 < val2:
            return frac2
        else:
            return "equal"
