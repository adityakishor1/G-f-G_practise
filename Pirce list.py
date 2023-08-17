class Solution:
    # Version 1: Sieve
    # Let v be the range of the value
    # TC: O(vloglogv + nlogv), SC: O(v)
    def primeList(self, head : Optional['Node']) -> Optional['Node']:
        # code here
        from bisect import bisect_left
        global maxv
        global hasCompute
        global prime
        
        if not hasCompute:
            hasCompute = True
            spf = list(range(maxv + 1))
            for i in range(2, maxv + 1):
                if spf[i] == i:
                    for j in range(i * i, maxv + 1, i):
                        spf[j] = min(spf[j], i)
            
            for i in range(2, maxv + 1):
                if spf[i] == i:
                    prime.append(i)
        
        current = head
        while current:
            index = bisect_left(prime, current.data)
            if index > 0 and index < len(prime):
                if current.data - prime[index - 1] <= prime[index] - current.data:
                    current.data = prime[index - 1]
                else:
                    current.data = prime[index]
            elif index > 0:
                current.data = prime[index - 1]
            else:
                current.data = prime[index]
            current = current.next
        return head
