class Solution:
	def nthPoint(self, n):
	    zeroth_step = 1
        first_step = 1
        steps = 0
        mod = int(1e9 + 7)
        for ith_step in range(2, n + 1):
            steps = (first_step%mod + zeroth_step%mod)%mod
            zeroth_step = first_step
            first_step = steps
        return first_step
