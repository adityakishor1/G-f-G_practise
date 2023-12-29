class Solution:
	def kSubstrConcat(self, n, s, k):
		if n % k != 0:
		    return 0
		mp = {}
		for i in range(0, n, k):
		    mp[s[i:i+k]] = mp.get(s[i:i+k], 0) + 1
		if len(mp) == 1:
		    return 1
		if len(mp) != 2:
		    return 0
		if mp[list(mp.keys())[0]] == 1 or mp[list(mp.keys())[0]] == (n // k - 1):
		    return 1
		return 0
