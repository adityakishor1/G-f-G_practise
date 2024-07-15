class Solution:
    def smallestNumber(self, s, d):
        if s > 9 * d or s < 1:
            return -1
        result = [0] * d
        for i in range(d - 1, -1, -1):
            if s >= 9:
                result[i] = 9
                s -= 9
            else:
                result[i] = s
                s = 0
        if result[0] == 0:
            result[0] = 1
            for i in range(1, d):
                if result[i] > 0:
                    result[i] -= 1
                    break
        return ''.join(map(str, result))

