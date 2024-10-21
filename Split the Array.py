MOD = 10**9 + 7

class Solution:
	def countgroup(self, arr):
		n = len(arr)
		total_xor = 0
		for num in arr:
			total_xor ^= num
		if total_xor != 0:
			return 0
		ways = (pow(2, n-1, MOD) - 1 + MOD) % MOD
		return ways
