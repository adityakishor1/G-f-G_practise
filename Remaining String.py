class Solution:
    def printString(self, s, ch, count):        occurrence = 0
        for i in range(len(s)):
            if s[i] == ch:
                occurrence += 1
                if occurrence == count:
                    return s[i+1:]
        return ""
