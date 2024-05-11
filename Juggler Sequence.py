class Solution:
    def jugglerSequence(self, n):
        sequence = [n]
        while n != 1:
            if n % 2 == 0:
                n = int(n ** (1 / 2))
            else:
                n = int(n ** (3 / 2))
            sequence.append(n)
        return sequence
