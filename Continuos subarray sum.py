class Solution(object):
    def checkSubarraySum(self, nums, k):
        if len(nums)==0 or len(nums)==1: return False
        prefixSumKRemain = collections.defaultdict(list)
        
        prefixSum = 0
        for i, n in enumerate(nums):
            prefixSum += n
            remain = prefixSum%k
            
            if prefixSum%k==0 and i>=1: return True
            if len(prefixSumKRemain[remain])>0 and prefixSumKRemain[remain][0]<i-1:
                return True
            prefixSumKRemain[remain].append(i)
            
        return False
