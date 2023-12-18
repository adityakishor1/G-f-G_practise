class Solution:
    def gameOfXor(self, N , A):
        if N % 2 == 0:
            return 0
        final_xor = 0
        for i in range(N):
            if i % 2 == 0:
                final_xor ^= A[i]
        return final_xor
