class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        cost = float('inf')
        
        workers = [(wage[i]/float(quality[i]), quality[i], wage[i]) for i in xrange(len(quality))]
        workers = sorted(workers)
        
        paidGroup = []
        sumQ = 0
        
        for r, q, w in workers:
            heapq.heappush(paidGroup, -q)
            sumQ += q
            
            if len(paidGroup)>k:
                sumQ -= -heapq.heappop(paidGroup)
            
            if len(paidGroup)==k:
                cost = min(cost, sumQ*r)
        
        return cost
