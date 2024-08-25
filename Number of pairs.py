import bisect

class Solution:
    def countPairs(self, arr, brr):
        brr.sort()
        count_y1 = brr.count(1)
        count_y2 = brr.count(2)
        count_y3 = brr.count(3)
        count_y4 = brr.count(4)

        total_pairs = 0

        for x in arr:
            if x == 1:
                continue
            idx = bisect.bisect_right(brr, x)
            total_pairs += len(brr) - idx
            if x == 2:
                total_pairs -= count_y3 + count_y4
                total_pairs += count_y1
            elif x == 3:
                total_pairs += count_y2
                total_pairs += count_y1
            else:
                total_pairs += count_y1
        
        return total_pairs
