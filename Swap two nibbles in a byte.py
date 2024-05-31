class Solution:
    def swapNibbles(self, n):
        binary = bin(n)[2:]
        binary = binary.zfill(8)
        swapped_binary = binary[4:] + binary[:4]
        result = int(swapped_binary, 2)
        
        return result
